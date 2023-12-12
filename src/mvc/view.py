import sys
sys.path.insert(0, '.')

import tkinter as tk
import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import Observer

class View(tk.Tk, Observer):
    """ Create View to be Represented

    It generates the view, inherits from Observer Class.
    Depending on the following parameters, you can change the behaviour of the representation of the view
    """


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
        self.gato_image = tk.PhotoImage(file="./assets/sprites/gato.png")
        self.jeizee_image = tk.PhotoImage(file="./assets/sprites/jeizee.png")
        

        #Links the skins with the object literal name
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, "Gato": self.gato_image, 
                          "Table": self.table_image, "Door_Closed": self.door_image, 
                          "Door_Open": self.door_open_image, "Fridge": self.fridge_image,
                          "Jeizee": self.jeizee_image}

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
    
    def update_self(self, *args, **kwargs):                   
        NOTIFY_KEYS = ('agents', 'matrix')

        for key, value in kwargs.items():
            if key not in NOTIFY_KEYS:
                raise KeyError(f"Invalid key: {key}")
            else:        
                match key:
                    case 'agents':
                        self.draw_agents(value)
                    case 'matrix':
                        self.draw_map(value)

                            
    def draw_map(self, map):
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
                    object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object")

        
        self.draw_grid(self.width, self.height)

    def draw_agents(self, agents):        
        # Draw the agents
        self.canvas.delete("agent")
        
        for agent in agents:
            img_agent = self.img_dict.get(agent.name)

            self.canvas.create_image(
                agent.x * 40, agent.y * 40, image=img_agent, anchor='nw', tags="agent"
            )
        
        # FIXME Poco óptimo, pero evita el bug visual de la grid solapando a los agentes
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
    import time
    from random import randint
    height = 640
    width = 640

    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)
    room.generate_agents(agent.Agent('Gato', 7, 7), agent.Agent('Jeizee', 5, 12))

    view = View('view', height, width)

    room.attach(view)
    
    delay = 1000
    time_after = 2000

    # Para ejecutar eventos cancelables, hay que devolver el id del evento para poder cancelar despues
    # Se pueden pasar argumentos a la funcion que se ejecuta en el after, 
    # pero hay que pasarlos como una funcion lambda
    def runtasks(i):
        room.notify(view, agents=room.agents, matrix=room.matrix)
        i += 1
        room.matrix[0][i] = 0
        id = view.after(delay, runtasks, i) 
        return id

    
    def start_moving():
        move1()
        view.after(delay, move2)

    def move1():
        room.move_object(7, 4, 8, 5)
        view.after(time_after, move1)

    def move2():
        room.move_object(8, 5, 7, 4)
        view.after(time_after, move2)

    def bailoteo_gatete():
        paso1()
        view.after(delay, paso2)

    def paso1():
        room.agents[0].x += 1
        room.agents[0].y -= 1
        view.draw_agents(room.agents)

        view.after(time_after, paso1)
        
    def paso2():
        room.agents[0].x -= 1
        room.agents[0].y += 1
        view.draw_agents(room.agents)

        view.after(time_after, paso2)

    def bailoteo_jeizee():
        paso3()
        view.after(delay, paso4)

    def paso3():
        room.agents[1].x += 1
        room.agents[1].y -= 1
        view.draw_agents(room.agents)

        view.after(time_after, paso3)
        
    def paso4():
        room.agents[1].x -= 1
        room.agents[1].y += 1
        view.draw_agents(room.agents)

        view.after(time_after, paso4)

    def shitty_draw(agentnumber):

        view.draw_agents(room.agents)
        room.agents[agentnumber].x += 1
        #room.agents[agentnumber].y += 1

        view.after(delay, shitty_draw, agentnumber)

    def delete_wall():
        if room.agents[0].x > 13:
            room.matrix[7][15] = 0
            room.notify(view, matrix=room.matrix)
        
        if room.agents[1].x > 13:
            room.matrix[12][15] = 0
            room.notify(view, matrix=room.matrix)

        view.after(100, delete_wall)

    task_id = runtasks(0)
    view.after_cancel(task_id)

    # TODO 

    # El bloque de código de arriba y el comentado hacen lo mismo a nivel funcional
    #view.after(0, room.notify(view, agents=room.agents, matrix=room.matrix))

    shitty_draw(0)
    shitty_draw(1)
    delete_wall()
    # FIXME PROBLEMA: cuando actualizamos objetos se envia toda la matriz:
    # si pilla a un agente encima de un objeto (p ej una puerta) pinta por encima!!!
    #start_moving()
    
    # OJO!!! funciones complejas como estas hacen que el programa vaya acumulando delays
    # y al final se dessincronizan los movimientos
    '''bailoteo_gatete()
    
    bailoteo_jeizee()'''
    

    # Start the main event loop
    view.mainloop()
