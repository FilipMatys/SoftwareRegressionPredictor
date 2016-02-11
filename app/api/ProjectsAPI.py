from flask import jsonify, request
from flask.ext.restful import Api, Resource

class ProjectAPI(Resource):
    def get(self, project_id):
        return jsonify({"data": "get project"})

    def delete(self, project_id):
        return jsonify({"data": "delete project"})

class ProjectsAPI(Resource):
    def get(self):
        return jsonify({"data": "get list of projects"})

    def post(self, project):
        return jsonify({"data": "save project"})


