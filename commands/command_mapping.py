from .whois import WhoIsCommand
from .whoshould import WhoShouldCommand
from .kill import KillCommand

command_mapping = {
    WhoIsCommand().command_name: WhoIsCommand,
    WhoShouldCommand().command_name: WhoShouldCommand,
    KillCommand().command_name: KillCommand
}

kill_command_name = KillCommand().command_name