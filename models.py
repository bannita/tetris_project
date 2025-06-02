from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    high_score = db.Column(db.Integer, default = 0)
    date_joined = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    scores = relationship("Score", backref="user")

class Score(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), unique = False, nullable = False)
    score = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Date, default = date.today, nullable = False)