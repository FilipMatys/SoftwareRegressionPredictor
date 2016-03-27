from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

# Initialize application
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from app import views, models, resources

# Initialize resources
api.add_resource(resources.ProjectsResource, '/api/projects')
api.add_resource(resources.ProjectResource, '/api/projects/<project_id>')
api.add_resource(resources.RepositoryCloneResource, '/api/repository/<project_id>/clone')
api.add_resource(resources.RepositoryExistsResource, '/api/repository/<project_id>/exists')
api.add_resource(resources.RepositoryLogResource, '/api/repository/<project_id>/log/<number>')
api.add_resource(resources.RepositoryCommitResource, '/api/repository/<project_id>/commit/<hash>')
api.add_resource(resources.ModelCreationResource, '/api/model/<project_id>/create')
api.add_resource(resources.ModelLoadResource, '/api/model/<project_id>/load')
