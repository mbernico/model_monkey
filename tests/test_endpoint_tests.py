import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model_monkey.endpoint_tests import ExpectedValueTest, TestFactory


class TestExpectedValueTestCases(unittest.TestCase):

    def setUp(self):
        os.environ['NO_PROXY'] = 'localhost'  # only needed when running against testing_api.py

    def test_good_ExpectedValueTest(self):
        evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/", inputs={"a": 5, "b": 5},
                                predict_label="answer", expected_output=10)
        test_result = evt.run_test()
        self.assertEqual(test_result['success'], True, msg="Expected Value Test True Failed")

    def test_bad_ExpectedValueTest(self):
        evt = ExpectedValueTest(url="http://localhost:5000/v666/predict/", inputs={"a": 5, "b": 5},
                                predict_label="answer", expected_output=11)
        test_result = evt.run_test()
        self.assertEqual(test_result['success'], False, msg="Expected Value Test False Failed")


class TestFactoryTest(unittest.TestCase):

    def test_factory_success(self):
        evt = TestFactory.create("ExpectedValueTest", url="localhost/blah/predict/", inputs=[1, 2, 3],
                                 predict_label='predict', expected_output=6)
        self.assertIsInstance(evt, ExpectedValueTest)

    def test_factory_failure(self):
        with self.assertRaises(AssertionError) as context:
            TestFactory.create("BorkBorkTest")
        self.assertTrue("BorkBorkTest" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
