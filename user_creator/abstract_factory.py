from abc import ABC, ABCMeta, abstractmethod
from utils.database import UserDatabase

class AbstractUserFactory(ABC):
    @abstractmethod
    def __init__(self):
        self._document_format = {"email" : None,
                                "password" : None,
                                "facebook_id" : None,
                                "twitter_id" : None,
                                "facebook_email" : None,
                                "twitter_email" : None,
                                "provider" : None}
        self.database = UserDatabase()

    @abstractmethod
    def create_user(self, **kwargs):
        pass

    @abstractmethod
    def _get_register_information(self, **kwargs):
        pass

    @abstractmethod
    def _verify_document(self, document):
        pass

    @abstractmethod
    def _register(self, document):
        pass

    @abstractmethod
    def process_and_save_access_token(self):
        pass

