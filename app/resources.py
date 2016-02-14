from flask import jsonify, request
from flask.ext.restful import Api, Resource
from app import services

""" Project resource """
class ProjectResource(Resource):
    # Get detail of project
    def get(self, project_id):
        return jsonify(services.ProjectService.getDetail(project_id).getVars())

""" Projects resource """
class ProjectsResource(Resource):
    # Get list of projects
    def get(self):
            return jsonify(services.ProjectService.getList().getVars())

""" Repository clone resource """
class RepositoryCloneResource(Resource):
    # Clone project repository
    def get(self, project_id):
        return jsonify(services.RepositoryService.clone(project_id).getVars())

""" Repository exists resource """
class RepositoryExistsResource(Resource):
    def get(self, project_id):
        return jsonify(services.RepositoryService.exists(project_id).getVars())

""" Repository log resource """
class RepositoryLogResource(Resource):
    def get(self, project_id):
        return jsonify(services.RepositoryService.log(project_id).getVars())

""" Repository commit resource """
class RepositoryCommitResource(Resource):
    def get(self, project_id, hash):
        return jsonify(services.RepositoryService.getCommit(project_id, hash).getVars())      

