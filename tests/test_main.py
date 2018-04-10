import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model_monkey.model_monkey import *


class TestMain(unittest.TestCase):
    def test_get_tests_from_config(self):
        pass

    def test_execute_tests(self):
        pass

    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()
