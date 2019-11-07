from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session
from utils.config import provider_config

class OAuthSignUp(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        config = provider_config[self.provider_name]
        self.consumer_id = config.id
        self.consumer_secret = config.secret

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('callback',
                       _external=True).replace("http", "https")

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            print(self.__subclasses__())
            for provider_class in self.__subclasses__():
                provider = provider_class()
                print(provider.provider_name)
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


    