from flask import jsonify, request
from flask.ext.restful import Api, Resource
from app.services.ProjectService import ProjectService
from app.services.RepositoryService import RepositoryService
from app.services.ModelService import ModelService

""" Model prediction resource """
class ModelPredictionResource(Resource):
    # Make prediction for revision
    def get(self, project_id, revision):
        return jsonify(ModelService.predictForRevision(project_id, revision).getVars())

    # Make prediction for file
    def post(self, project_id, revision):
        return jsonify(ModelService.predictForPatchFile(project_id, request.files["file"]).getVars())

""" Model exists resource """
class ModelExistsResource(Resource):
    # Check if model exists
    def get(self, project_id):
        return jsonify(ModelService.exists(project_id).getVars())

""" Model creation resource """
class ModelCreationResource(Resource):
    # Create model
    def get(self, project_id):
        return jsonify(ModelService.create(project_id).getVars());

""" Model load resource """
class ModelLoadResource(Resource):
    # Load model
    def get(self, project_id):
        return jsonify(ModelService.load(project_id).getVars());

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
    def get(self, project_id, number):
        return jsonify(RepositoryService.log(project_id, number).getVars())

""" Repository commit resource """
class RepositoryCommitResource(Resource):
    def get(self, project_id, hash):
        return jsonify(RepositoryService.getCommitByProject(project_id, hash).getVars())      

