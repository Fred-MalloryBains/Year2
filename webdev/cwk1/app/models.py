from app import db

#definition of the database model for the assessments
class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, unique=True)
    moduleCode = db.Column(db.String(50),)
    deadline = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    status = db.Column(db.Boolean)