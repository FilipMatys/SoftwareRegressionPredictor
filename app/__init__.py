from flask import Flask
from flask.ext.restful import Api
from app.api.ProjectsAPI import ProjectsAPI, ProjectAPI

# Initialize application
app = Flask(__name__)
api = Api(app)

# Initialize resources
api.add_resource(ProjectsAPI, '/api/projects')
api.add_resource(ProjectAPI, '/api/projects/<project_id>')

from app import views