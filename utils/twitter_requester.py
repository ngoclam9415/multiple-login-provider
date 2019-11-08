import twitter
from requests_oauthlib import OAuth1Session
import tweepy
from utils.config import TwitterConfig as Config


def get_request_token():
    oauth_client = OAuth1Session(Config.consumer_key, client_secret=Config.consumer_secret, callback_uri=Config.CALLBACK_URL)
    resp = oauth_client.fetch_request_token(Config.REQUEST_TOKEN_URL)
    return resp

def get_access_token(oauth_token, oauth_token_secret, oauth_verifier):
    oauth_client = OAuth1Session(Config.consumer_key, client_secret=Config.consumer_secret,
                                 resource_owner_key=oauth_token,
                                 resource_owner_secret=oauth_token_secret,
                                 verifier=oauth_verifier)
    resp = oauth_client.fetch_access_token(Config.ACCESS_TOKEN_URL)
    return resp

if __name__ == "__main__":
    request = get_request_token(Config.consumer_key, Config.consumer_secret)
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