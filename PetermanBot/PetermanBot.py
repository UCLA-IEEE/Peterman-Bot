import csv
from Scanner.Scanner import Scanner
from InputHandler.InputHandler import InputHandler

class PetermanBot(object):

    def __init__(self, bot_token, bot_id, slack_client):
        self.bot_token = bot_token
        self.bot_id = bot_id
        self.slack_client = slack_client
        self.mac_address_map = self.get_mac_address_map()
        self.scanner = Scanner()
        self.officers_in_lab = self.run_scan_for_officers()
        self.input_handler = InputHandler(slack_client)

    def get_mac_address_map(self):
        file_handler = open('./PetermanBot/config/officers.csv', 'rb')
        reader = csv.reader(file_handler)

        mac_address_map = {}
        for row in reader:
            mac_address_map[row[0]] = row[1]

        return mac_address_map

    def run_scan_for_officers(self):
        self.officers_in_lab = self.scanner.scan_arp(self.mac_address_map)

    def handle_events(self):
        event_list = self.slack_client.rtm_read()
        for event in event_list:
            if event.get('text') and event.get('user') != self.bot_id:
                channel_id = event.get('channel')
                user_input = event.get('text').lower().strip()
                self.handle_input(user_input, channel_id)

    def handle_input(self, user_input, channel_id):
        print self.officers_in_lab
        self.input_handler.handle_input(user_input, self.officers_in_lab, channel_id)
