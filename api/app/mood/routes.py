from . import mood_bp
from app.models import Moods, MoodLogger
from app.database import db
import logging
from flask import Blueprint, jsonify, request
import os
from datetime import datetime

AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD')
log = logging.getLogger(__name__)
@mood_bp.route('/mood/fetch-latest', methods=['GET'])
def fetch_latest():
    log.info('Received a request :: %s', request)
    # if request.headers.get('Authorization') != f'Bearer {AUTH_PASSWORD}':
    #     return jsonify({
    #         "message": "UNAUTHORIZED"
    #     }), 401
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

@mood_bp.route('/mood/fetch-all-logs', methods=['GET'])
def fetch_all_logs():
    log.info('Received a request :: %s', request)
    # if request.headers.get('Authorization') != f'Bearer {AUTH_PASSWORD}':
    #     return jsonify({
    #         "message": "UNAUTHORIZED"
    #     }), 401
    try:
        all_moods = MoodLogger.query.order_by(MoodLogger.id.desc()).all()
        moods_list = [
            {
                'id': m.id,
                'mood_id': m.mood_id,
                'mood_name': m.mood.mood,  # Accessing the mood name through the relationship
                'timestamp': m.timestamp
            }
            for m in all_moods
        ]
        return jsonify(moods_list), 200
    except Exception as exception:
        log.exception(exception)
        return jsonify({
            "message": "INTERNAL_ERROR"
        }), 500

@mood_bp.route('/mood/log/<mood_id>', methods=['POST', 'GET'])
def log_mood(mood_id):
    log.info('Received a request :: %s', request)
    # if request.headers.get('Authorization') != f'Bearer {AUTH_PASSWORD}:
    #     return jsonify({
    #         "message": "UNAUTHORIZED"
    #     }), 401
    try:
        new_mood_log = MoodLogger(mood_id=mood_id, timestamp=datetime.now())
        db.session.add(new_mood_log)
        db.session.commit()
        return jsonify({
            "message": "MOOD_LOGGED"
        }), 200
    except Exception as exception:
        log.exception(exception)
        return jsonify({
            "message": "INTERNAL_ERROR"
        }), 500

@mood_bp.route('/mood/fetch-all', methods=['GET'])
def fetch_all():
    log.info('Received a request :: %s', request)
    # if request.headers.get('Authorization') != f'Bearer {AUTH_PASSWORD}':
    #     return jsonify({
    #         "message": "UNAUTHORIZED, password entered " + str(request.headers.get('Authorization')) + " " + str(AUTH_PASSWORD)
    #     }), 401
    try:
        all_moods = Moods.query.all()
        if request.headers.get('getHidden') == f'y':
            moods_list = [{'id': m.id, 'mood': m.mood, 'hide': m.hide} for m in all_moods]
            return jsonify(moods_list), 200
        else:
            moods_list = [{'id': m.id, 'mood': m.mood} for m in all_moods if not m.hide]
            return jsonify(moods_list), 200
    except Exception as exception:
        log.exception(exception)
        return jsonify({
            "message": "INTERNAL_ERROR"
        }), 500

@mood_bp.route('/mood/<mood>', methods=['GET'])
def add_mood(mood):
    # Check if the mood already exists
    existing_mood = Moods.query.filter_by(mood=mood).first()
    if not existing_mood:
        # Add the mood to the Moods table
        new_mood = Moods(mood=mood)
        db.session.add(new_mood)
        db.session.commit()
        existing_mood = new_mood
    else:
        if request.headers.get('Hide') == f'y':
            if not existing_mood.hide:
                existing_mood.hide = True
            db.session.commit()
            return jsonify({
                "message": "HIDDEN"
            }), 200
        if request.headers.get('Hide') == f'n':
            if existing_mood.hide:
                existing_mood.hide = False
            db.session.commit()
            return jsonify({
                "message": "UNHIDDEN"
            }), 200


    # Retrieve all moods
    all_moods = Moods.query.all()
    moods_list = [{'id': m.id, 'mood': m.mood} for m in all_moods if not m.hide]

    return jsonify(moods_list)