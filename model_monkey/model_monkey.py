"""
Model Monkey - Application for testing ML Models deployed as RESTful API Endpoints
"""
from model_monkey.util import load_config, parse_args
from model_monkey.endpoint_tests import TestFactory
import sys


def create_arguments(test):
    """
    Arguments for a test include everything but the test type.  Arguments is a test minus the type.
    :param test:
    :return: arguments
    """
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
    :return: None
    """
    for test in tests:
        test.run_test()


def main(config=None):

    if config is None:
        # called from the command line so parse configuration
        args = parse_args(sys.argv[1:])
        config = load_config(args['config'])

    # config = load_config("../example/sample.json")
    tests = get_tests_from_config(config)
    execute_tests(tests)


if __name__ == "__main__":
    main()
