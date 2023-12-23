from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/modify-clipboard-link', methods=['POST'])
def modify_clipboard_link():
    data = request.json
    if 'link' in data:
        link = data['link']
        modified_link = link.replace('?forcedownload=1', '?forcedownload=0')
        return jsonify({'modified_link': modified_link})
    else:
        return jsonify({'error': 'Invalid request'}), 400


# Route - emt-bicimad
@app.route('/emt-bicimad', methods=['GET'])
def get_emt_bicimad():
    jsonArray = [
        {
            'data': [
                {'name': '000 - Other'}
            ]
        }
    ]
    return jsonify(jsonArray)


# Route - emt-bicimad-rel
@app.route('/emt-bicimad-rel', methods=['GET'])
def get_emt_bicimad_rel():
    jsonArray = [
        {
            'data': [
            ]
        }
    ]
    return jsonify(jsonArray)


# Route - emt-bus
@app.route('/emt-bus', methods=['GET'])
def get_emt_bus():
    jsonArray = [
        {
            'data': [
                {'id': '0000', 'name': 'Others'}
            ]
        }
    ]
    return jsonify(jsonArray)


if __name__ == '__main__':
    app.run(debug=True)
