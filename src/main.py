from src.mvc import model, view, observer, subject

# Constants:
X_MATRIX = 16
Y_MATRIX = 16
HEIGHT = 40 * Y_MATRIX
WIDTH = 40 * X_MATRIX

'''# Crear un sujeto
subject = Subject()

# Crear observadores
observer1 = ConcreteObserver('Observer1')
observer2 = ConcreteObserver('Observer2')

# Adjuntar los observadores al sujeto
subject.attach(observer1)
subject.attach(observer2)

# Notificar a todos los observadores
subject.notify('¡Hola, Observadores!')'''
  
room = model.Model(X_MATRIX, Y_MATRIX)
file_path = 'assets/default_16x16_room.json'
room.populate_room(file_path)

model_for_view = view.HouseModel(room.matrix)
view_house = view.HouseView(model_for_view, HEIGHT, WIDTH)

# Movimientos de prueba
movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
# Inicia la animación después de un segundo
view_house.after(1000, lambda: view_house.animate_movement(movements))

view_house.mainloop()

'''def main():
    pass

if __name__ == "__main__":
    main()'''