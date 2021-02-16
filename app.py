
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(app=f'{app.__dict__}', bilal='testing')
