import os
basedir = os.path.abspath(os.path.dirname(__file__))

REPOSITORIES = "C:\Repositories"
POLLING_KEY = "state"
CLASSIFIERS = os.path.join(basedir, 'classifiers')
RESULT_CLOUD_API = "http://localhost/method/"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')