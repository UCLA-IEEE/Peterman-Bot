import time
from slackclient import SlackClient

def main():
    with open('./config/key.txt', 'r') as key_file:
        bot_token = key_file.read().replace('\n', '')

    slack_client = SlackClient(bot_token)

    bot_id = "U0H7GEEJW"

    timer = time.time()

    if slack_client.rtm_connect():
        while True:
            event_list = slack_client.rtm_read()

            if time.time() - timer >= 5:
                timer = time.time()
                print '5 seconds have passed'

            for event in event_list:
                if event.get('text'):
                    user_input = event.get('text').lower().strip()
                    print 'Received user input: ', user_input

    else:
        print 'Connection Failed: Invalid Token'
        exit()

if __name__ == '__main__':
    main()
