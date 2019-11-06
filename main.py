from __future__ import print_function
from flask import redirect, render_template, Flask, Response, jsonify, request
from user_creator.user_creator_getter import UserCreatorGetter
import json
from utils.twitter_requester import *
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

@app.route("/api/twitter_callback")
def callback():
    data = request.values
    oauth_token = data.get("oauth_token")
    oauth_verifier = data.get("oauth_verifier", None)
    factory = userCreatorGetter.get_factory("twitter")
    if oauth_verifier is not None:
        oauth_token_secret = factory.get_request_token_secret(oauth_token)
        resp = get_access_token(oauth_token, oauth_token_secret, oauth_verifier)
        factory.save_access_token(oauth_token ,resp.get("oauth_token", None), resp.get("oauth_token_secret", None))
    return render_template("blank_page.html")

# @app.route("/api/verify_twitter_oath")
# def verify_twitter_oath():
#     pass

@app.route("/api/get_twitter_request_token")
def handle_tt_login():
    token_data = get_request_token(consumer_key, consumer_secret)
    factory = userCreatorGetter.get_factory("twitter")
    factory.save_request_token(token_data["oauth_token"], token_data["oauth_token_secret"])
    return jsonify({"oauth_token" : token_data["oauth_token"]})




if __name__ == '__main__':
    app.run('localhost', 5000, debug=True, ssl_context=('cert.pem', 'key.pem'))
    # app.run('localhost', 5000, debug=True)