import json
from utils.oauth_signup.abstract_oauth_signup import *

class FacebookSignUp(OAuthSignUp):
    def __init__(self):
        super(FacebookSignUp, self).__init__('facebook')
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )

    def authorize(self):
        print(self.consumer_secret)
        print(self.consumer_id)
        print(self.get_callback_url())
        print("authrozie_url : ",self.service.get_authorize_url(
                            scope='email',
                            response_type='code',
                            redirect_uri=self.get_callback_url())
                            )
        return redirect(self.service.get_authorize_url(
                            scope='email',
                            response_type='code',
                            redirect_uri=self.get_callback_url())
                            )

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()},
            decoder=decode_json
        )
        me = oauth_session.get('me?fields=id,email').json()
        return me.get("id", None), me.get("email", None)
