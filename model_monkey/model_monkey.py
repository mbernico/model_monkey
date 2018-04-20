"""
Model Monkey - Application for testing ML Models deployed as RESTful API Endpoints
"""
from model_monkey.util.utils import load_config
from model_monkey.endpoint_tests import TestFactory
import requests


def create_arguments(test):
    arguments = dict(test)
    del arguments['type']
    return arguments


def get_tests_from_config(config):
    """
    Creates test objects of the appropriate type for each test specified in the config
    :param config: configuration dictionary loaded from JSON
    :return: list of test objects
    """
    list_of_test_objects = list()
    config_test_list = config['tests']
    for test in config_test_list:
        arguments = create_arguments(test)
        list_of_test_objects.append(TestFactory.create(test['type'], **arguments))
    return list_of_test_objects


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