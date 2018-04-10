import requests
from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, url):
        self.url = url


    @abstractmethod
    def run_test(self):
        return False

    def _send_request(self, json):
        """
        Sends a request to the configured RESTful endpoint
        :return: endpoint response
        """
        response = requests.post(self.url,json=json)
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



