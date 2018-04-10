import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model_monkey.util.utils import *


class TestUtils(unittest.TestCase):
    def test_load_json(self):
        jf = os.path.join(os.path.dirname(__file__), '../example/sample.json')
        c = load_config(jf)
        self.assertEquals(c['name'], 'SampleModel', msg="JSON load not sane")


if __name__ == '__main__':
    unittest.main()
