
class TwitterConfig:
    consumer_key="WNns8HLyN0ktie3efgZQrgusv"
    consumer_secret="IodoMDsdVXOspXD734KAKC1rNXTIArZftGLXvPjoCTv7jbnVuM"
    # access_token_key="798707958280425472-YQ76CxPBh60T4EzUg7ecSsaE5jKNZwa"
    # access_token_secret="1Xvy7pOaqnDacFdimIgpdQCmG7vXIXQk9KPZj9RkqowT1"
    REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
    ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
    AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
    SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'
    CALLBACK_URL = "https://16eac7cd.ngrok.io/api/callback/twitter"