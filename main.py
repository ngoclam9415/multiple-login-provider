from __future__ import print_function
from flask import redirect, render_template, Flask, Response, jsonify, request
from user_creator.facebook_factory import FacebookUserFactory
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=["POST"])
def register():
    data = request.get_json()
    # TODO IMPLEMENT INSERT USER HERE
    return jsonify(True)

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True, ssl_context=('cert.pem', 'key.pem'))
    # app.run('localhost', 5000, debug=True)