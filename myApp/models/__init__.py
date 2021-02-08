import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    id = db.Column(db.String,primary_key=True,default=generate_uuid)
    username = db.Column(db.String,nullable=False,unique=True)
    email = db.Column(db.String,nullable=False,unique=True)
    

class Role(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String,nullable=False,unique=True)