from flask import Blueprint

lastfm_bp = Blueprint('lastfm', __name__)

from . import routes
