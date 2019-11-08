from user_creator.abstract_factory import AbstractUserFactory
import requests
import bcrypt
import re

class DefaultUserFactory(AbstractUserFactory):
    def __init__(self):
        super().__init__()

    def create_user(self, **kwargs):
        document = self._get_register_information(**kwargs)
        return self._register(document)

    def _get_register_information(self, **kwargs):
        email = kwargs.get("email", None)
        password = kwargs.get("password", None)
        if email is None or not self.verify_email(email) or not self.verify_password(password):
            return None
        document = self._generate_document(email, password)
        return document

    def verify_email(self, email):
        pattern = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        if re.match(pattern, email):
            return True
        return False

    def verify_password(self, password):
        if re.match(r'^[A-Za-z0-9]{8,20}$', password):
            return True
        return False

    def _verify_document(self, document):
        return self.database.verify_default_document(document)

    def _register(self, document):
        if document is None:
            return False
        if (self._verify_document(document)):
            self.database.insert_user(document)
            return True
        return False

    def _generate_document(self, email, password):
        document = self._document_format.copy()
        document["email"] = email
        document["password"] = self._hash_password(password)
        document["provider"] = "default"
        return document

    def _hash_password(self, password):
        password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password

    def process_and_save_access_token(self):
        pass


if __name__ == '__main__':
    pass
