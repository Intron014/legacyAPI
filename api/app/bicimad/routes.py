from flask import jsonify, request, current_app
from . import bicimad_bp
from Crypto.Cipher import DES
import binascii
import base64

encodedAccessKey = "OGZmNTI3ZjktZjg1Yi00NWVmLWIxYjItYmQ5ZWI1OWUwZmZm"
encodedBikeKey = "QklLRTIwMTk="

@bicimad_bp.route('/emt-bicimad', methods=['GET'])
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

@bicimad_bp.route('/emt-bicimad-rel', methods=['GET'])
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

@bicimad_bp.route('/emt-bus', methods=['GET'])
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

@bicimad_bp.route('/bicimad-gethashcode', methods=['POST'])
def process_bike_data():
    data = request.get_json()
    decoded_access_key, decoded_bike_key = decode_keys()

    first_cipher_str = generate_first_cipher_string(data)
    second_cipher_str = generate_second_cipher_string(first_cipher_str, decoded_bike_key)

    hash_code, cipher_error = ecb_encrypt_base64(second_cipher_str.encode(), decoded_access_key.encode())

    if cipher_error:
        current_app.logger.error(f"Error: {cipher_error}")
        return "", 500

    current_app.logger.info(f"{'-' * (len(second_cipher_str + '- secondCipherStr: '))}")
    current_app.logger.info(f"- d1: {data['D1']}")
    current_app.logger.info(f"- d2: {data['D2']}")
    current_app.logger.info(f"- bikeNumber: {data['BikeNumber']}")
    current_app.logger.info(f"- docker: {data['Docker']}")
    current_app.logger.info(f"- firstCipherStr: {first_cipher_str}")
    current_app.logger.info(f"- secondCipherStr: {second_cipher_str}")
    current_app.logger.info(f"{'-' * (len(second_cipher_str + '- secondCipherStr: '))}")
    return hash_code.decode(), 200

def decode_keys():
    decoded_access_key = base64.b64decode(encodedAccessKey).decode().upper()[:8]
    decoded_bike_key = base64.b64decode(encodedBikeKey).decode()

    return decoded_access_key, decoded_bike_key

def generate_first_cipher_string(data):
    d1, d2 = resize_coordinates(data['D1'], data['D2'])
    first_cipher_str = f"{data['BikeNumber']}#{data['Docker']}#{d1}#{d2}#D#{data['DNI']}"

    if len(first_cipher_str) % 8 != 0:
        length = 8 - (len(first_cipher_str) % 8)
        first_cipher_str += '#' * length

    return first_cipher_str

def resize_coordinates(d1, d2):
    current_app.logger.info(f"Resizing coordinates: {d1}, {d2}")
    d1 = str(d1)[:10] if len(str(d1)) >= 10 else str(d1).ljust(10, '0')
    d2 = str(d2)[:10] if len(str(d2)) >= 10 else str(d2).ljust(10, '0')
    return d1, d2

def generate_second_cipher_string(first_cipher_str, decoded_bike_key):
    ciphered_string, cipher_error = ecb_encrypt_hex(first_cipher_str.encode(), decoded_bike_key.encode())

    if cipher_error:
        current_app.logger.error(f"Error: {cipher_error}")
        return "", 500

    second_cipher_str = f"B{ciphered_string}"

    if len(second_cipher_str) % 8 != 0:
        length = 8 - (len(second_cipher_str) % 8)
        second_cipher_str += 'Z' * length

    return second_cipher_str

def ecb_encrypt_hex(src, key):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted = cipher.encrypt(src)
        return binascii.hexlify(encrypted).decode().upper(), None
    except Exception as e:
        current_app.logger.error(f"Error: {e}")
        return None, e

def ecb_encrypt_base64(src, key):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted = cipher.encrypt(src)
        return base64.b64encode(encrypted), None
    except Exception as e:
        current_app.logger.error(f"Error: {e}")
        return None, e
