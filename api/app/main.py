import logging
from flask import Flask
from app.bicimad.routes import bicimad_bp
from app.clipboard.routes import clipboard_bp
from app.lastfm.routes import lastfm_bp

import os

app = Flask(__name__)

LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
              "-30s %(funcName) -35s %(lineno) -5d: %(message)s")
logging.basicConfig(level=os.environ.get(
    'LOG_LEVEL', 'INFO'), format=LOG_FORMAT)

app.register_blueprint(bicimad_bp)
app.register_blueprint(clipboard_bp)
app.register_blueprint(lastfm_bp)

