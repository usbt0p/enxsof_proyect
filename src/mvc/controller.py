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
    def __init__(self, model:Model, view:View) -> None:
        self.model = model
        self.view = view

        # Configurar la vista para usar este controlador
        self.view.set_controller(self)

    def move_agent(self, agent_name:str, new_position:tuple(int, int)) -> None:
        """
        Mueve un agente a una nueva posición y actualiza la vista.
        """
        if self.model.move_agent(agent_name, new_position):
            self.view.update_view()

    def add_agent(self, agent_name:str, position:tuple(int, int)) -> None:
        """
        Añade un nuevo agente al modelo y actualiza la vista.
        """
        self.model.add_agent(agent_name, position)
        self.view.update_view()

    def remove_agent(self, agent_name:str) -> None:
        """
        Elimina un agente del modelo y actualiza la vista.
        """
        self.model.remove_agent(agent_name)
        self.view.update_view()

    # Aquí puedes agregar más métodos según sea necesario

# Integración en el flujo principal del programa
if __name__ == '__main__':
    model = HouseModel()  # Suponiendo que HouseModel ya está definido
    view = HouseView(model)  # Suponiendo que HouseView ya está definido
    controller = HouseController(model, view)

    # Ejemplo de uso del controlador
    controller.move_agent('agent1', (5, 5))
    controller.add_agent('agent2', (2, 3))
    controller.remove_agent('agent1')

    view.mainloop()
