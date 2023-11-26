import sys
sys.path.insert(0, '.')

from src.mvc.model import Model
from src.mvc.view import View
from src.mvc.controller import Controller
import unittest

# Show menu to select grid
opcion = 0
while opcion != 1 and opcion != 2 and opcion != 3:
    try:
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
    except ValueError:
        print("Error: Ingrese un número válido.")

# Constants:
HEIGHT = 40 * Y_MATRIX
WIDTH = 40 * X_MATRIX

file_path = f'assets/default_{X_MATRIX}x{Y_MATRIX}_room.json' 
# Filepath para los tests y la ejecucion posterior



# Creamos el Modelo, que es el sujeto del programa al que se subscribirán los obs y alamcena el environment
room = Model(X_MATRIX, Y_MATRIX)
room.populate_room(file_path)
room.generate_agents(['Gato'])

# Crea una vista de la casa, 'frontend' del proyecto:
# Procesa todos los objetos, los añade a un modelo para la vista, 
view_house = View('view_house', room.matrix, room.agents, HEIGHT, WIDTH)
main_controller = Controller(room, view_house)


# Adjuntar los observadores al sujeto
#room.attach(view_house) # TODO crea y attachea controller

room.notify(view_house, "Override the ConcreteObserver's method `update method` for personalized logic")


view_house.mainloop()



if __name__ == "__main__":

    #from src.mvc import model, view
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