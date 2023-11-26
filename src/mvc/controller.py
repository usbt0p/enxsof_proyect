import sys
sys.path.insert(0, '.')

import threading
import tkinter as tk
import src.mvc.model as model
import src.mvc.view as view
from src.mvc.observer import Observer


class Controller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        self.model.attach(self)
        self.model.attach(self.view)
        

        # Start a thread for handling terminal inputs
       # threading.Thread(target=self.handle_terminal_input, daemon=True).start()

    """
    def handle_terminal_input(self):
        while True:
            user_input = input("Enter commands as requested: ")
            # Process the input and update model or view
            self.process_input(user_input)

    def process_input(self, user_input):
        # Implement logic based on input
        if user_input == 'open door':
            # Example: Update model and view
            self.model.open_door()  # Assuming this method exists in the model
            # Schedule a GUI update in the main thread
            self.view.after(0, self.view.update_view)  # Assuming update_view method in view
            """
    
    def update_observer(self, *new_state):
        
        self.view.after(0, self.view.update_view)


    def add_agent(self, agent_name:str, position:tuple) -> None:
        """
        Adds a new agent to the model and updates the view.

        Args:
            agent_name: The name of the agent to be added.
            position: The position to place the new agent.
        """
        new_agent = self.model.generate_agents(agent_name, position)
        self.model.add_agent(new_agent)
        self.view.update_view()


    def remove_agent(self, agent_name:str) -> None:
        """
        Removes an agent from the model and updates the view.

        Args:
            agent_name: The name of the agent to be removed.
        """
        self.model.remove_agent(agent_name)
        self.view.update_view()

        

    def move_agent(self, agent, new_position) -> None:
        """
        Moves an agent to a new position and updates the view.

        Args:
            agent_name: The name of the agent to be moved.
            new_position: The new position to move the agent to.
        """
        agent.position(new_position)

    def animate_movement(self, agent, movements, index=0):
        if index < len(movements):
            pos = movements[index]
            self.move_agent(agent, pos)
            self.view.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.view.after(1000, lambda: self.animate_movement(agent, movements, index + 1))
    

    def handle_click(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.test_movement(self.model.agents[0])


    def test_movement(self, agent):
        movements = [[1,1],[2,2],[3,3],[4,4],[5,5],[5,4]]
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement(agent, movements))
    # Other controller methods to interact with model and view
    # ...

# Usage example (ensure that model and view are correctly instantiated)


