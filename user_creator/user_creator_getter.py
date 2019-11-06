from user_creator.facebook_factory import FacebookUserFactory
from user_creator.twitter_factory import TwitterUserFactory
from user_creator.default_factory import DefaultUserFactory

class UserCreatorGetter:
    def __init__(self):
        self.facebook_factory = FacebookUserFactory()
        self.twitter_factory = TwitterUserFactory()

    def get_factory(self, provider):
        if provider == "facebook":
            return self.facebook_factory
        elif provider == "twitter":
            return self.twitter_factory
        elif provider == "default":
            return self.default_factory