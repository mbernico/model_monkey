import requests
from abc import ABC, abstractmethod
from model_monkey.util import *
from json import JSONDecodeError


class TestFactory:
    @staticmethod
    def create(test_name, **kwargs):

        if test_name == "ExpectedValueTest":
            return ExpectedValueTest(**kwargs)
        if test_name == "ExpectedStatusTest":
            return ExpectedStatusTest(**kwargs)
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
        try:
            response_json = response.json()
        except JSONDecodeError:
            self.logger.error_log("!!!TEST FAIL!!!  HTTP STATUS CODE: " + str(response.status_code))
            return False
        actual_output = int(response_json[self.predict_label])

        success = False
        if actual_output == self.expected_output:
            success = True

        test_result = dict(test_type="ExpectedValueTest",
                           success=success,
                           input=self.inputs,
                           expected_output=self.expected_output,
                           actual_output=actual_output,
                           expected_http_status=200,
                           actual_http_status=response.status_code)

        self.logger.log(**test_result)
        return test_result


class ExpectedStatusTest(BaseTest):
    def __init__(self, url, headers, inputs, expected_http_status):
        super().__init__(url)
        self.headers = headers
        self.inputs = inputs
        self.expected_http_status = expected_http_status

    def run_test(self):
        self.logger.start_timer()
        response = self._send_request(method='post', headers=self.headers, json=self.inputs)
        actual_http_status = int(response.status_code)

        success = False
        if actual_http_status == self.expected_http_status:
            success = True

        test_result = dict(test_type="ExpectedValueTest",
                           success=success,
                           input=self.inputs,
                           expected_output="None",
                           actual_output="None",
                           expected_http_status=200,
                           actual_http_status=response.status_code)

        self.logger.log(**test_result)
        return test_result


