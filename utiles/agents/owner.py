from utiles.agents.agent import Agent
from src.mvc.subject import Subject
import sys
sys.path.insert(0, '.')


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

    def __init__(self, name:str, x:int, y:int) -> None:
        """
        Initializes a new instance of the Owner class.

        Args:
            name (str): The name of the owner.
            x (int): The x-coordinate of the owner's position.
            y (int): The y-coordinate of the owner's position.
        """

        super().__init__(name, x, y)
        self.inventory = []
        self.status = "Idle"

        self.heart_rate = 60
        self.blood_pressure = "120/80" 
        self.body_temperature = 36.6
        self.respiratory_rate = 16
        self.oxygen_saturation = 98
        self.gcs_score = 15

    def vitals_setter(self, heart_rate:int, blood_pressure:str, body_temperature:float, respiratory_rate:int, oxygen_saturation:int, gcs_score:15) -> None:
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.body_temperature = body_temperature
        self.respiratory_rate = respiratory_rate
        self.oxygen_saturation = oxygen_saturation
        self.gcs_score = gcs_score

    @property
    def vitals(self) -> tuple:
        return self.heart_rate, self.blood_pressure, self.body_temperature, self.respiratory_rate, self.oxygen_saturation, self.gcs_score

    def agent_pick_object(self, object) -> bool:
        '''
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        '''
        # asumiendo que la función se ejecuta solo cuando está encuima del objeto
        if self.x == object.x and self.y == object.y: 
            self.inventory.append(object)
            return True
        else:
            return False

    def agent_drop_object(self, object) -> bool:
        '''
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        '''

        return self.inventory.pop(0)
    

    def handle_event(self, event) -> None:
        """
        Specific event handling for Owner.
        Overrides the default implementation.
        """
        if event.event_type == 'specific_behavior_for_Owner':
            # Specific behavior for Owner
            pass
        else:
            # Call the default implementation for unhandled cases
            super().handle_event(event)
    
    
