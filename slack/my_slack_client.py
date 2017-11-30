from slackclient import SlackClient

class MySlackClient:
    """A wrapper for the slack client, so that we do not have to call the API directly.

    Args:
        bot_token: The API token of the bot.
        bot_id: The ID of the bot.
    """
    def __init__(self, bot_token, bot_id):
        self.bot_token = bot_token
        self.bot_id = bot_id

        self.slack_client = SlackClient(bot_token)
        connection = self.slack_client.rtm_connect()
        if not connection:
            print('Connection Failed: Invalid Token')
            exit()
    
    def get_user_input(self):
        """Returns the current user input from the slack client, as well
            as the channel to respond to, and the ID of the user.

        Returns:
            str, str, str: User id, channel id to respond to, actual user input.
                If no input, returns None.
        """
        event_list = self.slack_client.rtm_read()
        for event in event_list:
            if event.get('text') and event.get('user') != self.bot_id:
                channel_id = event.get('channel')
                user_id = event.get('user')
                user_input = event.get('text').lower().strip()
                return user_id, channel_id, user_input
        
        return None, None, None

    def send_user_message(self, channel_id, message):
        """Send a slack message over a given channel ID."""
        self.slack_client.api_call('chat.postMessage', as_user='true', channel=channel_id, text=message)
