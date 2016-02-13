from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

# Initialize application
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from app import views, models, services

# Initialize resources
api.add_resource(services.ProjectsService, '/api/projects')
api.add_resource(services.ProjectService, '/api/projects/<project_id>')
