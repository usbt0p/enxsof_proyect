import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning


class Nurse(Agent, Observer, pathPlanning):
    """
    A class representing a nurse agent in a simulation.

    Attributes:
    - name (str): The name of the nurse.
    - x (int): The x-coordinate of the nurse's current position.
    - y (int): The y-coordinate of the nurse's current position.
    - charging_x (int): The x-coordinate of the charging station.
    - charging_y (int): The y-coordinate of the charging station.
    - inventory (list): The nurse's inventory, limited to one object for now.
    - battery (int): The nurse's battery level.
    - charging (bool): Indicates whether the nurse is currently charging.
    - charging_station (list): The coordinates of the charging station.
    - charging_time (int): The time spent charging.
    - status (str): The current status of the nurse.

    Methods:
    - nurse_charge_battery(): Charges the nurse's battery to 100%.
    - nurse_pick_object(object): Allows the nurse to pick up an object.
    - nurse_drop_object(object): Allows the nurse to drop an object.
    - manhattan_distance_to_owner(owner): Calculates the Manhattan distance between the nurse and an owner.
    """

    def __init__(self, name, x, y, charging_x=0, charging_y=0):
        """
        Initializes a Nurse object.

        Args:
            name (str): The name of the nurse.
            x (int): The x-coordinate of the nurse's position.
            y (int): The y-coordinate of the nurse's position.
            charging_x (int): The x-coordinate of the charging station's position.
            charging_y (int): The y-coordinate of the charging station's position.
        """
        super().__init__(name, x, y)
        self._inventory = []  # nurse's inventory, limited to one object for now
        self._battery = 100
        self._charging_status = 1
        self._charging_station = [charging_x,charging_y]
        self._charging_time = 0
        self._status = "Idle"

    @property
    def status(self):
        """
        Get the status of the nurse.

        Returns:
            str: The status of the nurse.
        """
        return self._status
    
    @property
    def battery(self):
        """
        Get the current battery status of the nurse.

        Returns:
            Tuple: A tuple containing the battery level, charging status, charging time, and charging station.
        """
        return self._battery, self._charging_status, self._charging_time, self._charging_station
    
    

    @status.setter
    def status(self, value):
        """Set the status of the nurse."""
        self._status = value

       
    @battery.setter
    def battery(self, value):
        """Set the battery level of the nurse."""
        self._battery = value

    def nurse_charge_battery(self):
        """
        Charges the nurse's battery to 100%.
        """
        self.charging = True
        self.charging_time = 0
        self.status = "Charging"
        self.battery = 100

    def nurse_pick_object(self, object):
        """
        Allows the nurse to pick up an object.

        Parameters:
        - object (Object): The object to be picked up.

        Returns:
        - bool: True if the nurse picks up the object successfully, False otherwise.
        """
        if self.x == object.x and self.y == object.y:
            self.inventory.append(object)
            return True
        else:
            return False

    def nurse_drop_object(self, object):
        """
        Allows the nurse to drop an object.

        Parameters:
        - object (Object): The object to be dropped.

        Returns:
        - bool: True if the nurse drops the object successfully, False otherwise.
        """
        return self.inventory.pop(0)

    def manhattan_distance_to_owner(self, owner):
        """
        Calculates the Manhattan distance between the nurse and an owner.

        Parameters:
        - owner (Owner): The owner to calculate the distance to.

        Returns:
        - int: The Manhattan distance between the nurse and the owner.
        """
        return self.heuristic((self.x,self.y), (owner.x,owner.y))


    def updateFromNotification(self, *new_state, **kwargs):
        return super().updateFromNotification(*new_state, **kwargs) # Call the parent class method
    

    def handle_event(self, event):
        """
        Handle an event.

        Args:
            event (Event): The event to handle.
        """
        if event.event_type == 'some_event_type':
            # Add logic for handling 'some_event_type'
            pass


