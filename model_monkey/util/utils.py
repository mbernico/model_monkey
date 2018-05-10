import json
import argparse


def load_config(config_name):
    """
    Loads a json config file and returns a config dictionary.
    :param config_name: the path to the config json
    """
    with open(config_name) as config_file:
        config = json.load(config_file)
        return config


def parse_args(args):
    """
    Returns arguments passed at the command line as a dict
    """
    parser = argparse.ArgumentParser(description='Generates a machine Learning Dataset.')
    parser.add_argument('-c', help="Config File Location", required=True,
                        dest='config')
    return vars(parser.parse_args(args))

