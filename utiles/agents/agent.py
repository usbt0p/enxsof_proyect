import sys
sys.path.insert(0, '.')


from utiles.commons.event import Event

class Agent():
    """
    Represents an agent in the environment.
    """

    def __init__(self, name:str, x=0, y=0) -> None:
        """
        Initializes an Agent object.
        """
        self.name = name
        self.inventory = []
        self.x = x
        self.y = y

    def print_position(self) -> str:
        """
        Returns the current position of the agent.

        Returns:
            str: A string representing the current position in the format (x, y).
        """
        return f"({self.x}, {self.y})"

    def position(self, x:int, y:int) -> None:
        """
        Set the position of the agent.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
        """
        self.x = x
        self.y = y


    def __str__(self) -> str:
        """
        Returns a string representation of the Agent object.

        The string includes the agent's name and position.

        Returns:
            str: A string representation of the Agent object.
        """
        return f"Agent: {self.name} at position {self.print_position()}"
        


    def handle_event(self, event:Event) -> None:
        """
        Default event handling. Can be overridden by subclasses.
        """

        valid_events = ['default_behavior','move']

        if event.event_type in valid_events:
            pass
        else:
            print(f"Unhandled event type: {event.event_type}")
            