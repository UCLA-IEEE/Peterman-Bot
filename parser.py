from commands import command_mapping

def parse_command(command):
    """Parse a command, to give back a command instance, and the args and kwargs.
    
    Args:
        command (str): A command that a user entered in slack.
    
    Returns:
        str, [], {}: The command string, the args, and the kwargs.
    """
    split_command = command.split(' ')
    command_text = split_command[0]
    args = split_command[1:]

    return command_text, args, {}