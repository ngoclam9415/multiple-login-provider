from user_creator.abstract_factory import AbstractUserFactory
import requests

class FacebookUserFactory(AbstractUserFactory):
    def __init__(self):
        super().__init__()
        self.fb_graph_url = "https://graph.facebook.com/v5.0/me"

    def create_user(self, **kwargs):
        document = self._get_register_information(kwargs)
        return self._register(document)

    def _get_register_information(self, **kwargs):
        fb_access_token = kwargs.get("access_token", None)
        if fb_access_token is None :
            return None
        params = self._get_query_params(fb_access_token)
        fb_id, fb_email = self._get_facebook_information(params)
        document = self._generate_document(fb_id, fb_email)
        return document
            

    def _verify_document(self, document):
        return self.database.verify_fb_document(document)

    def _register(self, document):
        if (self._verify_document(document)):
            self.database.insert_user(document)
            return True
        return False

    def _generate_document(self, fb_id, fb_email):
        document = self._document_format.copy()
        document["email"] = fb_email
        document["facebook_email"] = fb_email
        document["facebook_id"] = fb_id
        document["provider"] = "facebook"
        return document

    def _get_query_params(self, access_token):
        return {"access_token" : access_token, "fields" : "id,name,email"}

    def _get_facebook_information(self, query_params):
        response = requests.post(self.fb_graph_url, params=query_params)
        response_result = response.json()
        fb_id = response_result.get("email", None)
        fb_email = response_result.get("id", None)
        return fb_id, fb_email

if __name__ == '__main__':
    pass
