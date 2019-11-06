from user_creator.abstract_factory import AbstractUserFactory
import requests

class TwitterUserFactory(AbstractUserFactory):
    def __init__(self):
        super().__init__()

    def create_user(self, **kwargs):
        document = self._get_register_information(**kwargs)
        return self._register(document)

    def _get_register_information(self, **kwargs):
        email = kwargs.get("email", None)
        password = kwargs.get("password", None)
        if email is None :
            return None
        document = self._generate_document(email, password)
        return document

    def get_request_token_secret(self, oauth_token):
        return self.authenticate_info[oauth_token]["oauth_token_secret"]

    def _verify_document(self, document):
        return self.database.verify_default_document(document)

    def _register(self, document):
        if (self._verify_document(document)):
            self.database.insert_user(document)
            return True
        return False

    def _generate_document(self, email, password):
        document = self._document_format.copy()
        document["email"] = email
        document["password"] = password
        document["provider"] = "default"
        return document


if __name__ == '__main__':
    pass
