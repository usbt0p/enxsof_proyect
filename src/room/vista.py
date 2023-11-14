import tkinter as tk

# Las imágenes para las habitaciones y los agentes deben estar en el mismo directorio que el script.
# Por ejemplo: "kitchen.png", "robot.png", etc.
ROOM_IMAGES = {
    "Kitchen": "kitchen.png",
    "Bath": "bath.png",
    "Bedroom": "bedroom.png",
    "Hallway": "hallway.png",
    "Hall": "hall.png",
    "Livingroom": "livingroom.png",
}
AGENT_IMAGE = "robot.png"

class EnvironmentGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Domestic Care Robot Environment')
        self.grid_size = 10  # Define el tamaño de la cuadrícula, por ejemplo 10x10
        self.cell_width = 50  # Ancho de cada celda de la cuadrícula
        self.cell_height = 50  # Altura de cada celda de la cuadrícula
        self.canvas = tk.Canvas(self, width=self.grid_size*self.cell_width,
                                height=self.grid_size*self.cell_height)
        self.canvas.pack()
        self.draw_grid()
        self.place_rooms()
        self.place_agents()

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_rectangle(i*self.cell_width, j*self.cell_height,
                                             (i+1)*self.cell_width, (j+1)*self.cell_height,
                                             fill='white')

    def place_rooms(self):
        # Este método debería colocar las imágenes de las habitaciones en sus respectivas posiciones.
        for room, image_file in ROOM_IMAGES.items():
            image = tk.PhotoImage(file=image_file)
            # Suponiendo que se tiene la posición de cada habitación, por ejemplo:
            # room_positions = {"Kitchen": (0, 0), "Bath": (1, 0), ...}
            x, y = room_positions[room]
            self.canvas.create_image(x*self.cell_width, y*self.cell_height,
                                     image=image, anchor='nw')
            # Guardar la referencia de la imagen para evitar que sea eliminada por el recolector de basura.
            self.canvas.image = image

    def place_agents(self):
        # Similar a place_rooms, pero para agentes como el robot.
        agent_image = tk.PhotoImage(file=AGENT_IMAGE)
        # Suponiendo que se tiene la posición del robot, por ejemplo (5, 5):
        x, y = (5, 5)
        self.canvas.create_image(x*self.cell_width, y*self.cell_height,
                                 image=agent_image, anchor='nw')
        self.canvas.agent_image = agent_image

# Ejecuta la aplicación
if __name__ == '__main__':
    app = EnvironmentGUI()
    app.mainloop()
