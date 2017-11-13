class InputHandler(object):

    def __init__(self, slack_client):
        self.slack_client = slack_client

    def handle_input(self, user_input, officers_in_lab, channel_id):
        handler_map = {
            "whois": self.handleWhoIs(officers_in_lab, channel_id)
        }

        if user_input not in handler_map:
            self.handleUnknownInput(handler_map, channel_id)
        else:
            handler_map[user_input]

    def handleWhoIs(self, officers_in_lab, channel_id):
        if len(officers_in_lab) == 0:
            message = "There doesn't seem to be any officers in the lab right now."
        else:
            message = "Here is the list of officers in the lab:\n" + "\n".join(officers_in_lab)

        self.sendMessage(message, channel_id)

    def handleUnknownInput(self, handler_map, channel_id):
        message = "Here are the commands that I support:\n"
        for key in handler_map:
            message += key + '\n'

        self.sendMessage(message, channel_id)

    def sendMessage(self, message, channel_id):
        self.slack_client.api_call('chat.postMessage', as_user='true', channel=channel_id, text=message)
