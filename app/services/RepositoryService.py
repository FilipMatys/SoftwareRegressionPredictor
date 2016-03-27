from utils.ResultCloud import ResultCloud
from utils.GitWrap import GitWrap, CommitWrap
from utils.ValidationResult import ValidationResult
from plugins.clanguage.Parser import Parser
from app import models
from app import db
import config

class RepositoryService(object):
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
    def log(project_id, number):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Init git wrap
        gitWrap = GitWrap(project.repository, config.REPOSITORIES)
        gitWrap.init()

        return ValidationResult([CommitWrap(n).getVars() for n in gitWrap.log(number)])
        
    """ Get revision information by project """
    def getCommitByProject(project_id, revision):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Get commit and changes within a result      
        return RepositoryService.getCommitByRepository(project.repository, revision + "^" ,revision)

    def getCommitByRepository(repository, prevRevision, revision):
        # Init git wrap
        gitWrap = GitWrap(repository, config.REPOSITORIES)
        gitWrap.init()

        # Load commit
        commit = gitWrap.get_commit(revision)
        commitWrap = CommitWrap(commit)

        # Get commit changes
        commitWrap.diff = RepositoryService.getRevisionDifference(repository, prevRevision, revision).data; 
       
        # Return result
        return ValidationResult(commitWrap.getVars())

    """ Get difference of two revisions """
    def getRevisionDifference(repository, prevRevision, revision):
        # Init git wrap
        gitWrap = GitWrap(repository, config.REPOSITORIES)
        gitWrap.init()
        
        # Get commit changes
        parser = Parser(gitWrap, prevRevision, revision)
        return ValidationResult(parser.run().getVars())