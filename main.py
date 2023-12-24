from flask import Flask, jsonify, request
import requests
from Crypto.Cipher import DES
import binascii
import base64

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
                {'name': '451 - Home'},
                {'name': '436 - UPM'},
                {'name': '437 - Sierra de Guadalupe'},
                {'name': '440 - Villa de Vallecas'},
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
                {'id': '2074', 'bid': '436'},
                {'id': '2003', 'bid': '437'},
                {'id': '2053', 'bid': '440'},
                {'id': '2188', 'bid': '451'}
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
                {'id': '3950', 'name': 'Home'},
                {'id': '3847', 'name': 'Home Away'},
                {'id': '5562', 'name': 'UPM Down'},
                {'id': '3854', 'name': 'Metro Las Suertes'},
                {'id': '4112', 'name': 'CC La Gavia'},
                {'id': '2612', 'name': 'UPM Up Up'},
                {'id': '1027', 'name': 'Sierra de Guadalupe'},
                {'id': '0000', 'name': 'Others'}
            ]
        }
    ]
    return jsonify(jsonArray)


if __name__ == '__main__':
    app.run(debug=True)
