import csv
import time

import requests

from config import config
from .scanner import Scanner

class PetermanBot(object):
    """Basically the backend for the application, runs scans for officers.

    Attributes:
        officers_in_lab ([str]): A list of the officers currently in the lab.
    """
    def __init__(self):
        self.refresh_data()

    def refresh_data(self):
        self.mac_address_map = self.get_mac_address_map()
        self.scanner = Scanner()
        self.officers_in_lab = []
        self.scan_for_officers()
        self.officer_lab_hour_data = self.get_officer_lab_hour_data()

    def get_mac_address_map(self):
        file_handler = open(config['config_path'] + '/officers.csv', 'r')
        reader = csv.reader(file_handler)

        mac_address_map = {}
        for row in reader:
            mac_address_map[row[0]] = row[1]

        return mac_address_map

    def scan_for_officers(self):
        self.officers_in_lab = self.scanner.scan_arp(self.mac_address_map)

    def get_officer_lab_hour_data(self):
        api_key = config['GOOGLE_API_KEY']
        spreadsheet_id = config['SPREADSHEET_ID']
        api_url = 'https://sheets.googleapis.com/v4/spreadsheets/' + spreadsheet_id + '/values/Fall%202017!A1:G13?key=' + api_key
        response = requests.get(api_url).json()
        data = response['values']
        return data
