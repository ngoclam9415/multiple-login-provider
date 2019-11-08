import json
from unittest.mock import MagicMock

class RegisterAPITestCase1:
    headers = {"Content-Type" : "application/json"}
    access_tokens = ["EAAl6RKwZCpmsBAGu2Tkl2ZBMGA9ZCUGyZCab41rfwkSZB5RdcFAmsvwnRqtocnVlGqkkMuBj4K8vnZC5ORmyTyzF7eEeyDSepEad0c85YZAgwSD1POjjadXJMrdMArOr1Ob3nNZBhQdGQ0nyiGvNDncsYLgivYwljReyNmI7u6qpCgC3XabeHWRV", "asdasd123asd!@@SAS", "!@#$%^&*YGHA(SHIANS)"]
    expected_results = [True, False, False]

    @classmethod
    def request(self, app):
        results = []
        for access_token in self.access_tokens:
            response = app.post('/api/register', headers=self.headers, data=json.dumps({"provider" : "facebook", "access_token" : access_token}))
            results.append(json.loads(response.data))
        return results

class RegisterAPITestCase2:
    headers = {"Content-Type" : "application/json"}

    emails = ["dasd123123", "112312e12e", "", "lamnn@athena.studio"]
    email_status = [False, False, False, True]
    
    passwords = ["dasd123123", "11231!#$%^W&QS2e12e", "", "asd12e1jadsasdsasdasdasdasdasdasdascasbjahbrwqnnancnmbashbmca"]
    password_status = [True, False, False, False]

    @classmethod
    def request(self, app):
        results = []
        for email in self.emails:
            for password in self.passwords:
                response = app.post('/api/register', headers=self.headers, data=json.dumps({"email" : email, "password" : password, "provider" : "default"}))
                results.append(json.loads(response.data))
        return results

    @classmethod
    def get_expected_results(self):
        return [(x and y) for x in self.email_status for y in self.password_status]

class FacebookFactoryTestCases:
    access_tokens = ["EAAl6RKwZCpmsBAGu2Tkl2ZBMGA9ZCUGyZCab41rfwkSZB5RdcFAmsvwnRqtocnVlGqkkMuBj4K8vnZC5ORmyTyzF7eEeyDSepEad0c85YZAgwSD1POjjadXJMrdMArOr1Ob3nNZBhQdGQ0nyiGvNDncsYLgivYwljReyNmI7u6qpCgC3XabeHWRV", "asdasd123asd!@@SAS", "!@#$%^&*YGHA(SHIANS)", ""]
    test_create_user_expected_result = [True, False, False, False]
    datas = [{"access_token" : access_token} for access_token in access_tokens]
    test_get_register_information = [True, None, None, None]

    @classmethod
    def test_create_user(self, facebook_factory):
        results = []
        for data in self.datas:
            result = facebook_factory.create_user(**data)
            results.append(result)
        return results

class DefaultFactoryTestCases:
    headers = {"Content-Type" : "application/json"}

    emails = ["dasd123123", "112312e12e", "", "lamnn@athena.studio", "lamnn@121312", "1411963@hcmut.edu.vn"]
    email_status = [False, False, False, True, False, True]

    passwords = ["dasd123123", "11231!#$%^W&QS2e12e", "", "asd12e1jadsasdsasdasdasdasdasdasdascasbjahbrwqnnancnmbashbmca", "1AjcmdDef123"]
    password_status = [True, False, False, False, True]

    @classmethod
    def get_expected_results(self):
        return [(x and y) for x in self.email_status for y in self.password_status]

    @classmethod
    def test_verify_email(self, default_factory):
        return [default_factory.verify_email(email) for email in self.emails]

    @classmethod
    def test_verify_password(self, default_factory):
        return [default_factory.verify_password(password) for password in self.passwords]

    @classmethod
    def test_create_user(self, default_factory):
        results = []
        for email in self.emails:
            for password in self.passwords:
                result = default_factory.create_user(**{"email" : email, "password" : password})
                results.append(result)
        return results