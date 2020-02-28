from flask import Flask, escape, request
from flask import json
# import urllib.request as request
from urllib2 import urlopen
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    url_base = os.environ['API_URL']
    number = request.args.get('number', default = 0, type = int)
    link = url_base + ":7000/?number="+str(number)
    response = urlopen(link)
    source = response.read()
    #data = json.loads(source)
    return source

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)