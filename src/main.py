from src.mvc import model, view

# Constants:
X_MATRIX = 10
Y_MATRIX = 10
HEIGHT = 40 * Y_MATRIX
WIDTH = 40 * X_MATRIX

room = model.Model(X_MATRIX, Y_MATRIX)
file_path = 'assets/default_10x10_room.json'
room.populate_room(file_path)

model_for_view = view.HouseModel(room.matrix)
view = view.HouseView(model_for_view, HEIGHT, WIDTH)

# Movimientos de prueba
movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
# Inicia la animación después de un segundo
view.after(1000, lambda: view.animate_movement(movements))

view.mainloop()