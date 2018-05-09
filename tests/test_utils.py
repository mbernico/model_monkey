import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from model_monkey.util.utils import *


def test_load_json():
    jf = os.path.join(os.path.dirname(__file__), '../example/sample.json')
    c = load_config(jf)
    assert c['name'] ==  'SampleModel'
