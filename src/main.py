from src.mvc import model, view
import unittest
from tests.test_room.test_model.initialization_test import TestRoomInitialization
from tests.test_room.test_model.populate_test import TestPopulateRoom
from tests.test_Objects.test_fridge import TestFridge
from tests.test_Objects.test_sofa import TestSofa
from tests.test_Objects.test_table import TestTable
from tests.test_Objects.test_thing import TestThing
from tests.test_Objects.test_wall import TestWall

file_path = 'assets/default_10x10_room.json' #Filepath para los tests y la ejecucion posterior

#Se ejecutan todos los tests de objetos

objects_tests_suite = unittest.TestLoader().loadTestsFromTestCase(TestFridge)
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSofa))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTable))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestThing))
objects_tests_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWall))

populate_instance_test = TestPopulateRoom(file_path)
initialization_instance_test = TestRoomInitialization()

model_tests_suite = unittest.TestSuite()
model_tests_suite.addTest(populate_instance_test)
model_tests_suite.addTest(initialization_instance_test)


unittest.TextTestRunner(verbosity=2).run(objects_tests_suite)

# Constants:
X_MATRIX = 10
Y_MATRIX = 10
HEIGHT = 40 * Y_MATRIX
WIDTH = 40 * X_MATRIX

room = model.Model(X_MATRIX, Y_MATRIX)
room.populate_room(file_path)

model_for_view = view.HouseModel(room.matrix)
view = view.HouseView(model_for_view, HEIGHT, WIDTH)

# Movimientos de prueba
movements = [(1,1),(2,2),(3,3),(4,4),(5,5),(5,4)]
# Inicia la animación después de un segundo
view.after(1000, lambda: view.animate_movement(movements))

view.mainloop()