import sys
sys.path.insert(0, '.')

import tkinter as tk
import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import Observer



class View(tk.Tk, Observer):

    def __init__(self, name, height, width): # matrix, agent_list, 

        tk.Tk.__init__(self)
        Observer.__init__(self, name)

    
        self.controller = None

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

        """
        button1 = tk.Button(frame, text="Movement Test (16x16)", command=self.button1_clicked)
        button1.grid(row=0, column=0, sticky='nsew')

        button2 = tk.Button(frame, text="Collision Test (16x16)", command=self.button2_clicked)
        button2.grid(row=0, column=1, sticky='nsew')

        button3 = tk.Button(frame, text="Door Test (16x16 Room Size ONLY)", command=self.button3_clicked)
        button3.grid(row=0, column=2, sticky='nsew')
        """

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
        self.canvas= tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(expand=True, fill='both')

        self.update() #Show view
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

    
    def updateFromNotification(self, *args, **kwargs):
        """
        Update the view based on the notification.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if kwargs['matrix']:
            
            self.draw_map(kwargs['matrix'])

        if kwargs['agents']:
            self.draw_agents(kwargs['agents'])

                            
    def draw_map(self, map, grid = True):
        """
        Representents a new view

        Updates the view by clearing the canvas and redrawing objects based on the model.
        You can specify which objects you want to delete. For example, fixed objects like walls,
        do not need to be deleted and redrawn.
        """

        
        self.canvas.delete("object")
        
        # Draw the objects
        for row in map:
            for object in row:
                if object == 0:
                    continue
                elif object.literal_name != "Door":
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

        if grid:
            self.draw_grid(self.width, self.height)

    def draw_agents(self, agents):
        
        # Draw the agents
        self.canvas.delete("agent")
        
        for agent in agents:
            img_agent = self.img_dict.get(agent.name)

           
            self.canvas.create_image(
                agent.x * 40, agent.y * 40, image=img_agent, anchor='nw', tags="agent"
            )

'''
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
'''



# Ejemplo de uso
if __name__ == '__main__':

    height = 640
    width = 640

    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    gato = agent.Agent("Gato", 7, 7)
    room.generate_agents(gato)

    view = View('view', height, width)

    room.attach(view)
    
    def runtasks():
        room.notify(view, agents=room.agents, matrix=room.matrix)

        view.after(1000, runtasks) 

    
    runtasks()

    # Start the main event loop
    view.mainloop()
    