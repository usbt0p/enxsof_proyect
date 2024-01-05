import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning


class Nurse(Agent, Observer, pathPlanning):

    def __init__(self, name, x, y):
        """
        Initializes a Nurse object.

        Args:
            name (str): The name of the nurse.
            x (int): The x-coordinate of the nurse's position.
            y (int): The y-coordinate of the nurse's position.
        """
        Agent.__init__(self, name, x, y)
        Observer.__init__(self, name)
        self._inventory = {}
        self._status = "Idle"


    @property
    def status(self):
        """
        Get the status of the nurse.

        Returns:
            str: The status of the nurse.
        """
        return self._status
    
    @status.setter
    def status(self, value):
        """Set the status of the nurse."""
        self._status = value