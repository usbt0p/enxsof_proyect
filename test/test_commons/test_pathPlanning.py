import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.pathPlanning import PathPlanning

class TestPathPlanning(unittest.TestCase):

    def setUp(self):
        # Puedes inicializar objetos o valores necesarios para tus pruebas aquí.
        pass

    def tearDown(self):
        # Puedes limpiar o liberar recursos después de cada prueba aquí.
        pass

    def test_generate_random_position(self):
        path_planning = PathPlanning()
        max_x, max_y = 10, 10
        random_position = path_planning.generate_random_position(max_x, max_y)
        self.assertTrue(0 <= random_position[0] < max_x)
        self.assertTrue(0 <= random_position[1] < max_y)

    def test_is_position_occupied(self):
        # Aquí deberías proporcionar un ejemplo válido de grid y coordenadas para probar la función.
        path_planning = PathPlanning()
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertTrue(path_planning.is_position_occupied(1, 1, grid))
        self.assertFalse(path_planning.is_position_occupied(0, 0, grid))

    def test_is_valid_position(self):
        path_planning = PathPlanning()
        max_x, max_y = 3, 3
        self.assertTrue(path_planning.is_valid_position(1, 1, max_x, max_y))
        self.assertFalse(path_planning.is_valid_position(3, 3, max_x, max_y))

    def test_heuristic(self):
        path_planning = PathPlanning()
        a, b = (0, 0), (3, 4)
        distance = path_planning.heuristic(a, b)
        self.assertEqual(distance, 7)  # Distancia de Manhattan

    # Puedes seguir añadiendo más pruebas según sea necesario

if __name__ == '__main__':
    unittest.main()
