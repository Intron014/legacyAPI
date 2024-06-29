from flask import Blueprint

clipboard_bp = Blueprint('clipboard', __name__)

from . import routes
