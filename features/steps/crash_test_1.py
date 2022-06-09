import requests
from behave import *
from helpers import is_port_in_use

@given('we have behave app on server')
def step_impl(context):
    context.headers = {
    'Content-type': 'application/json',
    }

    context.data = '{ "roomSize" : [5, 5], "coords" : [-100, 999], "patches" : [ [1, 0], [2, 2], [2, 3] ], "instructions" : "NNESEESWNWW" }'

    context.response = requests.post('http://localhost:8080/v1/cleaning-sessions', headers=context.headers, data=context.data)

@when('the app is running for the test')
def step_impl(context):
    assert is_port_in_use(8080)

@then('app returns error on input')
def step_impl(context):

    assert "error" in context.response.text