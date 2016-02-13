from app import db
from sqlalchemy.orm import class_mapper

def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]
    # then we return their values in a dict
    return dict((c, getattr(model, c)) for c in columns)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ext_id = db.Column(db.Integer)
    name = db.Column(db.String(128), unique=True)
    repository = db.Column(db.String(521))

    def __init__(self, ext_id, name, repository):
        self.ext_id = ext_id
        self.name = name
        self.repository = repository