from utils.ResultCloud import ResultCloud
from utils.GitWrap import GitWrap, CommitWrap
from utils.ValidationResult import ValidationResult
from plugins.clanguage.Parser import Parser
from app import models
from app import db
import config

class ProjectService(object):
    """ Get detail of project """
    def getDetail(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Check if project was found
        if not project:
            validation = ValidationResult(dict())
            validation.addError("Project not in internal database")

            return validation

        # Init result cloud api
        resultCloud = ResultCloud(config.RESULT_CLOUD_API)
        
        # Try to load project
        try:
            response = resultCloud.get_project(project.ext_id)
        except:
            # Prepare validation and return result
            validation = ValidationResult(models.serialize(project))
            return validation

        # Init result
        result = models.serialize(project)

        # If there was a response, get submissions
        if response:
            result["submissions"] = resultCloud.last_response['Result']['Submissions']

        # Prepare validation and return result
        validation = ValidationResult(result)
        return validation

    """ Save project """
    def save(project):
        db.session.add(project)
        db.session.commit()

    """ Get list of objects """
    def getList():
        # Init api handler
        resultCloud = ResultCloud(config.RESULT_CLOUD_API)

        # Try to load projects from result cloud
        try:
            response  = resultCloud.get_git_projects()   
        except:
            # Load internal projects
            internalProjects = models.Project.query.all()

            # Prepare validation and return result
            validation =  ValidationResult([models.serialize(project) for project in internalProjects])
            return validation
 
        # Check if the request was successful
        if not response:
            # Load failed
            validationResult = ValidationResult(dict())
            validationResult.addError("Failed to load projects from ResultCloud repository")

            # Return result
            return jsonify(validationResult.getVars())
        else:
            # Load was successful
            externalProjects = resultCloud.last_response['Result']

            # Merge new projects
            for project in externalProjects:
                if not models.Project.query.filter_by(ext_id=project["Id"]).first():
                    new_project = models.Project(project["Id"], project["Name"], project["GitRepository"])
                    self.save(new_project)

            # Load internal projects
            internalProjects = models.Project.query.all()

            # Prepare validation and return result
            validation =  ValidationResult([models.serialize(project) for project in internalProjects])
            return validation



