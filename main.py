import time
from slackclient import SlackClient

from scanner.scan import run_scan_for_officers

def main():
    with open('./config/key.txt', 'r') as key_file:
        bot_token = key_file.read().replace('\n', '')

    bot_id = "U0H7GEEJW"

    slack_client = SlackClient(bot_token)

    timer = time.time()

    officer_list = []

    if slack_client.rtm_connect():
        while True:
            event_list = slack_client.rtm_read()
            for event in event_list:
                if event.get('text'):
                    user_input = event.get('text').lower().strip()
                    print 'Received user input: ', user_input

            if time.time() - timer >= 5:
                timer = time.time()
                print '5 seconds have passed'

    else:
        print 'Connection Failed: Invalid Token'
        exit()


if __name__ == '__main__':
    main()
