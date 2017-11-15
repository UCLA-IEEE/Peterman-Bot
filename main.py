import time
from slackclient import SlackClient

from PetermanBot.PetermanBot import PetermanBot

def main():
    # get bot_token and bot_id
    with open('./PetermanBot/config/key.txt', 'r') as key_file:
        bot_token = key_file.read().replace('\n', '')

    with open('./PetermanBot/config/bot_id.txt', 'r') as bot_id_file:
        bot_id = bot_id_file.read().replace('\n', '')

    # initialize slack client object
    slack_client = SlackClient(bot_token)
    connection = slack_client.rtm_connect()
    if not connection:
        print 'Connection Failed: Invalid Token'
        exit()

    peterman_bot = PetermanBot(bot_token, bot_id, slack_client)

    timer = time.time()

    # continuously have PetermanBot handle events
    # every 10 seconds, have PetermanBot re-scan the network
    while True:
        peterman_bot.handle_events()

        if time.time() - timer >= 10:
            timer = time.time()
            peterman_bot.run_scan_for_officers()


if __name__ == '__main__':
    main()
