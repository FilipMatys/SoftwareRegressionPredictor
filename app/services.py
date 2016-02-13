from flask import jsonify, request
from flask.ext.restful import Api, Resource
from utils.ResultCloud import ResultCloud
from utils.ValidationResult import ValidationResult
from app import models
from app import db

""" Project service """
class ProjectService(Resource):
    # Get detail of project
    def get(self, project_id):
        # Load project from internal database
        project = models.Project.query.filter_by(id=project_id).first()

        # Check if project was found
        if not project:
            validation = ValidationResult(dict())
            validation.addError("Project not in internal database")

            return jsonify(validation.getVars())

        # Prepare validation and return result
        validation = ValidationResult(models.serialize(project))
        return jsonify(validation.getVars())

    # Delete project
    def delete(self, project_id):
        return jsonify({"data": "delete project"})

""" Projects service """
class ProjectsService(Resource):
    # Get list of projects
    def get(self):
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
                print(project)
                if not models.Project.query.filter_by(ext_id=project["Id"]).first():
                    new_project = models.Project(project["Id"], project["Name"], project["GitRepository"])
                    db.session.add(new_project)
                    db.session.commit()

            # Load internal projects
            internalProjects = models.Project.query.all()

            # Prepare validation and return result
            validation =  ValidationResult([models.serialize(project) for project in internalProjects])
            return jsonify(validation.getVars())


    # Save new project
    def post(self, project):
        return jsonify({"data": "save project"})


