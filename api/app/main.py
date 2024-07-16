import logging
from flask import Flask, redirect
from app.bicimad.routes import bicimad_bp
from app.clipboard.routes import clipboard_bp
from app.lastfm.routes import lastfm_bp
from app.mood.routes import mood_bp
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ledb.db'

db = SQLAlchemy(app)

class Moods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(200), nullable=False)

class MoodLogger(db.Model):
    timestamp = db.Column(db.DateTime, primary_key=True)
    mood_id = db.Column(db.Integer, db.ForeignKey('moods.id'), nullable=False)
    mood = db.relationship('Moods', backref=db.backref('moodlog', lazy=True))

app.app_context().push()
db.create_all()


LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
              "-30s %(funcName) -35s %(lineno) -5d: %(message)s")
logging.basicConfig(level=os.environ.get(
    'LOG_LEVEL', 'INFO'), format=LOG_FORMAT)

app.register_blueprint(bicimad_bp)
app.register_blueprint(clipboard_bp)
app.register_blueprint(lastfm_bp)
app.register_blueprint(mood_bp)

@app.route('/<path:path>')
def catch_all(path):
    return redirect("https://intron014.com/404api", code=302)
@app.route('/')
def root():
    return redirect("https://intron014.com/404api", code=302)
