import json

import flask
from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/', methods=['GET'])
def __get__():  # put application's code here
    params = request.args
    return json.dumps(params)


@app.route('/', methods=['POST'])
def __post__():
    params = request.form
    return json.dumps(params)


if __name__ == "__main__":
    port = int(os.environ.get('Port', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
