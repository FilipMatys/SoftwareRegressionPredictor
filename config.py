import os
basedir = os.path.abspath(os.path.dirname(__file__))

REPOSITORIES = "C:\Repositories"
RESULT_CLOUD_API = "http://result-cloud.org/production/method/"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')