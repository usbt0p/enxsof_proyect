import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
import time
import random


class Controller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        self.model.attach(self.view)
        self.model.attach(self)
        

        self.animation_running = False
        self.animation_id = None
        self.previous_event = None
    
    
    def updateFromNotification(self, *new_state, **kwargs):
        NOTIFY_KEYS = ('agent_move_right', 'random_movement')
        print(kwargs)
        for key, value in kwargs.items():
            if key not in NOTIFY_KEYS:
                raise KeyError(f"Invalid key: {key}")
            else:        
                match key:
                    case 'agent_move_right':
                        self.model.agent_move_right(value)
                    case 'random_movement':
                        # random movement necesita el indice del agente (del que luego se saca su posicion)
                        path = self.model.path_generator(value)
                        self.move_randomly(path, value)


    def move_randomly(self, path, agent_index):
        print(self.model.agents)
        print(path)
        self.model.agents[agent_index].x = path[0][0]
        self.model.agents[agent_index].y = path[0][1]

        self.model.notify(self.view, agents=self.model.agents)
        if path != []:
            id = self.view.after(1000, self.move_randomly, path[1:], agent_index) 
            return id
        

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

        

   





