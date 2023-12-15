import sys
sys.path.insert(0, '.')

from src.mvc import (model, view, controller)
from utiles.commons import owner
import unittest

# Define constants for matrix size and window size
X_SIZE = 16
Y_SIZE = 16

height = 40*X_SIZE
width = 40*Y_SIZE

# Create the model and specify the size of the room and its configuration file
room = model.Model(X_SIZE, Y_SIZE)
file_path = 'assets/default_16x16_room.json'
room.populate_room(file_path)

# Create an agent and add it to the room
gato1 = owner.Owner("Gato", 7, 7)
gato2 = owner.Owner("Gato", 13, 13)
gato3 = owner.Owner("Gato", 3, 11)
gato4 = owner.Owner("Gato", 11, 3)
room.generate_agents(gato1, gato2, gato3, gato4)

# Create a view
view = view.View('view', height, width)

# Initalize controller and start vital constants thread
main_controller = controller.Controller(room, view)
main_controller.vital_threading()

# Send initial state to the view
room.notify(view, agents=room.agents, matrix=room.matrix)

# Start the main event loop
view.mainloop()




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
    