import tkinter as tk
import os
print(os.getcwd())
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
    def __init__(self, model):
        super().__init__()
        self.model = model  # Referencia al modelo

        self.title("Entorno Domótico")
        self.geometry("640x640")  # Tamaño de la ventana

        self.object_image = tk.PhotoImage(file="./src/room/gato.png")

        self.canvas = tk.Canvas(self, bg='white', height=640, width=640)
        self.canvas.pack()

        self.draw_grid()
        self.update_view()  # Actualiza la vista con el estado inicial del modelo

    def draw_grid(self):
        for i in range(0, 640, 40):
            self.canvas.create_line([(i, 0), (i, 640)], tag='grid_line')
            self.canvas.create_line([(0, i), (640, i)], tag='grid_line')

    def update_view(self):
        self.canvas.delete("agent", "object")  # Limpia solo agentes y objetos

        # Dibuja los agentes
        for agent_name, agent in self.model.agents.items():
            x, y = agent.position
            self.canvas.create_image(
                x * 40, y * 40, image=self.object_image, anchor='nw', tags="agent"
            )

        # Dibuja los objetos
        for object_name, obj in self.model.objects.items():
            x, y = obj.position
            self.canvas.create_rectangle(
                x * 40, y * 40, x * 40 + 30, y * 40 + 30, fill="green", tags="object"
            )

    def animate_movement(self, movements, index=0):
        if index < len(movements):
            pos = movements[index]
            self.model.move_agent('robot', pos)
            self.update_view()
            # Programa el siguiente movimiento después de un segundo
            self.after(1000, lambda: self.animate_movement(movements, index + 1))

# Ejemplo de uso
if __name__ == '__main__':
    model = HouseModel()
    view = HouseView(model)

    # Movimientos de prueba
    movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
    # Inicia la animación después de un segundo
    view.after(1000, lambda: view.animate_movement(movements))

    view.mainloop()

