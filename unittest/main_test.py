import unittest
from main import *
import json
from utils.database import UserDatabase

class FlaskMainAppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
        self.database = UserDatabase()
        self.database.user_collection.remove({})

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_api(self):
        headers = {"Content-Type" : "application/json"}
        access_tokens = ["EAAl6RKwZCpmsBAGu2Tkl2ZBMGA9ZCUGyZCab41rfwkSZB5RdcFAmsvwnRqtocnVlGqkkMuBj4K8vnZC5ORmyTyzF7eEeyDSepEad0c85YZAgwSD1POjjadXJMrdMArOr1Ob3nNZBhQdGQ0nyiGvNDncsYLgivYwljReyNmI7u6qpCgC3XabeHWRV", "asdasd123asd!@@SAS", "!@#$%^&*YGHA(SHIANS)"]
        expected_results = [True, False, False]
        for index, access_token in enumerate(access_tokens):
            response = self.app.post('/api/register', headers=headers, data=json.dumps({"provider" : "facebook", "access_token" : access_token}))
            print(index, response.data)
            self.assertEqual(json.loads(response.data), expected_results[index])

        expected_results = [False, False, False]
        for index, access_token in enumerate(access_tokens):
            response = self.app.post('/api/register', headers=headers, data=json.dumps({"provider" : "twitter", "oauth_token" : access_token}))
            print(index, response.data)
            self.assertEqual(json.loads(response.data), expected_results[index])

        emails = ["dasd123123", "112312e12e", "", "lamnn@athena.studio"]
        email_status = [False, False, False, True]
        passwords = ["dasd123123", "11231!#$%^W&QS2e12e", "", "asd12e1jadsasdsasdasdasdasdasdasdascasbjahbrwqnnancnmbashbmca"]
        password_status = [True, False, False, False]
        for i, email in enumerate(emails):
            for j, password in enumerate(passwords):
                response = self.app.post('/api/register', headers=headers, data=json.dumps({"email" : email, "password" : password, "provider" : "default"}))
                self.assertEqual(json.loads(response.data), email_status[i] and password_status[j])

    def test_callback_page(self):
        response = self.app.get('/api/twitter_callback', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()
    UserDatabase().user_collection.remove({})