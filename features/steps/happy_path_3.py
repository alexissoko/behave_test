import requests
from behave import *

@given('we have behave app online one more time')
def step_impl(context):
    context.headers = {
    'Content-type': 'application/json',
    }

    context.data = '{ "roomSize" : [5, 5], "coords" : [0, 0], "patches" : [ [1, 0], [2, 2], [2, 3] ], "instructions" : "NNESEESWNWW" }'

    context.response = requests.post('http://localhost:8080/v1/cleaning-sessions', headers=context.headers, data=context.data)
"""
@when('we implement a test')
def step_impl(context):
    assert True is not False
"""

@then('the result is empty this time')
def step_impl(context):

    assert "0" == context.response.text.split("patches")[1].split(":")[1].rstrip("}")