import logging
from flask import Flask
from app.bicimad.routes import bicimad_bp
from app.clipboard.routes import clipboard_bp

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

app.register_blueprint(bicimad_bp)
app.register_blueprint(clipboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
