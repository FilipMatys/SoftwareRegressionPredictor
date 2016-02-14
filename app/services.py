from utils.ResultCloud import ResultCloud
from utils.GitWrap import GitWrap
from utils.ValidationResult import ValidationResult
from app import models
from app import db
import config

class ProjectService():
    """ Get detail of project """
    def getDetail(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Check if project was found
        if not project:
            validation = ValidationResult(dict())
            validation.addError("Project not in internal database")

            return jsonify(validation.getVars())

        # Prepare validation and return result
        validation = ValidationResult(models.serialize(project))
        return validation

    """ Save project """
    def save(project):
        db.session.add(project)
        db.session.commit()

    """ Get list of objects """
    def getList():
        # Init api handler
        resultCloud = ResultCloud("http://result-cloud.org/production/method/")

        # Load projects from ResultCloud
        if not resultCloud.get_git_projects():
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

class GitService():
    def clone(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)

        # Clone
        gitWrap.clone()

        # Init validation
        return ValidationResult(dict())
        