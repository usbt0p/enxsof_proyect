import os
os.environ['PYTHONPATH'] = '.'

import unittest
from src.mvc import model, view
from tests.test_room.test_model.initialization_test import TestRoomInitialization
from tests.test_room.test_model.populate_test import TestPopulateRoom
from tests.test_Objects.unittest_object_fridge import TestFridge
from tests.test_Objects.unittest_object_sofa import TestSofa
from tests.test_Objects.unittest_object_table import TestTable
from tests.test_Objects.unittest_object_thing import TestThing
from tests.test_Objects.unittest_object_wall import TestWall
from tests.test_Objects.unittest_object_air import TestAir
from tests.test_Objects.unittest_object_container import TestContainer
from tests.test_Objects.unittest_object_door import TestDoor
from tests.test_Objects.unittest_object_obstacle import TestObstacle


opcion = 0
while opcion != 1 and opcion != 2 and opcion != 3:
    opcion = int(input("Ingrese el tamaño de la casa \n1.10x10 \n2.16x10 \n3.16x16 \n--> "))
    
    if opcion == 1:
        X_MATRIX = 10
        Y_MATRIX = 10
    elif opcion == 2:
        X_MATRIX = 16
        Y_MATRIX = 10
    elif opcion == 3:
        X_MATRIX = 16
        Y_MATRIX = 16
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Constants:
HEIGHT = 40 * Y_MATRIX
WIDTH = 40 * X_MATRIX

file_path = f'assets/default_{X_MATRIX}x{Y_MATRIX}_room.json' #Filepath para los tests y la ejecucion posterior

#Se ejecutan todos los tests de objetos

objects_tests_suite = unittest.TestLoader().loadTestsFromTestCase(TestFridge)
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSofa))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTable))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestThing))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWall))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAir))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestContainer))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDoor))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestObstacle))

populate_instance_test = TestPopulateRoom(file_path)
initialization_instance_test = TestRoomInitialization()

model_tests_suite = unittest.TestSuite()
model_tests_suite.addTest(populate_instance_test)
model_tests_suite.addTest(initialization_instance_test)


unittest.TextTestRunner(verbosity=2).run(objects_tests_suite)

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