import urllib2, json, datetime

class InputHandler(object):

    def __init__(self, slack_client):
        self.slack_client = slack_client
        with open('./PetermanBot/config/owner.txt', 'r') as owner_file:
            self.owner_id = owner_file.read().replace('\n', '')
        self.stats = {}

    def handle_input(self, user_input, officers_in_lab, channel_id, event):
        handler_map = {
            "whois": self.handleWhoIs,
            "whoshould": self.handleWhoIsSupposedToBe
        }

        admin_map = {
            "kill": self.handleKill,
            "stats": self.handleStats
        }

        if user_input not in handler_map and user_input not in admin_map:
            self.handleUnknownInput(handler_map, channel_id)
        elif user_input in admin_map:
            if event.get('user') != self.owner_id:
                self.handleUnknownInput(handler_map, channel_id)
            else:
                admin_map[user_input](channel_id)

            if event.get('user') != self.owner_id:
                self.record_input(user_input)
        else:
            handler_map[user_input](officers_in_lab, channel_id)

            if event.get('user') != self.owner_id:
                self.record_input(user_input)

    def handleWhoIs(self, officers_in_lab, channel_id):
        if len(officers_in_lab) == 0:
            message = "There doesn't seem to be any officers in the lab right now."
        else:
            message = "Here is the list of officers in the lab:\n" + "\n".join(officers_in_lab)

        self.sendMessage(message, channel_id)

    def handleWhoIsSupposedToBe(self, officers_in_lab, channel_id):
        with open('./PetermanBot/config/google_api_key.txt', 'r') as key_file:
            api_key = key_file.read().replace('\n', '')
        spreadsheet_id = '1pYy3YIyndz-xe2BTZQxWkEPFuxomc7lJTKdm988trOA'
        api_url = 'https://sheets.googleapis.com/v4/spreadsheets/' + spreadsheet_id + '/values/Fall%202017!A1:G13?key=' + api_key
        response = json.loads(urllib2.urlopen(api_url).read())
        data = response['values']
        date = datetime.datetime.today()
        dayOfTheWeek = date.weekday()
        hoursSinceEight = date.hour - 8
        nextHour = hoursSinceEight + 1

        if hoursSinceEight > 11:
            hoursSinceEight = 11
        if nextHour > 11:
            nextHour = 11


        if dayOfTheWeek > 4:
            message = 'No one is obligated to be in here on the weekends!'
        elif hoursSinceEight < 0:
            message = "It's too early for anyone to be in the lab!"
        else:
            officers = data[hoursSinceEight + 1][dayOfTheWeek + 1]
            nextOfficers = data[nextHour + 1][dayOfTheWeek + 1]
            message = 'Here are the officers signed up for this hour:\n'
            message += officers
            message += '\nHere are the officers that are signed up for the next hour:\n'
            message += nextOfficers

        self.sendMessage(message, channel_id)

    def handleKill(self, channel_id):
        message = "Peterman Bot shutting down. See ya later!"
        self.sendMessage(message, channel_id)
        exit()

    def handleStats(self,channel_id):
        message = "Here are my stats since my last restart:\n"
        for key in self.stats:
            message += key + ': ' + str(self.stats[key]) + ' calls\n'

        self.sendMessage(message, channel_id)

    def handleUnknownInput(self, handler_map, channel_id):
        message = "Here are the commands that I support:\n"
        for key in handler_map:
            message += key + '\n'

        self.sendMessage(message, channel_id)

    def sendMessage(self, message, channel_id):
        self.slack_client.api_call('chat.postMessage', as_user='true', channel=channel_id, text=message)

    def record_input(self, user_input):
        if user_input not in self.stats:
            self.stats[user_input] = 1
        else:
            self.stats[user_input] += 1
