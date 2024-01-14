import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
from utiles.agents.agent import Agent
from utiles.commons.movementSystem import pathPlanning
from utiles.objects import mixed

import functools

class Delivery(Agent, Observer, pathPlanning):

    def __init__(self, name, x, y, animation_speed=1000):
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
        self.animation_speed = animation_speed


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
    

    def on_movement_complete(self, controller):
            box = mixed.Mixed(self.x, self.y, 'Box', {'medicinas': 3, 'cervezas': 17})
            controller.add_object(box, self.x, self.y)

    def on_delivery_complete(self, controller):
            self.status = "Idle"
            # Schedule the removal of the agent to allow the animation to complete
            controller.view.after(self.animation_speed, lambda: controller.remove_agent(self.name))
            #controller.remove_agent(self.name)
    

    def handle_event(self, event, controller):
        """
        Specific event handling for Delivery.
        Overrides the default implementation.
        """

        if event.event_type == 'delivery':
            origin = (self.x, self.y)
            print(origin)
            print(event.data)
            path = self.a_star_search((self.x, self.y), event.data, controller.model.matrix, True) # (self, start, goal, grid, stop_before_target)
            print(path)
            if path:
                self.status = "Delivering"
                index = controller.model.agents.index(self)
                controller.concrete_move(path, index, path[0],functools.partial(self.on_movement_complete, controller))
                #box = mixed.Mixed(self.x, self.y, 'Box', {'medicinas': 3, 'cervezas': 17})
                #controller.add_object(box, self.x, self.y)
                
            if origin != (self.x, self.y):   
                path = self.a_star_search((self.x, self.y), origin, controller.model.matrix, False) # (self, start, goal, grid, stop_before_target)
                if path:
                    self.status = "Moving"
                    index = controller.model.agents.index(self)
                    controller.concrete_move(path, index, path[0], functools.partial(self.on_delivery_complete, controller))
                    #self.status = "Idle"
                    #controller.remove_agent(self.name)
            else:
                self.status = "Idle"
                controller.remove_agent(self.name) 

        else:
            # Call the default implementation for unhandled cases
            super().handle_event(event)