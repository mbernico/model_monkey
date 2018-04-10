"""
Model Monkey - Application for testing ML Models deployed as RESTful API Endpoints
"""
from util.utils import load_config
import requests


def get_tests_from_config(config):
    """
    Creates test objects of the appropriate type for each test specified in the config
    :param config: configuration dictionary loaded from JSON
    :return: list of test objects
    """
    # TODO config should contain more than one test.
    # TODO get test config and return a list of test objs
    pass


def execute_tests(tests):
    """
    Executes the tests in each test Obj in the lists tests
    :param tests: a list of test objects
    :return: Nothing
    """
    # TODO execute each test in the set of tests, logging as we go.
    pass


def main():
    config = load_config("../example/sample.json")
    tests = get_tests_from_config(config)
    execute_tests(tests)





if __name__ == "__main__":
    main()