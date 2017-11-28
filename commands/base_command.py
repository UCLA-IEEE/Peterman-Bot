class Command:
    """Base class for a Command object.

    Command objects act as the API - they call the PetermanBot, which does the
    actual work, and then interprets the results, and sends them back to the 
    client.
    
    Args:
        command_name (str): The text representation of the command.
    
    Attributes:
        command_name (str): The text representation of the command.
    """

    def __init__(self, name):
        """Child must call this __init__ to specify the name."""
        self.command_name = self.get_command_name()
    
    def get_command_name(self):
        """ABC method.

        Returns:
            str: The name of the child command.
        """
        pass