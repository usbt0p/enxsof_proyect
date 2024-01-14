import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning
from utiles.objects.mixed import Mixed

class Waiter(Agent, Observer, pathPlanning):

    def __init__(self, name:str, x:int, y:int) -> None:
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
    def status(self) -> str:
        """
        Get the status of the waiter.

        Returns:
            str: The status of the waiter.
        """
        return self._status
    
    @status.setter
    def status(self, value) -> None:
        """Set the status of the waiter."""
        self._status = value


    def updateFromNotification(self, *new_state:tuple, **kwargs:dict) -> None:
        return super().updateFromNotification(*new_state, **kwargs) # Call the parent class method
    

    def handle_event(self, event, controller) -> None:
        """
        Specific event handling for Waiter.
        Overrides the default implementation.
        """
        if event.event_type == 'random_move':
            index = controller.model.agents.index(self)
            while path == False or path == None or path == []: #No hay camino / el destino no es valido / Origen == Destino
                path = controller.model.path_generator(index)
                controller.move_randomly(path, index, path[0])

        elif event.event_type == 'delivery_pickup':
            path = self.a_star_search((self.x, self.y), event.data, controller.model.matrix) # (self, start, goal, grid)
            index = controller.model.agents.index(self)
            controller.concrete_move(path, index, path[0])


        # Check for 'check_stock' event
        elif event.event_type == 'check_stock':

            enough_stock = True

            # Initialize a set to store objects with their positions
            stock_to_check = set()

            # Iterate through the matrix to find objects of type 'Mixed'
            for i, row in enumerate(controller.model.matrix):
                for j, element in enumerate(row):
                    # Check if the element is an instance of 'Mixed'
                    if isinstance(element, Mixed):
                        # Create a dictionary with the element and its position
                        element_with_position = {'object': element, 'position': (i, j)}
                        # Add the dictionary to the set
                        stock_to_check.add(element_with_position)

            # Iterate over the set while it has elements
            while stock_to_check:
                # Remove and select a dictionary from the set
                selected_item = stock_to_check.pop()
                # Retrieve the object and its position from the dictionary
                selected_object = selected_item['object']
                position = selected_item['position']

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
                        if selected_object.storage['stock'] < 5:
                            enough_stock = False
                        #TODO ADD STOCK

            #Order a delivery
            if not enough_stock:
                controller.trigger_delivery(controller)

        elif event.event_type == 'low_battery':
            # Find charger
            # Iterate through each row and column in the matrix
            for i, row in enumerate(controller.model.matrix):
                for j, element in enumerate(row):
                    # Check if the element has the 'name' attribute
                    if hasattr(element, 'name'):
                    # Check if the 'name' attribute matches the target name
                        if element.name == target_name: #TODO: Change target_name
                            # Return the position of the element
                            position = (i, j)
                            
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