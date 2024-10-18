from app import db

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), index=True, unique=True)
    moduleCode = db.Column(db.Integer)
    deadline = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    status = db.Column(db.Boolean)