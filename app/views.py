from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/frame')
def frame():
    return render_template('frame.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/project_settings')
def project_settings():
    return render_template('project_settings.html')

@app.route('/project_board')
def project_board():
    return render_template('project_board.html')

@app.route('/project_model')
def project_model():
    return render_template('project_model.html')

@app.route('/project_git')
def project_git():
    return render_template('project_git.html')

@app.route('/project_git_commit')
def project_git_commit():
    return render_template('project_git_commit.html')

@app.route('/project_git_log')
def project_git_log():
    return render_template('project_git_log.html')

@app.route('/<path:dummy>')
def fallback(dummy):
    return render_template('index.html')