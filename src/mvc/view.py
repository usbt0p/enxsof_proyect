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

        button1 = tk.Button(frame, text="Movement Test (16x16)", command=self.button1_clicked)
        button1.grid(row=0, column=0, sticky='nsew')

        button2 = tk.Button(frame, text="Collision Test (16x16)", command=self.button2_clicked)
        button2.grid(row=0, column=1, sticky='nsew')

        button3 = tk.Button(frame, text="Door Test (16x16 Room Size ONLY)", command=self.button3_clicked)
        button3.grid(row=0, column=2, sticky='nsew')

        # Configure the columns to distribute extra space equally
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)




        #It defines the srpites for each object's representation
        self.wall_image = tk.PhotoImage(file="./assets/sprites/wall.png")
        self.air_image = tk.PhotoImage(file="./assets/sprites/air.png")
        self.sofa_image = tk.PhotoImage(file="./assets/sprites/sofa.png")
        self.table_image = tk.PhotoImage(file="./assets/sprites/table.png")
        self.door_image = tk.PhotoImage(file="./assets/sprites/door.png")
        self.door_open_image = tk.PhotoImage(file="./assets/sprites/door_open.png")
        self.fridge_image = tk.PhotoImage(file="./assets/sprites/fridge.png")
        self.agent_image = tk.PhotoImage(file="./assets/sprites/gato.png")
        

        #Links the skins with the object literal name
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, "Gato": self.agent_image, 
                          "Table": self.table_image, "Door_Closed": self.door_image, 
                          "Door_Open": self.door_open_image, "Fridge": self.fridge_image}

        #Initialices the model with all the atributes
        self.canvas = tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(expand=True, fill='both')
        self.update_view() #Show view
        self.draw_grid(width, height) #Draw Grid
        self.attributes('-topmost', True) #Show Window on Top of other Windows




    def resize_window(self):
        """
        Resizes the window to fit the required width and height.
        """
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
        """
        Set the controller for the view.

        Parameters:
        - controller: The controller object to be set.

        Returns:
        None
        """
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

            if object.literal_name != "Door":
                img = self.img_dict.get(object.literal_name)
            else:
                if object.isOpen:
                    img = self.img_dict.get("Door_Open")
                elif object.isOpen == False:
                    img = self.img_dict.get("Door_Closed")
            
            # Paints the image of the object based on it's sprite PNG.
            self.canvas.create_image(
                object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
            )

        # Draw the agents
        
        for agent in self.agents_list:

            img_agent = self.img_dict.get(agent.name)

           
            self.canvas.create_image(
                agent.x * 40, agent.y * 40, image=img_agent, anchor='nw', tags="agent"
            )

        self.draw_grid(self.width, self.height)


    def button1_clicked(self):
        """
        Handle the click event for button1.

        If a controller is available, call its handle_click method with the argument "movement".
        """
        if self.controller:
            self.controller.handle_click("movement")

    def button2_clicked(self):
        """
        Handle the click event for button2.

        If a controller is set, call its handle_click method with the argument "collision".
        """
        if self.controller:
            self.controller.handle_click("collision")

    def button3_clicked(self):
        """
        Handle the click event for button3.

        If a controller is available, call its handle_click method with the argument "door".
        """
        if self.controller:
            self.controller.handle_click("door")



# Ejemplo de uso
if __name__ == '__main__':

    height = 640
    width = 640

    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    view = View('view', room.matrix,[], height, width)
    #view.mainloop()




    frame = tk.Frame(view)
    frame.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(frame, text="Button")
    button.pack(fill=tk.BOTH, expand=True)



    

    # Start the main event loop
    view.mainloop()
