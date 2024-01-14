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
    

    def handle_event(self, event, controller):
        """
        Specific event handling for Nurse.
        Overrides the default implementation.
        """
        if event.event_type == 'follow_owner':

            radius = 5  # The radius in which the nurse will follow the owner

        # Continuously follow the moving target
            while True:
                # Calculate the current distance to the target
                distance_to_target = self.heuristic((self.x, self.y), (event.data.x, event.data.y))

                # Check if within the desired radius
                if distance_to_target <= radius:
                    # Optional: Adjust position within the radius or perform other actions
                    break

                # Get the current position of the target
                target_position = (event.data.x, event.data.y)

                # Calculate the path to the new target position
                path = self.a_star_search((self.x, self.y), target_position, controller.model.matrix, True)

                # If a path is found, move along the path
                if path:
                    index = controller.model.agents.index(self)
                    controller.concrete_move(path, index, path[0])
                
                # Optional: Wait or perform other tasks before recalculating
                # time.sleep(...) or other actions

                # Optional: Conditions to break the loop, like a stop command or target reached

        elif event.event_type == 'low_battery':
            # Find charger
            found = False
            # Iterate through each row and column in the matrix
            for i, row in enumerate(controller.model.matrix):
                for j, element in enumerate(row):
                    # Check if the element has the 'name' attribute
                    if hasattr(element, 'name'):
                    # Check if the 'name' attribute matches the target name
                        if element.name == target_name: #TODO: Change target_name
                            # Return the position of the element
                            position = (i, j)
                            found = True
                            break
                if found:
                    break
                            
            # Check if a valid position was found
                if position:
                    # Calculate the path to the object's position, stopping one cell before
                    path = self.a_star_search((self.x, self.y), position, controller.model.matrix, True)
                    # Check if a valid path was found
                    if path:
                        # Find the index of the current agent in the list of agents
                        index = controller.model.agents.index(self)
                        # Move the agent along the calculated path
                        controller.concrete_move(path, index, path[0])

        else:
            # Call the default implementation for unhandled cases
            super().handle_event(event)


