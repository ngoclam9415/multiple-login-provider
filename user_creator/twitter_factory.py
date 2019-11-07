from user_creator.abstract_factory import AbstractUserFactory
import requests
import twitter
from utils.config import TwitterConfig as Config

class TwitterUserFactory(AbstractUserFactory):
    def __init__(self):
        super().__init__()
        self.authenticate_info = {}
        self.consumer_key = Config.consumer_key
        self.consumer_secret = Config.consumer_secret

    def create_user(self, **kwargs):
        document = self._get_register_information(**kwargs)
        return self._register(document)

    def _get_register_information(self, **kwargs):
        tt_oauth_token = kwargs.get("oauth_token", None)
        # TODO Implement
        if tt_oauth_token is None :
            return None
        tt_id, tt_email = self._get_twitter_information(tt_oauth_token)
        if tt_id is None:
            return None
        document = self._generate_document(tt_id, tt_email)
        return document
            
    def save_request_token(self, oauth_token, oauth_token_secret):
        self.authenticate_info[oauth_token] = {"oauth_token_secret" : oauth_token_secret}
        self.authenticate_info[oauth_token]["is_verified"] = False

    def save_access_token(self, oauth_token, access_token_key, access_token_secret):
        self.authenticate_info[oauth_token]["access_token_key"] = access_token_key
        self.authenticate_info[oauth_token]["access_token_secret"] = access_token_secret
        if access_token_key is not None:
            self.authenticate_info[oauth_token]["is_verified"] = True

    def get_request_token_secret(self, oauth_token):
        return self.authenticate_info[oauth_token]["oauth_token_secret"]

    def _verify_document(self, document):
        return self.database.verify_tt_document(document)

    def _register(self, document):
        if document is None:
            return False
        if (self._verify_document(document)):
            self.database.insert_user(document)
            return True
        return False

    def _generate_document(self, tt_id, tt_email):
        document = self._document_format.copy()
        document["email"] = tt_email
        document["twitter_email"] = tt_email
        document["twitter_id"] = tt_id
        document["provider"] = "twitter"
        return document

    def _get_twitter_information(self, oauth_token):
        try:
            api = twitter.Api(consumer_key=self.consumer_key,
                            consumer_secret=self.consumer_secret,
                            access_token_key=self.authenticate_info[oauth_token]["access_token_key"],
                            access_token_secret=self.authenticate_info[oauth_token]["access_token_secret"])
            user = api.VerifyCredentials(include_email=True)
            user = user.AsDict()
            return user["id"], user["email"]
        except:
            return None, None

if __name__ == '__main__':
    pass
