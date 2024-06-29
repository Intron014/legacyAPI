from flask import jsonify, request, Blueprint, redirect
import logging
from . import clipboard_bp

log = logging.getLogger(__name__)

@clipboard_bp.route('/')
def root():
    log.info('Received a request :: %s', request)
    return redirect("https://intron014.com/404api", code=302)

@clipboard_bp.route('/modify-clipboard-link', methods=['POST'])
def modify_clipboard_link():
    log.info('Received a request :: %s', request)
    data = request.json
    if 'link' in data:
        link = data['link']
        modified_link = link.replace('?forcedownload=1', '?forcedownload=0')
        return jsonify({'modified_link': modified_link})
    else:
        return jsonify({'error': 'Invalid request'}), 400
