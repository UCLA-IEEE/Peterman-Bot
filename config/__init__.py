import json
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

with open('{}/config.json'.format(dir_path)) as config_file:
    config = json.load(config_file)

config['config_path'] = dir_path