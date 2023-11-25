import sys
sys.path.insert(0, '.')

import tkinter as tk

import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import ConcreteObserver, Observer


class HouseModel:
    """
    Represents the model of the house environment.

    Includes the strucure of the house, the grid, objects...
    Those elements will be later represented.
    """

    OBJECTS = ("Air", "Door", "Fridge", "Sofa", "Table", "Wall")
    # Constant of Allowed Objects

    def __init__(self, grid:list) -> None:

        self.agents = dict()
        self.objects = dict()

        for row in grid:
            for elem in row: 
                if elem.literal_name in self.OBJECTS:
                    self.objects[elem] = [elem.x, elem.y]
                else: 
                    self.agents[elem] = [elem.x, elem.y]

class View(tk.Tk, ConcreteObserver):
    """ Create View to be Represented

    It generates the view, it inherits from ConcreteObserver (Observer Class).
    Depending on the following parameters, you can change the behaviour of the representation of the view
    """

    def __init__(self, name, matrix, height, width):

        tk.Tk.__init__(self)
        ConcreteObserver.__init__(self, name)

        self.model = HouseModel(matrix)

        self.height = height 
        self.width = width 
        self.CELL_SIZE = 40 
        self.title("Entorno Domótico")
        self.geometry(str(width) + "x" + str(height))  

        #It defines the srpites for each object's representation
        self.wall_image = tk.PhotoImage(file="./assets/sprites/wall.png")
        self.air_image = tk.PhotoImage(file="./assets/sprites/air.png")
        self.sofa_image = tk.PhotoImage(file="./assets/sprites/sofa.png")
        self.table_image = tk.PhotoImage(file="./assets/sprites/table.png")
        self.door_image = tk.PhotoImage(file="./assets/sprites/door.png")
        self.fridge_image = tk.PhotoImage(file="./assets/sprites/fridge.png")

        #Links the skins with the object literal name
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, #"Air": self.air_image, 
                          "Table": self.table_image, "Door": self.door_image, "Fridge": self.fridge_image}

        #Initialices the model with all the atributes
        self.canvas = tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(expand=True, fill='both')
        self.update_view() #Show view
        self.draw_grid(width, height) #Draw Grid
        self.attributes('-topmost', True) #Show Window on Top of other Windows



    # Override the ConcreteObserver's method for personalized logic
    def update(self, *new_state):
        print(f'{self.name} ha recibido una actualización: {new_state}')
        #Method of the action when you are notified by the subject of a modification

    def draw_grid(self, width:int, height:int):
        """
        Draws grid lines on the canvas.
        """
        
        for i in range(0, width, self.CELL_SIZE):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line', fill='grey')

        for i in range(0, height, self.CELL_SIZE):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line', fill='grey')
            

    def update_view(self):
        """
        Representents a new view

        Updates the view by clearing the canvas and redrawing objects based on the model.
        You can specify which objects you want to delete. For example, fixed objects like walls,
        do not need to be deleted and redrawn.
        """

        self.canvas.delete("agent", "object")
        
        # Draw the objects
        for object, matrix_pos in self.model.objects.items():

            img = self.img_dict.get(object.literal_name)
            
            # Paints the image of the object based on it's sprite PNG.
            self.canvas.create_image(
                object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
            )

        self.draw_grid(self.width, self.height)


# Ejemplo de uso
if __name__ == '__main__':

    height = 640
    width = 640


    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    view = View('view', room.matrix, height, width)

    view.mainloop()

# TODO PLACEHOLDERS, NO ELIMINAR, DAN UNA PLANTILLA PARA COMO CONTINUAR
"""
class Agent:

    Represents an agent in the environment.

    def __init__(self, name, position=(0, 0)):

        Initializes an Agent object.

        Parameters:
        - name (str): The name of the agent.
        - position (tuple): The initial position of the agent. Defaults to (0, 0).

        self.name = name
        self.position = position
        self.inventory = []

class Object:

    Represents an object in the environment.
    def __init__(self, name, position=(0, 0)):

        Initializes an Object object.

        Parameters:
        - name (str): The name of the object.
        - position (tuple): The initial position of the object. Defaults to (0, 0).

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

        Moves the specified agent to a new position.

        Parameters:
        - agent_name (str): The name of the agent to be moved.
        - new_position (tuple): The new position for the agent.

        Returns:
        - bool: True if the agent is moved successfully, False otherwise.

        if agent_name in self.agents:
            self.agents[agent_name].position = new_position
            return True
        return False

    def agent_pick_object(self, agent_name, object_name):

        Allows an agent to pick up an object.

        Parameters:
        - agent_name (str): The name of the agent.
        - object_name (str): The name of the object to be picked up.

        Returns:
        - bool: True if the agent picks up the object successfully, False otherwise.

        if agent_name in self.agents and object_name in self.objects:
            agent = self.agents[agent_name]
            obj = self.objects[object_name]
            if agent.position == obj.position:
                agent.inventory.append(obj)
                del self.objects[object_name]
                return True
        return False    
"""