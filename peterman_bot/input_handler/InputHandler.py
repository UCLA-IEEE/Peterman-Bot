import requests, json, datetime

from PetermanBot.config import config

class InputHandler(object):
    def __init__(self, slack_client):
        self.slack_client = slack_client
        self.owner_id = config['owner']
        self.stats = {}

    def handleStats(self,channel_id):
        message = "Here are my stats since my last restart:\n"
        for key in self.stats:
            message += key + ': ' + str(self.stats[key]) + ' calls\n'

        self.sendMessage(message, channel_id)

    def record_input(self, user_input):
        if user_input not in self.stats:
            self.stats[user_input] = 1
        else:
            self.stats[user_input] += 1
