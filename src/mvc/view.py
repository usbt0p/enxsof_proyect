import tkinter as tk
import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import ConcreteObserver, Observer
#from icecream import ic

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
        }'''
    
class HouseModel:
    """
    Represents the model of the house environment.
    """

    OBJECTS = ("Air", "Door", "Fridge", "Sofa", "Table", "Wall")

    def __init__(self, grid) -> None:
        """
        Initializes a HouseModel object.

        Parameters:
        - grid (list): The grid representing the environment.
        """
        self.agents = dict()
        self.objects = dict()
        # la comento pq no creo q nos interese almacenarla 2 veces en memoria pero no se
        #self.grid = grid  

        for row in grid:
            for elem in row: 
                if elem.literal_name in self.OBJECTS:
                    
                    self.objects[elem] = [elem.x, elem.y]
                else: 
                    self.agents[elem] = [elem.x, elem.y]

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

# Definición de la Vista
class View(tk.Tk, ConcreteObserver):

    def __init__(self, name, matrix, height, width):

        # Recibe los métodos y atributos de ConcreteObserver y de tk.Tk
        # con super().__init__(name) no funciona, busca en tk.Tk el atributo name y no lo encuentra,
        # y por alguna razón no ejecuta el arbol de busqueda para encontrarlo en ConcreteObserver????
        tk.Tk.__init__(self)
        ConcreteObserver.__init__(self, name)

        ''' /!\ ATENCIÓN /!\\
        - Si vas a trabajar en cambiar esta clase, ten en cuenta que sus comportamientos dependen de
            la siguiente linea!!!
            self.model es una referencia al modelo, después de procesarlo llamando a HouseModel, que
            se encarga de procesar, encontrar y almacenar objetos, agentes, etc. para hacer el display
        '''
        self.model = HouseModel(matrix) 

        self.height = height
        self.width = width
        self.CELL_SIZE = 40
        self.title("Entorno Domótico")
        self.geometry(str(width) + "x" + str(height))  # Tamaño de la ventana

        # Establece las skins
        # TODO se puede hacer más modular??
        self.wall_image = tk.PhotoImage(file="./assets/sprites/wall.png")
        self.air_image = tk.PhotoImage(file="./assets/sprites/air.png")
        self.sofa_image = tk.PhotoImage(file="./assets/sprites/sofa.png")
        self.table_image = tk.PhotoImage(file="./assets/sprites/table.png")
        self.door_image = tk.PhotoImage(file="./assets/sprites/door.png")
        self.fridge_image = tk.PhotoImage(file="./assets/sprites/fridge.png")

        #Asigna las skins a los literales de cada objeto
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, #"Air": self.air_image, 
                          "Table": self.table_image, "Door": self.door_image, "Fridge": self.fridge_image}

        #Inicializa el modelo con todos los atributos listos
        self.canvas = tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack()
        self.update_view() 
        self.draw_grid(width, height)

    # Override the ConcreteObserver's method for personalized logic
    def update(self, *new_state):
        print(f'{self.name} ha recibido una actualización: {new_state}')

    def draw_grid(self, width, height):
        """
        Draws grid lines on the canvas.
    
        Parameters:
        - width (int): The width of the canvas.
        - height (int): The height of the canvas.
        """
        for i in range(0, width, self.CELL_SIZE):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line', fill='grey')

        for i in range(0, height, self.CELL_SIZE):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line', fill='grey')
            

    def update_view(self):
        """
        Updates the view by clearing the canvas and redrawing objects based on the model.
        """
        self.canvas.delete("agent", "object")
        # Dibuja los agentes
        '''for agent_name, agent in self.model.agents.items():
            x, y = agent.position
            self.canvas.create_image(
                x * 40, y * 40, image=self.object_image, anchor='nw', tags="agent"
            )'''
        
        
        # Dibuja los objetos
        for object, matrix_pos in self.model.objects.items():
            
            # Que hace esto???
            #object.x, object.y = matrix_pos.position
            #ic(object.x, object.y)

            # TODO añadir lógica: si objeto ya ha sido dibujado, no dibujar

            img = self.img_dict.get(object.literal_name)
            
            # TODO añadir ruta de imagen a objetos???
            self.canvas.create_image(
                object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
            )

        self.draw_grid(self.width, self.height)

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


# Ejemplo de uso
if __name__ == '__main__':

    height = 640
    width = 640


    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    view = View('view', room.matrix, height, width)

    # Movimientos de prueba
    movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
    # Inicia la animación después de un segundo
    view.after(1000, lambda: view.animate_movement(movements))

    view.mainloop()

