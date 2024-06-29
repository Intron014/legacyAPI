from flask import Blueprint

bicimad_bp = Blueprint('bicimad', __name__)

from . import routes
