import time
from slackclient import SlackClient

from scanner.scan import run_scan_for_officers
from scanner.util import get_mac_address_map
from handler.index import handle_input

def main():
    with open('./config/key.txt', 'r') as key_file:
        bot_token = key_file.read().replace('\n', '')

    bot_id = "U0H7GEEJW"

    slack_client = SlackClient(bot_token)

    timer = time.time()

    mac_address_map = get_mac_address_map()
    officers_in_lab = run_scan_for_officers(mac_address_map)

    if slack_client.rtm_connect():
        while True:
            response = ''
            event_list = slack_client.rtm_read()
            for event in event_list:
                if event.get('text'):
                    user_input = event.get('text').lower().strip()
                    response = handle_input(user_input, officers_in_lab)

            if time.time() - timer >= 10:
                timer = time.time()
                officers_in_lab = run_scan_for_officers(mac_address_map)

            if response and event.get('user') != bot_id:
                channel_id = event.get('channel')
                slack_client.api_call('chat.postMessage', as_user='true', channel=channel_id, text=response)

    else:
        print 'Connection Failed: Invalid Token'
        exit()


if __name__ == '__main__':
    main()
