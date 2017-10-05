from flask import Flask, request
import json
try:
    from urllib.parse import parse_qs
except ImportError:
     from urlparse import parse_qs

app = Flask(__name__, static_url_path='')

@app.route('/recognize', methods=['POST'])
def recognize():
   # print(parse_qs((request.get_data())))
   if request.method == 'POST':
       return "true", 200
   else:
       return "false", 417

if __name__ == "__main__":
    app.run()
