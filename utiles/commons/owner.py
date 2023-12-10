import sys
sys.path.insert(0, '.')

from src.mvc.subject import Subject

global heart_rate
global blood_pressure
global body_temperature
global respiratory_rate
global oxygen_saturation
global gcs_score

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