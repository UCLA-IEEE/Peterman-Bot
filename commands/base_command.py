from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """Base class for a Command object.

    Command objects act as the API - they call the PetermanBot, which does the
    actual work, and then interprets the results, and sends them back to the 
    client.
    
    Args:
        command_name (str): The text representation of the command.
    
    Attributes:
        command_name (str): The text representation of the command.
    """
    def __init__(self):
        """Child should not call __init__ on its own."""
        self.command_name = self.get_command_name()
    
    @abstractmethod
    def get_command_name(self):
        """ABC method.

        Returns:
            str: The name of the child command.
        """
        pass
    
    @abstractmethod
    def action(self, *args, **kwargs):
        """Perform the action of the command, and return the output.

        Args:
            *args (str): The arguments, strings that are passed when user calls the
                command.
            **kwargs (str): the keyword arguments the user calls.
        
        Returns:
            str: The output of the command.
        """
        pass