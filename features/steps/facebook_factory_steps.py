from behave import *
import parse
from user_creator.facebook_factory import FacebookUserFactory


@given(u'a access_token {access_token}')
def step_impl(context, access_token):
    context.facebook_factory = FacebookUserFactory()
    context.access_token = access_token


@when(u'asked to find user\'s email and facebook id')
def step_impl(context):
    params = context.facebook_factory._get_query_params(context.access_token)
    fb_id, email = context.facebook_factory._get_facebook_information(params)
    context.fb_id = "undefined" if fb_id == None else fb_id
    context.email = "undefined" if email == None else email

@then(u'user\'s email is : {email} and user\'s facebook id is : {fb_id}')
def step_impl(context, email, fb_id):
    assert (context.fb_id == fb_id and context.email == email)