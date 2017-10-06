from flask import Flask, request
import json
import scanfaces

try:
    from urllib.parse import parse_qs
except ImportError:
     from urlparse import parse_qs

app = Flask(__name__, static_url_path='')

@app.route('/recognize', methods=['POST'])
def recognize():
   if request.method == 'POST':
       image_base64 = request.json['image']
       print(image_base64)
       scanfaces.get_info(image_base64, '/home/hkayaroh/attendance/res')
       return "true", 200
   else:
       return "false", 417

if __name__ == "__main__":
    app.run()
