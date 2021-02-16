
# A very simple Flask Hello World app for you to get started with...

import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify( bilal='testing', envs=dict(os.environ))
