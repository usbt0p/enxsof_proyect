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
<<<<<<< HEAD
    def __init__(self, model:Model, view:View) -> None:
=======
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
>>>>>>> 1ae9fb2479e3de79204a88de5a4a874e97f56801
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
