#!/usr/bin/env python
import time
import threading
import os

from authentication import validate_command, validate_command_permissions
from commands import command_mapping, kill_command_name
from parser import parse_command
from slack import MySlackClient
from config import config
from peterman_bot import peterman_bot as pb
from util import create_repeating_timer

OFFICER_SCAN_TIME = 10
REFRESH_DATA_TIME = 60 * 60

def main():
    """
    Creates and instance of PetermanBot, then continuously has it
    handle events and scan the network for officers.
    """

    bot_token = config['bot_key']
    bot_id = config['bot_id']

    slack_client = MySlackClient(bot_token, bot_id)
    start_pb_timers(pb)

    while True:
        channel_id, user_input = slack_client.get_user_input()
        if channel_id:
            command_text, args, kwargs = parse_command(user_input)

            if not validate_command(command_text):
                message = "Invalid command. Type `help` for help."
            elif not validate_command_permissions(command_text, channel_id):
                message = "You do not have permissions to use that command."
            else:
                command = command_mapping[command_text]()
                message = command.action()

            slack_client.send_user_message(channel_id, message)
            if command_text == kill_command_name and validate_command_permissions(command_text, channel_id):
                os._exit(0)

def start_pb_timers(pbot):
    """Starts timer'd threads for PetermanBot updates."""
    create_repeating_timer(pbot.scan_for_officers, OFFICER_SCAN_TIME).start()
    create_repeating_timer(pbot.refresh_data, REFRESH_DATA_TIME).start()

if __name__ == '__main__':
    main()
