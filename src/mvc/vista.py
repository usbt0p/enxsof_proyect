import tkinter as tk
import model
from utiles.commons import *
from icecream import ic

# Definición del Modelo
class Agent:
    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.position = position
        self.inventory = []

class Object:
    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.position = position

    '''class HouseModel:
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

    OBJECTS = ("Air", "Door", "Fridge", "Sofa", "Table", "Wall")

    def __init__(self, grid) -> None:
        self.agents = dict()
        self.objects = dict()
        self.grid = grid

        for row in grid:
            for elem in row: 
                if elem.literal_name in self.OBJECTS:
                    
                    self.objects[elem] = [elem.x, elem.y]
                else: 
                    self.agents[elem] = [elem.x, elem.y]

    def move_agent(self, agent_name, new_position):
        if agent_name in self.agents:
            self.agents[agent_name].position = new_position
            return True
        return False

    def agent_pick_object(self, agent_name, object_name):
        if agent_name in self.agents and object_name in self.objects:
            agent = self.agents[agent_name]
            obj = self.objects[object_name]
            if agent.position == obj.position:
                agent.inventory.append(obj)
                del self.objects[object_name]
                return True
        return False

# Definición de la Vista
class HouseView(tk.Tk):
    def __init__(self, model : HouseModel, height, width):
        super().__init__()
        self.model = model  # Referencia al modelo
        self.height = height
        self.width = width
        self.title("Entorno Domótico")
        self.geometry(str(height) + "x" + str(width))  # Tamaño de la ventana

        # TODO hacer como en esta
        #self.wall_image = tk.PhotoImage(file="./src/room/wall.png")
        self.wall_image = tk.PhotoImage(file="./assets/gato.png")
        self.object_image = tk.PhotoImage(file="./assets/gato.png")
        self.air_image = tk.PhotoImage(file="./assets/gato.png")
        self.img_dict = {"Wall": self.wall_image, "Air": self.air_image}

        # TODO si se puede meter variables aqui (numfilas * 40, nucol * 40)
        self.canvas = tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack()

        self.draw_grid(width, height)
        self.update_view()  # Actualiza la vista con el estado inicial del modelo

    def draw_grid(self, width, height):
        for i in range(0, height, 40): # FIXME problema con matrices rectangulares!!!
            self.canvas.create_line([(i, 0), (i, width)], tag='grid_line')
            self.canvas.create_line([(0, i), (height, i)], tag='grid_line')

    def update_view(self):
        self.canvas.delete("agent", "object")  # Limpia solo agentes y objetos

        # Dibuja los agentes
        '''for agent_name, agent in self.model.agents.items():
            x, y = agent.position
            self.canvas.create_image(
                x * 40, y * 40, image=self.object_image, anchor='nw', tags="agent"
            )'''
        
        
        # Dibuja los objetos
        ic(self.img_dict)
        for object, matrix_pos in self.model.objects.items():
            
            #object.x, object.y = matrix_pos.position
            #ic(object.x, object.y)

            img = self.img_dict.get(object.literal_name)
            
            # TODO añadir ruta de imagen a objetos
            self.canvas.create_image(
                object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
            )
            '''self.canvas.create_rectangle(
                object.x * 40, object.y * 40, object.x * 40 + 30, object.y * 40 + 30, fill="green", tags="object"
            )'''

    def animate_movement(self, movements, index=0):
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

    model_for_view = HouseModel(room.matrix)
    view = HouseView(model_for_view, height, width)

    # Movimientos de prueba
    movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
    # Inicia la animación después de un segundo
    view.after(1000, lambda: view.animate_movement(movements))

    view.mainloop()

