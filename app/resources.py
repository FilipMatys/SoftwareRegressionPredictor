from flask import jsonify, request
from flask.ext.restful import Api, Resource
from app.services.ProjectService import ProjectService
from app.services.RepositoryService import RepositoryService

""" Project resource """
class ProjectResource(Resource):
    # Get detail of project
    def get(self, project_id):
        return jsonify(ProjectService.getDetail(project_id).getVars())

""" Projects resource """
class ProjectsResource(Resource):
    # Get list of projects
    def get(self):
            return jsonify(ProjectService.getList().getVars())

""" Repository clone resource """
class RepositoryCloneResource(Resource):
    # Clone project repository
    def get(self, project_id):
        return jsonify(RepositoryService.clone(project_id).getVars())

""" Repository exists resource """
class RepositoryExistsResource(Resource):
    def get(self, project_id):
        return jsonify(RepositoryService.exists(project_id).getVars())

""" Repository log resource """
class RepositoryLogResource(Resource):
    def get(self, project_id):
        return jsonify(RepositoryService.log(project_id).getVars())

""" Repository commit resource """
class RepositoryCommitResource(Resource):
    def get(self, project_id, hash):
        return jsonify(RepositoryService.getCommit(project_id, hash).getVars())      

