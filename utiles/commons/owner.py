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

        self.heart_rate = 60  # Initializing to prevent crash due to uninitialized variable
        self.blood_pressure = "120/80"  # Example initialization
        self.body_temperature = 36.6  # Example initialization
        self.respiratory_rate = 16  # Example initialization
        self.oxygen_saturation = 98  # Example initialization
        self.gcs_score = 15  # Example initialization



    def vitals_setter(self, heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score):
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.body_temperature  = body_temperature
        self.respiratory_rate = respiratory_rate
        self.oxygen_saturation = oxygen_saturation
        self.gcs_score = gcs_score

    @property
    def vitals(self):
        return self.heart_rate, self.blood_pressure, self.body_temperature, self.respiratory_rate, self.oxygen_saturation, self.gcs_score

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

        







'''
class Owner(Subject):
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

        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.body_temperature  = body_temperature
        self.respiratory_rate = respiratory_rate
        self.oxygen_saturation = oxygen_saturation
        self.gcs_score = gcs_score
    '''