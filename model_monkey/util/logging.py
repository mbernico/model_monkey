import logging
import sys
import time
import datetime
import json


class Borg:
    """Borg Pattern by  Alex Martelli.  Like a Singleton but maybe more elegant, all instances of this
    class will have the same internal state"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class BaseLogger(Borg):

    def __init__(self):
        Borg.__init__(self)
        if not hasattr(self, 'logger'):  # create a monostate logger only the first time the class is instantiated
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.INFO)
            self.fmt = logging.Formatter("MONKEY_LOG:%(message)s")
            self.stdout_handler = logging.StreamHandler(sys.stdout)
            self.stdout_handler.setFormatter(self.fmt)
            self.logger.addHandler(self.stdout_handler)

    def start_timer(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        now = time.time()
        try:
            delta_time = now - self.start_time
        except AttributeError as a:
            logging.debug("elapsed time can't be computed without a call to start_timer() first.")
            return False
        return delta_time

    @staticmethod
    def get_current_time(human=True):
        timestamp = time.time()
        human_readable_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S %z')
        if human:
            return human_readable_time
        return timestamp


class MonkeyLogger(BaseLogger):

    def __init__(self):
        super().__init__()

    def log(self, test_type, success, input, expected_output, actual_output, expected_http_status, actual_http_status):
        log_message = dict(test_type=test_type,
                           success=success,
                           timestamp=self.get_current_time(),
                           delta_time=self.get_elapsed_time(),
                           input=input,
                           expected_output=expected_output,
                           actual_output=actual_output,
                           expected_http_status=expected_http_status,
                           actual_http_status=actual_http_status)
        self.logger.info(msg=json.dumps(log_message))

    def error_log(self, message):
        self.logger.error(msg=message)
