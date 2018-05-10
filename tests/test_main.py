import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from model_monkey.model_monkey import *
from model_monkey.endpoint_tests import *


@pytest.fixture
def set_up():
    os.environ['NO_PROXY'] = 'localhost'  # only needed when running against testing_api.py

    return {
        "name": "SampleModel",
        "tests": [
            {"type": "ExpectedValueTest",
             "headers":{
                 "apikey": "NRf6gXUUGLNhRIGXP2fq3KeK06xJcP65",
                 "content-type": "application/json"
             },
             "url": "http://localhost:5000/v666/predict/",
             "inputs": {"a": 5, "b": 5},
             "predict_label": "answer",
             "expected_output": 10}
        ]
    }


def test_get_tests_from_config(set_up):
    tests = get_tests_from_config(set_up)
    assert type(tests) is list
    assert isinstance(tests[0], ExpectedValueTest)


def test_execute_tests(set_up):
    tests = get_tests_from_config(set_up)
    assert execute_tests(tests) is None


def test_main(set_up):
    # At this point it doesn't seem sensible to test main()
    pass
