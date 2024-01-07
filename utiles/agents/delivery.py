import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning


class Delivery(Agent, Observer, pathPlanning):

    def __init__(self, name, x, y):
        """
        Initializes a Delivery object.

        Args:
            name (str): The name of the delivery.
            x (int): The x-coordinate of the delivery's position.
            y (int): The y-coordinate of the delivery's position.
        """
        super().__init__(name, x, y)
        self._inventory = {}
        self._status = "Idle"


    @property
    def status(self):
        """
        Get the status of the delivery.

        Returns:
            str: The status of the delivery.
        """
        return self._status
    
    @status.setter
    def status(self, value):
        """Set the status of the delivery."""
        self._status = value


    def updateFromNotification(self, *new_state, **kwargs):
        return super().updateFromNotification(*new_state, **kwargs) # Call the parent class method
    

    def handle_event(self, event):
        """
        Specific event handling for Delivery.
        Overrides the default implementation.
        """
        if event.event_type == 'specific_behavior_for_Delivery':
            # Specific behavior for Delivery
            pass
        else:
            # Call the default implementation for unhandled cases
            super().handle_event(event)