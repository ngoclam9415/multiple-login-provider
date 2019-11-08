from __future__ import print_function
from flask import redirect, render_template, Flask, Response, jsonify, request
from user_creator.user_creator_getter import UserCreatorGetter
import json
from utils.twitter_requester import get_request_token
import twitter

app = Flask(__name__)
userCreatorGetter = UserCreatorGetter()
storage = {}
verified = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=["POST"])
def register():
    data = request.get_json()
    # TODO IMPLEMENT INSERT USER HERE
    print(data)
    factory = userCreatorGetter.get_factory(data.get("provider"))
    flag = factory.create_user(**data)
    return jsonify(flag)

@app.route("/api/callback/<provider>")
def callback(provider):
    factory = userCreatorGetter.get_factory(provider)
    factory.process_and_save_access_token()
    return render_template("blank_page.html")


@app.route("/api/get_twitter_request_token")
def handle_tt_login():
    token_data = get_request_token()
    factory = userCreatorGetter.get_factory("twitter")
    factory.save_request_token(token_data["oauth_token"], token_data["oauth_token_secret"])
    return jsonify({"oauth_token" : token_data["oauth_token"]})




if __name__ == '__main__':
    # app.run('localhost', 5000, debug=True, ssl_context=('cert.pem', 'key.pem'))
    app.run('localhost', 5000, debug=True)