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
api.add_resource(resources.GitResource, '/api/git/<project_id>')
