from commands.base_command import BaseCommand
from peterman_bot import peterman_bot as pb

class WhoIsCommand(BaseCommand):
    """Command for who is currently in the lab."""

    def get_command_name(self):
        """Abstract method definition."""
        return "whois"

    def action(self, *args, **kwargs):
        """Abstract method definition."""
        if len(pb.officers_in_lab) == 0:
            message = "There doesn't seem to be any officers in the lab right now."
        else:
            message = "Here is the list of officers in the lab:\n" + "\n".join(pb.officers_in_lab)

        return message
