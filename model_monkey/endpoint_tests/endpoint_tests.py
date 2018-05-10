import requests
from abc import ABC, abstractmethod
from model_monkey.util import *


class TestFactory:
    @staticmethod
    def create(test_name, **kwargs):

        if test_name == "ExpectedValueTest":
            return ExpectedValueTest(**kwargs)
        else:
            raise AssertionError("Bad test type: " + test_name)


class BaseTest(ABC):
    def __init__(self, url):
        self.url = url
        self.logger = MonkeyLogger()

    @abstractmethod
    def run_test(self):
        pass

    def _send_request(self, method='post', headers=None, json=None):
        """
        Sends a request to the configured RESTful endpoint
        
        :param method: http method to use
        :param method: json data to pass
        :return: endpoint response
        """
        response = getattr(requests, method)(self.url, headers=headers, json=json)
        return response


class ExpectedValueTest(BaseTest):
    def __init__(self, url, headers, inputs, predict_label, expected_output):
        super().__init__(url)
        self.headers = headers
        self.inputs = inputs
        self.predict_label = predict_label
        self.expected_output = expected_output

    def run_test(self):
        self.logger.start_timer()
        response = self._send_request(method='post', headers=self.headers, json=self.inputs)
        response_json = response.json()
        api_prediction = response_json[self.predict_label]

        success = False
        if api_prediction == self.expected_output:
            success = True

        test_result = dict(test_type="ExpectedValueTest",
                           success=success,
                           inputs=self.inputs,
                           expected_outputs=self.expected_output,
                           api_output=api_prediction,
                           response_code=response.status_code)

        self.logger.log(**test_result)
        return test_result




