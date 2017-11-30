from commands.base_command import BaseCommand

class KillCommand(BaseCommand):
    def get_command_name(self):
        return "kill"

    def action(self, *args, **kwargs):
        return "PetermanBot shutting down. See you later!"