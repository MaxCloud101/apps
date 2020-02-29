from flask import Flask, escape, request
from flask import json
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    number = request.args.get('number', default = 0, type = int)
    data = {"reponse": number*2}
    return json.dumps(data)


if __name__ == '__main__':
    logging.basicConfig(filename='/home/ubuntu/logging.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=7000)
