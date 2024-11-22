from app import db
from flask_sqlalchemy import SQLAlchemy


class Users (db.models):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(50))
    spotify_connected = db.Column(db.Boolean, default=False)
    spotify_access_token = db.Column(db.String(400), nullable = True)
    spotify_refresh_token = db.Column(db.String(400), nullable = True)
    
    def __repr__(self):
            return '{}{}{}'.format(self.id, self.name, self.contact_number)

