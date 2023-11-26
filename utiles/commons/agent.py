import sys
sys.path.insert(0, '.')

from src.mvc.subject import Subject

# TODO implementar lógica de envío de notificación desde agente hasta el controlador
# TODO implementar lógica en el controlador para comprobar si la notif. de movimiento es válida
# TODO si es válida, mandar el movimiento aceptado por el controlador al modelo
# TODO implementar lógica de la notificación del modelo cuando detecta el cambio en el agente
# TODO pintar el agente en la vista una vez esta reciba la notificación

class Agent(Subject):
    """
    Represents an agent in the environment.
    """

    def __init__(self, name, x=0, y=0):
        """
        Initializes an Agent object.
        Parameters:
        - name (str): The name of the agent.
        - position (tuple): The initial position of the agent. Defaults to (0, 0).
        """
        self.name = name
        self.inventory = []
        self.x = x
        self.y = y

    def print_position(self):
        print(f"({self.x}, {self.y})")

    def position(self, position):
        print(f"Agent {self.name} moved to {position}")
        # Se podría mandar una notif a controller para que compruebe si el movimiento es válido
        # self.notify()
        self.x = position[0]
        self.y = position[1]
        


    def move_agent(self, new_position):
        """
        Moves the specified agent to a new position.
        Parameters:
        - agent_name (str): The name of the agent to be moved.
        - new_position (tuple): The new position for the agent.
        Returns:
        - bool: True if the agent is moved successfully, False otherwise.
        """
        # TODO pathplanning algorithms
        
        self.position(new_position)

    def __str__(self) -> str:
        return f"Agent: {self.name} at position {self.position}"


    #TODO: A COMPLETAR EN EL FUUTURO
    
    """ 
    def agent_pick_object(self, agent_name, object_name):
        
        '''
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        '''

        if agent_name in self.agents and object_name in self.objects:
            agent = self.agents[agent_name]
            obj = self.objects[object_name]
            if agent.position == obj.position:
                agent.inventory.append(obj)
                del self.objects[object_name]
                return True
        return False    
    """
        
    def animate_movement(self, movements, index=0):
        if index < len(movements):
            pos = movements[index]
            self.move_agent('robot', pos)
            self.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.after(1000, lambda: self.animate_movement(movements, index + 1))
 

