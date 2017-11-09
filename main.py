from slackclient import SlackClient

def main():
    with open('./config/key.txt', 'r') as key_file:
        bot_token = key_file.read().replace('\n', '')

    slack_obj = SlackClient(bot_token)

    bot_id = "U0H7GEEJW"

    timer = 0

    if slack_obj.rtm_connect():
        print 'hello world'
    else:
        print 'Connection Failed: Invalid Token'
        exit()

if __name__ == '__main__':
    main()
