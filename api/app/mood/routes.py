from . import mood_bp
from app.models import Moods, MoodLogger
from app.database import db
import logging
from flask import Blueprint, jsonify, request
import os

log = logging.getLogger(__name__)
@mood_bp.route('/mood/fetch-latest', methods=['GET'])
def fetch_latest():
    AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD')
    log.info('Received a request :: %s', request)
    if request.headers.get('Authorization') != f'Bearer {AUTH_PASSWORD}':
        return jsonify({
            "message": "UNAUTHORIZED"
        }), 401
    try:
        mood = Moods.query.order_by(Moods.id.desc()).first()
        if not mood:
            return jsonify({
                "message": "NO_MOODS_FOUND"
            }), 200
        return jsonify({
            "mood": mood.mood
        }), 200
    except Exception as exception:
        log.exception(exception)
        return jsonify({
            "message": "INTERNAL_ERROR"
        }), 500

@mood_bp.route('/salsa/<mood>', methods=['GET'])
def add_mood(mood):
    # Check if the mood already exists
    existing_mood = Moods.query.filter_by(mood=mood).first()
    if not existing_mood:
        # Add the mood to the Moods table
        new_mood = Moods(mood=mood)
        db.session.add(new_mood)
        db.session.commit()
        existing_mood = new_mood

    # Log the mood
    mood_log = MoodLogger(mood_id=existing_mood.id)
    db.session.add(mood_log)
    db.session.commit()

    # Retrieve all moods
    all_moods = Moods.query.all()
    moods_list = [{'id': m.id, 'mood': m.mood} for m in all_moods]

    return jsonify(moods_list)