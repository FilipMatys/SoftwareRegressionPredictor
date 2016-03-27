from utils.ResultCloud import ResultCloud
from utils.ValidationResult import ValidationResult
from app.services.ProjectService import ProjectService
from app.services.RepositoryService import RepositoryService
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from app import models
from app import db
import config
import ntpath

class ModelService(object):
    """ Update measurements of model """
    def _updateModelMeasurements(measurements, testCaseName, sample, response):
        # If the model exists, update it
        if not testCaseName in measurements:
            measurements[testCaseName] = ([], [])

        # Update model measurements
        measurements[testCaseName] = ModelService._updateSamplesFeatures(measurements[testCaseName], sample, response)
        return measurements

    """ Create model for each test case """
    def _calculate(measurements):
        # Initialize classifiers
        classifiers = dict()

        # Create classifier for each model
        for key in measurements:
            # Initialize model
            classifiers[key] = { "model": GaussianNB(), "features": [] }
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
            
            # Fit the model
            classifiers[key]["model"].fit(X_train, y_train)

            # Test the model
            pred = classifiers[key]["model"].predict(X_test)
            classifiers[key]["accuracy"] = metrics.accuracy_score(y_test, pred)

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

    """ Load model of project """
    def load(project_id):
        # Load classifiers from file
        classifiers = ModelService._loadClassifiers("project_" + project_id)

        # Init validation with result data
        validation = ValidationResult([])

        # Iterate through classifiers and create user friendly output
        for key in classifiers:
            # Init model object and fill it
            model = dict()
            model["name"] = key
            model["features"] = classifiers[key]["features"]
            model["accuracy"] = classifiers[key]["accuracy"]
            validation.data.append(model)

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
                response  = resultCloud.get_submission_by_hash(submission["GitHash"])   
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


