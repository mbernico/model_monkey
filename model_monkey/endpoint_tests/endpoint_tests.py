import requests
from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, url):
        self.url = url


    @abstractmethod
    def run_test(self):
        return False

    def _send_request(self, method='post', json=None):
        """
        Sends a request to the configured RESTful endpoint
        
        :param method: http method to use
        :param method: json data to pass
        :return: endpoint response
        """
        response = getattr(requests,method)(self.url,json=json) 
        return response


class ExpectedValueTest(BaseTest):
    def __init__(self, url, input, predict_label, expected_output):
        self.url = url
        self.input = input
        self.predict_label = predict_label
        self.expected_output = expected_output

    def run_test(self):
        api_response = self._send_request(self.input)
        api_prediction_json = api_response.json()
        api_prediction = api_prediction_json[self.predict_label]
        if api_prediction == self.expected_output:
            return {"success": True,
                    "input": self.input,
                    "expected_output": self.expected_output,
                    "api_prediction": api_prediction}

        return {"success": False,
                "input": self.input,
                "expected_output": self.expected_output,
                "api_prediction": api_prediction}



