from . import db  # import from package __init__
from flask_login import UserMixin  # To help with the login
from sqlalchemy.sql import func  # used to get date and more?


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # allow alchemy self set date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Getting form class User.id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Foreign key for Notes
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  # This relations is for user to get all of their notes
