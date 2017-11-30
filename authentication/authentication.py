from commands import command_mapping
from config import config
from commands.permissions import admin_commands

def validate_command(command):
    """Validates a given command.
    
    Args:
        command (str): The command to be validated.
    Returns:
        bool: Whether or not the command is valid.
    """
    try:
        command_mapping[command]
        return True
    except KeyError:
        return False

def validate_command_permissions(command, user_id):
    """Validates that a user has permissions to use that command.
    
    Args:
        command (str): The command to be validated.
        user_id (str): The user ID that is being checked.
    Returns:
        bool: Wheteher or not the given user has permissions to use the command.
    """
    if (command in admin_commands) and not (user_id in config['admins']):
        return False
    else:
        return True