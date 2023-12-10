import sys
sys.path.insert(0, '.')

from src.mvc.model import Model
from src.mvc.view import View
from src.mvc.controller import Controller
import unittest

# Una única casa
X_MATRIX = 16
Y_MATRIX = 16

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
view_house = View('view_house', HEIGHT, WIDTH)


main_controller = Controller(room, view_house)

# Adjuntar los observadores al sujeto
room.attach(view_house)

room.notify(view_house, agents=room.agents, matrix=room.matrix)

print(room.agents[0])
#main_controller.test_movement(room.agents[0])

main_controller.vital_threading()

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

    populate_instance_test = TestPopulateRoom()
    initialization_instance_test = TestRoomInitialization()

    model_tests_suite = unittest.TestSuite()
    model_tests_suite.addTest(populate_instance_test)
    model_tests_suite.addTest(initialization_instance_test)


    unittest.TextTestRunner(verbosity=2).run(objects_tests_suite)