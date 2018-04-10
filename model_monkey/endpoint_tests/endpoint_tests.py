import requests
from abc import ABC, abstractmethod


class BaseTest(ABC):
    # TODO take configuration on instationation
    @abstractmethod
    def run_test(self):
        return None

    def _send_request(self):
        """
        Sends a request to the configured RESTful endpoint
        :return: endpoint response
        """
        return None

class ExpectedValueTest(BaseTest):
    def run_test(self):
        return None

    def _send_request(self):
        return None

