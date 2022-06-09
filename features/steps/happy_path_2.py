import requests
from behave import *

@given('we have behave app online and valid coord yet')
def step_impl(context):
    context.headers = {
    'Content-type': 'application/json',
    }

    context.data = '{ "roomSize" : [5, 5], "coords" : [3, 3], "patches" : [ [1, 0], [2, 2], [2, 3] ], "instructions" : "NNESEESWNWW" }'

    context.response = requests.post('http://localhost:8080/v1/cleaning-sessions', headers=context.headers, data=context.data)
"""
@when('we implement a test')
def step_impl(context):
    assert True is not False
"""

@then('the result is again the expected')
def step_impl(context):

    assert "1" == context.response.text.split("patches")[1].split(":")[1].rstrip("}")