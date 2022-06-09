import requests
from behave import *
from helpers import is_port_in_use

@given('we have behave app deployed')
def step_impl(context):
    context.headers = {
    'Content-type': 'application/json',
    }

    context.data = '{ "roomSize" : [5, 5], "coords" : [-100. 999.], "patches" : [ [1, 0], [2, 2], [2, 3] ], "instructions" : "NNESEESWNWW" }'

    context.response = requests.post('http://localhost:8080/v1/cleaning-sessions', headers=context.headers, data=context.data)

@when('the app is up and running')
def step_impl(context):
    assert is_port_in_use(8080)

@then('we get bad request from server')
def step_impl(context):

    assert 400 == context.response.status_code