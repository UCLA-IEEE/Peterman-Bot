from commands.whois import WhoIsCommand
from commands.whoshould import WhoShouldCommand
from commands.kill import KillCommand

handler_commands = set([
    WhoIsCommand().command_name,
    WhoShouldCommand().command_name
])

admin_commands = set([
    KillCommand().command_name
])