import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model_monkey.endpoint_tests.endpoint_tests import *


class TestEndpointTestCases(unittest.TestCase):
    def test_good_ExpectedValueTest(self):
        evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/",input={"a":5,"b":5}, predict_label="answer",
                                expected_output=10)
        test_result = evt.run_test()
        self.assertEqual(test_result['success'], True, msg="Expected Value Test True Failed")

    def test_bad_ExpectedValueTest(self):
        evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/",input={"a":5,"b":5}, predict_label="answer",
                                expected_output=11)
        test_result = evt.run_test()
        self.assertEqual(test_result['success'], False, msg="Expected Value Test False Failed")


if __name__ == '__main__':
    unittest.main()
