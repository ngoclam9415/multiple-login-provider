import unittest
from main import *
import json
from utils.database import UserDatabase
from user_creator.facebook_factory import FacebookUserFactory
from user_creator.default_factory import DefaultUserFactory
from test_case import *

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
        result = RegisterAPITestCase1.request(self.app)
        self.assertEquals(result, RegisterAPITestCase1.expected_results)

        result = RegisterAPITestCase2.request(self.app)
        self.assertEquals(result, RegisterAPITestCase2.get_expected_results())

    def test_facebook_factory_methods(self):
        self.database.user_collection.remove({})
        facebook_factory = FacebookUserFactory()

        results = FacebookFactoryTestCases.test_create_user(facebook_factory)
        self.assertEquals(results, FacebookFactoryTestCases.test_create_user_expected_result)

    def test_default_factory_methods(self):
        self.database.user_collection.remove({})
        default_factory = DefaultUserFactory()
        # results = DefaultFactoryTestCases.test_create_user(default_factory)
        # self.assertEquals(results, DefaultFactoryTestCases.get_expected_results())
        results = DefaultFactoryTestCases.test_verify_email(default_factory)
        self.assertEquals(results, DefaultFactoryTestCases.email_status)
        results = DefaultFactoryTestCases.test_verify_password(default_factory)
        self.assertEquals(results, DefaultFactoryTestCases.password_status)


    def test_callback_page(self):
        response = self.app.get('/api/callback/facebook', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/api/callback/twitter', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()
    UserDatabase().user_collection.remove({})