import sys
sys.path.insert(0, '.')

from src.mvc.subject import Subject
from utiles.commons.agent import Agent

class Owner(Agent, Subject):
    """
    Represents an owner in the system.

    Inherits from Agent and Subject classes.

    Attributes:
        name (str): The name of the owner.
        x (int): The x-coordinate of the owner's position.
        y (int): The y-coordinate of the owner's position.
        inventory (list): The owner's inventory, limited to one object for now.
    """

    def __init__(self, name, x, y):
        """
        Initializes a new instance of the Owner class.

        Args:
            name (str): The name of the owner.
            x (int): The x-coordinate of the owner's position.
            y (int): The y-coordinate of the owner's position.
        """
        Agent.__init__(self, name, x, y)
        Subject.__init__(self)
        self.inventory = []  # owner's inventory, limited to one object for now

    def agent_pick_object(self, object):
        '''
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        '''

        if self.x == object.x and self.y == object.y:
            self.inventory.append(object)
            return True
        else:
            return False

    def agent_drop_object(self, object):
        '''
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        '''
        
        return self.intentory.pop(0)

        