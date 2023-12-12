import sys
sys.path.insert(0, '.')


class Agent():
    """
    Represents an agent in the environment.
    """

    def __init__(self, name, x=0, y=0):
        """
        Initializes an Agent object.
        Parameters:
        - name (str): The name of the agent.
        - position (tuple): The initial position of the agent. Defaults to (0, 0).
        """
        self.name = name
        self.inventory = []
        self.x = x
        self.y = y

    def print_position(self):
            """
            Returns the current position of the agent.

            Returns:
                str: A string representing the current position in the format (x, y).
            """
            return f"({self.x}, {self.y})"

    def position(self, x, y):
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
        
    def animate_movement(self, movements, index=0):
        if index < len(movements):
            pos = movements[index]
            self.move_agent('robot', pos)
            self.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.after(1000, lambda: self.animate_movement(movements, index + 1))
 

