from flask import Flask, request
import json
import scanfaces
from flask.json import jsonify
from flask_sslify import SSLify

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

app = Flask(__name__, static_url_path='')

@app.route('/recognize', methods=['POST'])
def recognize():
   if request.method == 'POST':
       image_base64 = request.json['image']
       info = scanfaces.get_info(image_base64)
       return jsonify(info), 200
   else:
       return "METHOD NOT FOUND", 417

@app.route('/status', methods=['GET'])
def status():
   print('coming in')
   return 'Yes, The service is up'

if __name__ == "__main__":
    app.run()
