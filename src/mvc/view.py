import sys
sys.path.insert(0, '.')

import tkinter as tk
import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import Observer


class HouseModel:
    """
    Represents the model of the house environment.

    Includes the strucure of the house, the grid, objects...
    Those elements will be later represented.
    """

    OBJECTS = ("Air", "Door", "Fridge", "Sofa", "Table", "Wall")
    # Constant of Allowed Objects

    def __init__(self, model) -> None:

        self.objects = dict()

        for row in model:
            for elem in row: 
                if elem.literal_name in self.OBJECTS:
                    self.objects[elem] = [elem.x, elem.y]



class View(tk.Tk, Observer):
    """ Create View to be Represented

    It generates the view, it inherits from ConcreteObserver (Observer Class).
    Depending on the following parameters, you can change the behaviour of the representation of the view
    """


    def __init__(self, name, matrix, agent_list, height, width):

        tk.Tk.__init__(self)
        Observer.__init__(self, name)

        def handle_click(event):
            print("Button clicked!")
            self.controller.handle_click()

        self.controller = None

        self.house_model = HouseModel(matrix)
        self.agents_list = agent_list

        self.height = height
        self.min_height = height 
        self.width = width
        self.min_width = width 
        self.CELL_SIZE = 40 
        self.title("Entorno Domótico")
        self.geometry(str(width) + "x" + str(height+30))
        self.minsize(self.min_width, self.min_height)

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        button = tk.Button(frame, text="Button")
        button.pack(fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", handle_click)

        """
        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        button = tk.Button(frame, text="TEST MOVIMIENTO")
        button.pack(fill=tk.BOTH, expand=True)

        button.bind("<Button-1>", self.handle_click("movement"))
        """


        #It defines the srpites for each object's representation
        self.wall_image = tk.PhotoImage(file="./assets/sprites/wall.png")
        self.air_image = tk.PhotoImage(file="./assets/sprites/air.png")
        self.sofa_image = tk.PhotoImage(file="./assets/sprites/sofa.png")
        self.table_image = tk.PhotoImage(file="./assets/sprites/table.png")
        self.door_image = tk.PhotoImage(file="./assets/sprites/door.png")
        self.fridge_image = tk.PhotoImage(file="./assets/sprites/fridge.png")
        self.agent_image = tk.PhotoImage(file="./assets/sprites/gato.png")

        #Links the skins with the object literal name
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, "Gato": self.agent_image, 
                          "Table": self.table_image, "Door": self.door_image, "Fridge": self.fridge_image}

        #Initialices the model with all the atributes
        self.canvas = tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(expand=True, fill='both')
        self.update_view() #Show view
        self.draw_grid(width, height) #Draw Grid
        self.attributes('-topmost', True) #Show Window on Top of other Windows


    


    """   
    def handle_click(self, event):
        print("Button clicked!")
        if self.controller:
            self.controller.handle_click(event)
    """

    def resize_window(self):
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        self.geometry(f"{width}x{height+30}")
        self.minsize(self.min_width, self.min_height) 



    # Override the ConcreteObserver's method for personalized logic
    def notify(self, *new_state):
        print(f'{self.name} ha recibido una actualización: {new_state}')
        self.update_view(self)
        #Method of the action when you are notified by the subject of a modification

    def set_controller(self, controller):
        self.controller = controller

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
        for object, matrix_pos in self.house_model.objects.items():

            img = self.img_dict.get(object.literal_name)
            
            # Paints the image of the object based on it's sprite PNG.
            self.canvas.create_image(
                object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
            )

        # Dibuja los agentes
        
        for agent in self.agents_list:

            img_agent = self.img_dict.get(agent.name)

           
            self.canvas.create_image(
                agent.x * 40, agent.y * 40, image=img_agent, anchor='nw', tags="agent"
            )

        self.draw_grid(self.width, self.height)





# Ejemplo de uso
if __name__ == '__main__':

    height = 640
    width = 640

    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    view = View('view', room.matrix,[], height, width)
    #view.mainloop()

    #AÑADIR BOTONES
     
    # Define the handle_click function
    #def handle_click(event):
    #    print("Button clicked!")


    frame = tk.Frame(view)
    frame.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(frame, text="Button")
    button.pack(fill=tk.BOTH, expand=True)

    # Create a button
    # button = tk.Button(view, text="Click Me")
    # button.pack(fill=tk.BOTH, expand=True)

    # Bind the button's click event to the handle_click function
    button.bind("<Button-1>", handle_click)

    """
    movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
    # Inicia la animación después de un segundo
    view.after(1000, lambda: view.animate_movement(movements))
    """

    

    # Start the main event loop
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