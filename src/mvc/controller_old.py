import sys
sys.path.insert(0, '.')

from model import Model
from view import View
from src.mvc.observer import ConcreteObserver

'''Para cuando haya que dibujar agentes:
Probablemente, lo mejor sea que los agentes estén en otra 'dimensión'
con respecto a los objetos: como en las capas de photoshop.
Así, solo hay que repintar esa capa y no los objetos, y tampoco hay que eliminar un objeto
cuando el agente se mueva a su casilla...
Simplemente habría que coger la coord a la que el agente se quiere mover en su mapa,
y ver las propiedades de colisión del obj en el otro mapa: ESTO SERÍA EL CONTROLADOR!!!'''

#TODO COMPLETAR CUANDO EL MODELO SEA DINÁMICO Y NO ESTÁTICO

class Controller(ConcreteObserver):


    """ 
    A controller class that acts as an observer to manage agents in the MVC architecture.
    It connects the model and view, handling user interactions and updating the view
    based on changes in the model.
    """

    def __init__(self, model, view):
        """
        Initializes the Controller with a model and a view.

        Args:
            model: The model part of the MVC architecture.
            view: The view part of the MVC architecture.
        """

        self.model = model
        self.view = view

        # Configure the view to use this controller.
        self.view.set_controller(self)

    def move_agent(self, agent_name:str, new_position:tuple(int, int)) -> None:
        """
        Moves an agent to a new position and updates the view.

        Args:
            agent_name: The name of the agent to be moved.
            new_position: The new position to move the agent to.
        """
        if self.model.move_agent(agent_name, new_position):
            self.view.update_view()

    def add_agent(self, agent_name:str, position:tuple(int, int)) -> None:
        """
        Adds a new agent to the model and updates the view.

        Args:
            agent_name: The name of the agent to be added.
            position: The position to place the new agent.
        """
        self.model.add_agent(agent_name, position)
        self.view.update_view()

    def remove_agent(self, agent_name:str) -> None:
        """
        Removes an agent from the model and updates the view.

        Args:
            agent_name: The name of the agent to be removed.
        """
        self.model.remove_agent(agent_name)
        self.view.update_view()

    # Additional methods can be added here as needed.

# Main program flow integration
if __name__ == '__main__':
    model = HouseModel()  # Assuming HouseModel is already defined.
    view = HouseView(model)  # Assuming HouseView is already defined.
    controller = HouseController(model, view)

    # Example usage of the controller
    controller.move_agent('agent1', (5, 5))
    controller.add_agent('agent2', (2, 3))
    controller.remove_agent('agent1')

    view.mainloop()


# TODO PLACEHOLDERS, NO ELIMINAR, DAN UNA PLANTILLA PARA COMO CONTINUAR
'''
class Agent:
    """
    Represents an agent in the environment.
    """
    def __init__(self, name, position=(0, 0)):
        """
        Initializes an Agent object.
        Parameters:
        - name (str): The name of the agent.
        - position (tuple): The initial position of the agent. Defaults to (0, 0).
        """
        self.name = name
        self.position = position
        self.inventory = []
class Object:
    """
    Represents an object in the environment.
    """
    def __init__(self, name, position=(0, 0)):
        """
        Initializes an Object object.
        Parameters:
        - name (str): The name of the object.
        - position (tuple): The initial position of the object. Defaults to (0, 0).
        """
        self.name = name
        self.position = position
class HouseModel:
    def __init__(self):
        self.agents = {
            'robot': Agent('robot', position=(0, 0)),
            'human': Agent('human', position=(0, 0))
        }
        self.objects = {
            'beer': Object('beer', position=(0, 0)),
            'medkit': Object('medkit', position=(0, 0))
        }
        
        
    def move_agent(self, agent_name, new_position):
        """
        Moves the specified agent to a new position.
        Parameters:
        - agent_name (str): The name of the agent to be moved.
        - new_position (tuple): The new position for the agent.
        Returns:
        - bool: True if the agent is moved successfully, False otherwise.
        """
        if agent_name in self.agents:
            self.agents[agent_name].position = new_position
            return True
        return False
    def agent_pick_object(self, agent_name, object_name):
        """
        Allows an agent to pick up an object.
        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.
        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.
        """
        if agent_name in self.agents and object_name in self.objects:
            agent = self.agents[agent_name]
            obj = self.objects[object_name]
            if agent.position == obj.position:
                agent.inventory.append(obj)
                del self.objects[object_name]
                return True
        return False    
        
    def animate_movement(self, movements, index=0):
        if index < len(movements):
            pos = movements[index]
            self.model.move_agent('robot', pos)
            self.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.after(1000, lambda: self.animate_movement(movements, index + 1))
        
class View(tk.Tk, ConcreteObserver):
        
    def animate_movement(self, movements, index=0):
        """
        Animates the movement of the agent in the view.
        Parameters:
        - movements (list): List of tuples representing the agent's movements.
        - index (int): Index to keep track of the current movement. Defaults to 0.
        """
        if index < len(movements):
            pos = movements[index]
            self.model.move_agent('robot', pos)
            self.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.after(1000, lambda: self.animate_movement(movements, index + 1))




    if __name__ == '__main__':
    model = HouseModel()
    view = HouseView(model)

    # Movimientos de prueba
    movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
    # Inicia la animación después de un segundo
    view.after(1000, lambda: view.animate_movement(movements))

    view.mainloop()

    
    '''