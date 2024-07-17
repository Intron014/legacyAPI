from app.database import db
from datetime import datetime

class Moods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mood = db.Column(db.String(200), nullable=False)

class MoodLogger(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mood_id = db.Column(db.Integer, db.ForeignKey('moods.id'), nullable=False, autoincrement=True)
    mood = db.relationship('Moods', backref=db.backref('moodlog', lazy=True))
