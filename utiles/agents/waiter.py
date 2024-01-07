import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning


class Waiter(Agent, Observer, pathPlanning):

    def __init__(self, name, x, y):
        """
        Initializes a Waiter object.

        Args:
            name (str): The name of the waiter.
            x (int): The x-coordinate of the waiter's position.
            y (int): The y-coordinate of the waiter's position.
        """
        super().__init__(name, x, y)
        self._inventory = {}
        self._status = "Idle"


    @property
    def status(self):
        """
        Get the status of the waiter.

        Returns:
            str: The status of the waiter.
        """
        return self._status
    
    @status.setter
    def status(self, value):
        """Set the status of the waiter."""
        self._status = value


    def updateFromNotification(self, *new_state, **kwargs):
        return super().updateFromNotification(*new_state, **kwargs) # Call the parent class method
    

    def handle_event(self, event):
        """
        Specific event handling for Waiter.
        Overrides the default implementation.
        """
        if event.event_type == 'specific_behavior_for_waiter':
            # Specific behavior for Waiter
            pass
        else:
            # Call the default implementation for unhandled cases
            super().handle_event(event)