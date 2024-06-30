
from . import lastfm_bp

import logging
import os

import requests

from flask import jsonify, request

log = logging.getLogger(__name__)
BASE_URL = 'https://ws.audioscrobbler.com/2.0/'
RECENT_TRACKS_PARAMS = 'method=user.getrecenttracks&limit=1&format=json'
TIMEOUT = 10


@lastfm_bp.route('/<user>/latest-song', methods=['GET'])
def latest_song(user):
    log.info('Received a request :: %s', request)
    api_key = os.environ.get('LASTFM_API_KEY')
    api_url = f"{BASE_URL}?{RECENT_TRACKS_PARAMS}&user={user}&api_key={api_key}"
    if not api_key:
        log.error('Last.fm API key is not set')
        return jsonify({
            "message": "INTERNAL_ERROR"
        }), 500
    try:
        req = requests.get(api_url, timeout=TIMEOUT)
        lastfm_response = req.json()
        try:
            track = lastfm_response['recenttracks']['track'][0]

        except IndexError:
            return jsonify({
                'message': 'NO_TRACKS_FOUND'
            }), 200
        try:
            isplaying = track['@attr']['nowplaying']
        except KeyError:
            isplaying = 'false'
        if request.args.get('format') == 'shields.io':
            song = track['name']
            artist = track['artist']['#text']
            include_artist = request.args.get('artist', 'y').lower() != 'n'
            message = f"{song} - {artist}" if include_artist else song
            return jsonify({
                'schemaVersion': 1,
                'label': 'Listening to' if isplaying == 'true' else 'Last Played',
                'message': message,
            }), 200
        return jsonify({
            'track': track
        }), req.status_code
    except Exception as exception:
        log.exception(exception)
        return jsonify({
            'message': 'INTERNAL_ERROR'
        }), 500
