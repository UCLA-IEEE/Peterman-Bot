import datetime

from commands.base_command import BaseCommand
from peterman_bot import peterman_bot as pb

class WhoShouldCommand(BaseCommand):
    """Command for who should currently be in the lab."""

    def get_command_name(self):
        """Abstract method definition."""
        return "whoshould"

    def action(self, *args, **kwargs):
        """Abstract method definition."""
        data = pb.officer_lab_hour_data

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
        return message
