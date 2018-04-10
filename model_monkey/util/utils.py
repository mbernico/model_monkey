import json

def load_config(config_name):
    """
    Loads a json config file and returns a config dictionary.
    :param config_name: the path to the config json
    """
    with open(config_name) as config_file:
        config = json.load(config_file)
        return config

