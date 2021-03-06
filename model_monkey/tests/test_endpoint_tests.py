import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from model_monkey.endpoint_tests import ExpectedValueTest, TestFactory, ExpectedStatusTest


@pytest.fixture
def set_proxy():
    os.environ['NO_PROXY'] = 'localhost'  # only needed when running against testing_api.py


def test_good_ExpectedValueTest(set_proxy):
    evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/",headers=None, inputs={"a": 5, "b": 5},
                            predict_label="answer", expected_output=10)
    test_result = evt.run_test()
    assert test_result['success'] is True


def test_bad_ExpectedValueTest(set_proxy):
    evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/",headers=None, inputs={"a": 5, "b": 5},
                            predict_label="answer", expected_output=11)
    test_result = evt.run_test()
    assert test_result['success'] is False


def test_factory_success():
    evt = TestFactory.create("ExpectedValueTest", url="localhost/blah/predict/", headers=None, inputs=[1, 2, 3],
                             predict_label='predict', expected_output=6)
    assert isinstance(evt, ExpectedValueTest)


def test_factory_failure():
    with pytest.raises(AssertionError) as context:
        TestFactory.create("BorkBorkTest")
    assert "BorkBorkTest" in str(context.value)


def test_good_ExpectedStatusTest(set_proxy):
    evt = ExpectedStatusTest(url="http://localhost:5000/v666/predict/", headers=None, inputs={"a": 5, "b": 5},
                             expected_http_status=200)
    test_result = evt.run_test()
    assert test_result['success'] is True


def test_bad_ExpectedStatusTest(set_proxy):
    evt = ExpectedStatusTest(url="http://localhost:5000/v666/predict/",headers=None, inputs={"a": 5},
                             expected_http_status=200)
    test_result = evt.run_test()
    assert test_result['success'] is False