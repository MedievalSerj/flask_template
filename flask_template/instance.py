from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'msg': 'welcome to flask_template API v1'
    })
