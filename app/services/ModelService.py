from utils.ResultCloud import ResultCloud
from utils.ValidationResult import ValidationResult
from app.services.ProjectService import ProjectService
from app.services.RepositoryService import RepositoryService
from plugins.clanguage.Parser import Parser
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from app import models
from app import db
import config
import ntpath
import chardet

class ModelService(object):
    """ Update measurements of model """
    def _updateModelMeasurements(measurements, testCaseName, sample, response):
        # If the model exists, update it
        if not testCaseName in measurements:
            measurements[testCaseName] = ([], [])

        # Update model measurements
        measurements[testCaseName] = ModelService._updateSamplesFeatures(measurements[testCaseName], sample, response)
        return measurements

    """ Get dictionary of supported models """
    def _getSupportedModels():
        models = dict()
        models["GaussianNB"]  = { "name": "Gaussian Naive Bayes", "model": GaussianNB() }
        models["LogisticRegression"]  = { "name": "Logistic regression", "model": LogisticRegression(C=1., solver='lbfgs') }
        models["SVC"]  = { "name": "SVC", "model": LinearSVC() }
        models["CalibratedGaussianNBIsotonic"]  = { "name": "Gaussian Naive Bayes Isotonic", "model": CalibratedClassifierCV(GaussianNB(), cv=2, method='isotonic') }
        models["CalibratedGaussianNBSigmoid"]  = { "name": "Gaussian Naive Bayes Sigmoid", "model": CalibratedClassifierCV(GaussianNB(), cv=2, method='sigmoid') }
        models["CalibratedSVCIsotonic"]  = { "name": "SVC Isotonic", "model": CalibratedClassifierCV(LinearSVC(), cv=2, method='isotonic') }
        models["CalibratedSVCSigmoid"]  = { "name": "SVC Sigmoid", "model": CalibratedClassifierCV(LinearSVC(), cv=2, method='sigmoid') }
        
        return models

    """ Create models from data """
    def _createModels(X_train, X_test, y_train, y_test):
        # Init models dictionary
        models = list()

        # Create models
        # Model creation can fall, because some do not handle missing samples for class
        availableModels = ModelService._getSupportedModels()
        for key in availableModels:
            try:
                models.append(ModelService._fitAndEvaluateModel(key, availableModels[key]["model"], X_train, X_test, y_train, y_test))
            except ValueError:
                pass
 
        # Return models
        return models

    """ Fit and evaluate given model """
    def _fitAndEvaluateModel(id, model, X_train, X_test, y_train, y_test):
        # Init model info
        modelInfo = dict()
        modelInfo["identifier"] = id
        modelInfo["model"] = model        

        # Fit model
        modelInfo["model"].fit(X_train, y_train)

        # Test the model
        pred = modelInfo["model"].predict(X_test)
        modelInfo["accuracy"] = metrics.accuracy_score(y_test, pred)
        modelInfo["precision"] = metrics.precision_score(y_test, pred)
        modelInfo["recall"] = metrics.recall_score(y_test, pred)
    
        # Return fitted and evaluated model
        return modelInfo

    """ Create model for each test case """
    def _calculate(measurements):
        # Initialize classifiers
        classifiers = dict()

        # Create classifier for each model
        for key in measurements:
            # Initialize model
            classifiers[key] = { "models": dict(), "features": [] }
            vec = DictVectorizer()

            # Set vectorizer to use only selected features
            features = vec.fit_transform(measurements[key][0])
            # Init feature selection and use it
            support = SelectKBest(chi2, k=10).fit(features, measurements[key][1])
            vec.restrict(support.get_support()) 

            # Assign used features
            classifiers[key]["features"] = vec.get_feature_names()

            # Get selected features data
            data = vec.transform(measurements[key][0]).toarray()

            # We need to split these data to create learning and testing set
            X_train, X_test, y_train, y_test = train_test_split(data, measurements[key][1])
            
            # Fit all models
            classifiers[key]["models"] = ModelService._createModels(X_train, X_test, y_train, y_test)

        # Return result
        return classifiers

    """ Save classifiers into file """
    def _saveClassifiers(classifiers, path):
        parts = [ config.CLASSIFIERS, path, 'classifiers.pkl']
        joblib.dump(classifiers, ntpath.join(*parts))

    """ Load classifiers from file """
    def _loadClassifiers(path):
        try:
            parts = [ config.CLASSIFIERS, path, 'classifiers.pkl']
            return joblib.load(ntpath.join(*parts))
        except FileNotFoundError:
            return dict()

    """ Extract test cases from submission """
    def _extractTestCases(submission):
        # Init test cases
        testCases = []

        # Iterate through categories
        for category in submission["Categories"]:
            testCases = testCases + category["TestCases"]

        # Return result
        return testCases

    """ Transform difference into vector """
    def _diffObjectToSample(difference):
        # Initialize dictionary to be later transformed
        sample = dict()

        # It holds files, so go through them
        for file in difference["files"]:
            # First all the added changes
            for key, value in file["added"]["changes"].items():
                sample[file["name"] + "_added_" + key] = value

            # And now the removed ones
            for key, value in file["removed"]["changes"].items():
                sample[file["name"] + "_removed_" + key] = value

        return sample

    """ Update tuple of samples and features """
    def _updateSamplesFeatures(measurements, diffObject, feature):
        measurements[0].append(ModelService._diffObjectToSample(diffObject))
        measurements[1].append(feature)

        return measurements

    """ Load models of project """
    def load(project_id):
        # Load classifiers from file
        classifiers = ModelService._loadClassifiers("project_" + project_id)

        # Init validation with result data
        validation = ValidationResult([])

        # Iterate through classifiers and create user friendly output
        for key in classifiers:
            # Init classifier and fill it
            classifier = dict()
            classifier["name"] = key
            classifier["features"] = list()
            classifier["models"] = list()

            # Map features
            for feature in classifiers[key]["features"]:
                featureInfo = dict()
                # Get information from string
                parts = feature.split("_")
                
                # Fill info
                featureInfo["file"] = parts[0]
                featureInfo["state"] = parts[1]
                featureInfo["change"] = parts[2]

                # Add to features list
                classifier["features"].append(featureInfo)                


            supportedModels = ModelService._getSupportedModels()
            accuracy = 0
            # Load each classifier   
            for model in classifiers[key]["models"]:
                modelInfo = dict()
                modelInfo["name"] =  supportedModels[model["identifier"]]["name"] 
                modelInfo["accuracy"] = model["accuracy"]
                modelInfo["precision"] = model["precision"]
                modelInfo["recall"] = model["recall"]

                # Update accuracy and add model info to list
                accuracy += modelInfo["accuracy"]
                classifier["models"].append(modelInfo)

            # Count overal accuracy
            classifier["accuracy"] = accuracy / classifier["models"].__len__()

            # Add classifier into list
            validation.data.append(classifier)

        # Return validation
        return validation

    """ Fill features with data """
    def _fillFeatures(features, changes):
        sample = []
        # Load each feature from changes
        for feature in features:
            if feature in changes:
                sample.append(changes[feature])
            else:
                sample.append(0)

        # Return sample
        return sample

    """ Make prediction for patch file """
    def predictForPatchFile(project_id, patchFile):
        # Init validation
        validation = ValidationResult([]);

        # Decode patch file
        patchFileContent = patchFile.read()
        result = chardet.detect(patchFileContent)

        # Get changes of patch file
        changes = Parser.run(patchFileContent.decode(encoding=result['encoding'])).getVars()

        # Make prediction
        return ModelService.predict(project_id, changes)

    """ Make prediction for revision """
    def predictForRevision(project_id, revision):
        # Init validation
        validation = ValidationResult([]);

        # Load project
        projectValidation = ProjectService.getDetail(project_id);

        # Check project validation
        if not validation.append(projectValidation):
            return validation

        # Get changes of given revision
        submissionValidation = RepositoryService.getRevisionDifference(projectValidation.data["repository"], revision + "^", revision)

        # Check submission validation
        if not validation.append(submissionValidation):
            return validation        

        # Make prediction
        return ModelService.predict(project_id, submissionValidation.data)

    """ Predict which test cases are most likely to change """
    def predict(project_id, patch):
        # Init validation
        validation = ValidationResult([]);

        # We need one dimensional change analysis
        changes = ModelService._diffObjectToSample(patch)

        # And now load classifiers
        classifiers = ModelService._loadClassifiers("project_" + project_id)
        supportedModels = ModelService._getSupportedModels()

        # Iterate through classifiers
        for key in classifiers:
            # Map changes into values array
            X = ModelService._fillFeatures(classifiers[key]["features"], changes)

            # Prediction flag
            predictionFlag = False
            modelsInfo = list()

            # Make predictions for each model
            for model in classifiers[key]["models"]:
                modelInfo = dict()
                # Predict
                modelInfo["prediction"] = model["model"].predict([X])[0] 
                modelInfo["name"] =  supportedModels[model["identifier"]]["name"] 
                modelInfo["accuracy"] = model["accuracy"]
                modelInfo["precision"] = model["precision"]
                modelInfo["recall"] = model["recall"]
                
                # Add model to list
                modelsInfo.append(modelInfo)

                # Check prediction output
                if modelInfo["prediction"] is 1:
                    predictionFlag = True

            # We made predictions, if any was true, then add classifier to list
            if predictionFlag:
                validation.data.append(modelsInfo)

        # Return validation
        return validation

    """ Create model for project """
    def create(project_id):
        # Get detail about project
        validation = ProjectService.getDetail(project_id);

        # If getting detail failed, pass it
        if not validation.isValid:
            return validation;

        # Init tuple to hold data
        measurements = dict()

        # It went ok, so let us begin
        # We need to process each submission
        sortedSubmissions = sorted(validation.data["submissions"], key=lambda k: k['SequenceNumber'])
        for index, submission in enumerate(sortedSubmissions, start=0): 
            # Init api handler
            resultCloud = ResultCloud(config.RESULT_CLOUD_API)

            # Get submission with test cases from result cloud
            try:
                response  = resultCloud.get_submission_by_id(submission["Id"])   
            except:
                # Prepare validation and return result
                validation.addError("Failed to load submission from ResultCloud")
                return validation

            # Failed to get response
            if not response:
                # Prepare validation and return result
                validation.addError("Failed to load submission from ResultCloud")
                return validation
            
            # Assign result 
            rcSubmission = resultCloud.last_response['Result']

            # Get changes of submission
            if index < 1:
                # There is no previous submission
                submissionValidation = RepositoryService.getRevisionDifference(validation.data["repository"], submission["GitHash"] + "^", submission["GitHash"])
            else:
                submissionValidation = RepositoryService.getRevisionDifference(validation.data["repository"], sortedSubmissions[index-1]["GitHash"] , submission["GitHash"])

            # Check if validation is ok
            if not validation.append(submissionValidation):
                return validation

            # We have all we need
            for testCase in ModelService._extractTestCases(rcSubmission):
                # Update measurements
                measurements = ModelService._updateModelMeasurements(measurements, ntpath.basename(testCase["Name"]), submissionValidation.data, testCase["ChangeFlag"])

        # Calculate and save models
        classifiers = ModelService._calculate(measurements)
        ModelService._saveClassifiers(classifiers, "project_" + project_id)

        # Return validation
        return validation


