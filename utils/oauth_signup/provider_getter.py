from utils.oauth_signup.facebook_oauth_signup import FacebookSignUp

class ProviderGetter:
    # def __init__(self):
    #     self.facebook_oauth_signup = FacebookSignUp()
        
    @staticmethod
    def get_provider(provider):
        if provider == "facebook":
            return FacebookSignUp()
        # elif provider == "twitter":
        #     return self.twitter_factory
        # elif provider == "default":
        #     return self.default_factory