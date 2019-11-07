import twitter
from requests_oauthlib import OAuth1Session
import tweepy
consumer_key="WNns8HLyN0ktie3efgZQrgusv"
consumer_secret="IodoMDsdVXOspXD734KAKC1rNXTIArZftGLXvPjoCTv7jbnVuM"
# access_token_key="798707958280425472-YQ76CxPBh60T4EzUg7ecSsaE5jKNZwa"
# access_token_secret="1Xvy7pOaqnDacFdimIgpdQCmG7vXIXQk9KPZj9RkqowT1"
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


def get_request_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='https://16eac7cd.ngrok.io/api/twitter_callback')
    resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    return resp

def get_access_token(oauth_token, oauth_token_secret, oauth_verifier):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=oauth_token,
                                 resource_owner_secret=oauth_token_secret,
                                 verifier=oauth_verifier)
    resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    return resp

if __name__ == "__main__":
    request = get_request_token(consumer_key, consumer_secret)
    print(request)
    # # get_access_token("YTq7pwAAAAABAwwdAAABbj8WKhk", "ZPeF6Q0UzwdTCaFCQPSR64GCO2hQMkUk", "RSJDRRA0O7PL4mn4wYYBDUXubnTO3bxK")
    # api = twitter.Api(consumer_key=consumer_key,
    #                     consumer_secret=consumer_secret,
    #                     access_token_key=access_token_key,
    #                     access_token_secret=access_token_secret)
    # user = api.VerifyCredentials(include_email=True)
    # print(user)
    
    # # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # # auth.set_access_token(access_token_key, access_token_secret)
    # # api = tweepy.API(auth)
    # # api.ve
    # # user = api.get_user(screen_name="ngoclam9412")
    # # print(user)