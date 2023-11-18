from src.mvc import model, view

# Constants:
HEIGHT = 640 # TODO Escalar en función del tamaño del array!!!
WIDTH = 640

room = model.Model(16, 16)
file_path = 'assets/default_16x16_room.json'
room.populate_room(file_path)

model_for_view = view.HouseModel(room.matrix)
view = view.HouseView(model_for_view, HEIGHT, WIDTH)

# Movimientos de prueba
movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
# Inicia la animación después de un segundo
view.after(1000, lambda: view.animate_movement(movements))

view.mainloop()