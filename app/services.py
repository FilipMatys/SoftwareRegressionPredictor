from utils.ResultCloud import ResultCloud
from utils.GitWrap import GitWrap, CommitWrap, DiffWrap
from utils.ValidationResult import ValidationResult
from app import models
from app import db
import config
import whatthepatch

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

class RepositoryService():
    """ Clone repository """
    def clone(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)

        # Clone
        #gitWrap.clone()

        # Init validation
        return ValidationResult(dict())

    """ Check if repository exists """
    def exists(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)
        result = { "exists" : gitWrap.init() }

        # Init validation
        return ValidationResult(result)

    """ Load commits of projects repository """
    def log(project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)
        gitWrap.init()

        return ValidationResult([CommitWrap(n).getVars() for n in gitWrap.log(10)])
        

    def getCommit(project_id, hash):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)
        gitWrap.init()

        # Load commit
        commit = gitWrap.get_commit(hash)
        commitWrap = CommitWrap(commit)

        # Get commit changes
        commitWrap.diff = [DiffWrap(diff).getVars() for diff in whatthepatch.parse_patch(gitWrap.get_commit_diff(hash))] 
       
        # Return result
        return ValidationResult(commitWrap.getVars())