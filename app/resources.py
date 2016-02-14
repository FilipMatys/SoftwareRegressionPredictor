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

""" Git resource """
class GitResource(Resource):
    # Clone project repository
    def get(self, project_id):
        return jsonify(services.GitService.clone(project_id).getVars())

