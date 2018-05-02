import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model_monkey.model_monkey import *
from model_monkey.endpoint_tests import *


class TestMain(unittest.TestCase):

    def setUp(self):
        self.config = {
            "name": "SampleModel",
            "tests": [
                {"type": "ExpectedValueTest",
                 "url": "http://localhost:5000/v666/predict/",
                 "inputs": {"a": 5, "b": 5},
                 "predict_label": "answer",
                 "expected_output": 10}
            ]
        }

    def test_get_tests_from_config(self):
        tests = get_tests_from_config(self.config)
        self.assertTrue(type(tests) is list, "tests is not a list")
        self.assertIsInstance(tests[0], ExpectedValueTest, "test 0 is not an ExpectedValueTest")

    def test_execute_tests(self):
        tests = get_tests_from_config(self.config)
        self.assertEqual(execute_tests(tests), None, "execute_tests didn't return None")

    def test_main(self):
        # At this point it doesn't seem sensible to test main()
        pass


if __name__ == '__main__':
    unittest.main()
