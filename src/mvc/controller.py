import sys
sys.path.insert(0, '.')

import threading
import tkinter as tk
import src.mvc.model as model
import src.mvc.view as view
from src.mvc.observer import Observer
import time



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

    def animate_movement_collision(self, agent, movements, index=0):
        agent.x = 1
        agent.y = 1
        if index < len(movements):
            pos = movements[index]
            eval_object = self.model.is_position_occupied(pos)
            # If the new position is occupied, stop the animation
            if ((not eval_object.interactive) and eval_object.movable and eval_object.literal_name != "Air"):
                print("\nI can maybe try to move this obstacle... but I'm not sure if I can do it alone, I'm just a cat!")
                return
            elif ((eval_object.interactive) and (eval_object.movable)):
                print("\nI like to jump on the sofa!\n")
            elif ((eval_object.collision) and not (eval_object.movable)):
                print("\nOoops! It looks like there is an obstacle in the way!\n")
                return
                    
            self.move_agent(agent, pos)
            self.view.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.view.after(1000, lambda: self.animate_movement_collision(agent, movements, index + 1))

    def animate_door(self, agent, movements, index=0):
        agent.x = 5
        agent.y = 3
        if index < len(movements):
            pos = movements[index]
            eval_object = self.model.is_position_occupied(pos)
            if (eval_object.interactive) and not(eval_object.movable) and not(eval_object.collision):
                if eval_object.isOpen:
                    eval_object.close()
                    print("\nI'm closing the door\n")
                    time.sleep(1)

                elif not(eval_object.isOpen):
                    eval_object.open()
                    print("\nI'm opening the door\n")
                    time.sleep(1)

            self.move_agent(agent, pos)
            self.view.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.view.after(1000, lambda: self.animate_door(agent, movements, index + 1))
    

    def handle_click(self, event):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if event == "movement":
            self.test_movement(self.model.agents[0])
        elif event == "collision":
            self.test_collision(self.model.agents[0])
        elif event == "door":
            self.test_door(self.model.agents[0])


    def test_movement(self, agent):
        movements = [[1,1],[2,2],[3,3],[4,4],[5,5],[5,4]]
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement(agent, movements))

    def test_collision(self, agent):
        movements = [[1,1],[2,2],[3,3],[4,4],[5,5],[5,4]]
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement_collision(agent, movements))

    def test_door(self, agent):
        movements = [[5,3],[5,4],[5,5],[5,6],[5,7],[5,8]]
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement_collision(agent, movements))




