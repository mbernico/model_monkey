import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_monkey.util import *


def test_load_json():
    jf = os.path.join(os.path.dirname(__file__), '../../example/sample.json')
    c = load_config(jf)
    assert c['name'] == 'SampleTestSet'


def test_Borg():
    b1 = Borg()
    b2 = Borg()
    assert b1 != b2
    b1.sound = "woof"
    assert b2.sound == "woof"


def test_BaseLoggerBorginess():
    logger = BaseLogger()
    logger2 = BaseLogger()
    assert id(logger.logger) == id(logger2.logger)


def test_MonkeyLoggerLog(capsys):
    logger = MonkeyLogger()
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.logger.addHandler(stdout_handler)
    logger.start_timer()
    time.sleep(1)
    logger.log(test_type="Endpoint_Test", success=True, input={"a": 5, "b": 5}, expected_output=10, actual_output=10,
               expected_http_status=200, actual_http_status=200)
    out, err = capsys.readouterr()
    assert "Endpoint_Test" in out


def test_timer():
    logger = MonkeyLogger()
    logger.start_timer()
    time.sleep(1)
    time_out = logger.get_elapsed_time()
    assert time_out > 0


def test_current_time():
    logger = MonkeyLogger()
    current_time = logger.get_current_time(human=True)
    assert ":" in current_time
    current_time = logger.get_current_time(human=False)
    assert current_time > 0

def test_arg_parser():
    args = parse_args(["-ctest.json"])
    assert args['config'] == 'test.json', "parse_args failed to parse it's argument"