import json

with open('./PetermanBot/new_config/config.json') as config_file:
    config = json.load(config_file)

print config