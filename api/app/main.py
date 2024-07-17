import logging
from flask import Flask, redirect, jsonify, request
from app.bicimad.routes import bicimad_bp
from app.clipboard.routes import clipboard_bp
from app.lastfm.routes import lastfm_bp
from app.mood.routes import mood_bp
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ledb.db'

from app.database import db
db.init_app(app)


LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
              "-30s %(funcName) -35s %(lineno) -5d: %(message)s")
logging.basicConfig(level=os.environ.get(
    'LOG_LEVEL', 'INFO'), format=LOG_FORMAT)
log = logging.getLogger(__name__)
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


if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)