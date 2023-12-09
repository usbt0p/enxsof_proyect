import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import patch
from utiles.commons.pathPlanning import PathPlanning

#Esta clase necesita repaso, junto con la de pathplanning no estoy seguro de si el funcioanmiento es correcto
#Los tests no funcionan correctamente, no se si es por el pathplanning o por el test pero prefiero no tocar pathplanning
class PathPlanningTests(unittest.TestCase):

    def setUp(self):
        self.path_planning = PathPlanning()

    def test_generate_random_position(self):
        max_x = 4
        max_y = 4
        position = self.path_planning.generate_random_position(max_x, max_y)
        self.assertTrue(0 <= position[0] < max_x)
        self.assertTrue(0 <= position[1] < max_y)

    def test_is_position_occupied(self):
        x = 3
        y = 3
        max_x = 4
        max_y = 4
        grid = [[0 for _ in range(max_y)] for _ in range(max_x)]
        self.assertFalse(self.path_planning.is_position_occupied(x, y, grid))

    def test_is_valid_position(self):
        x = 3
        y = 3
        max_x = 4
        max_y = 4
        self.assertTrue(self.path_planning.is_valid_position(x, y, max_x, max_y))

    @patch.object(PathPlanning, 'generate_random_position')
    def test_move_randomly_valid_position(self, mock_generate_random_position):
        max_x = 4
        max_y = 4
        mock_generate_random_position.return_value = (3, 3)
        self.path_planning.move_randomly(max_x, max_y)
        self.assertEqual(self.path_planning.position, (3, 3))

    @patch.object(PathPlanning, 'generate_random_position')
    def test_move_randomly_invalid_position(self, mock_generate_random_position):
        max_x = 4
        max_y = 4
        mock_generate_random_position.return_value = (2, 2)
        self.path_planning.move_randomly(max_x, max_y)
        self.assertNotEqual(self.path_planning.position, (2, 2))

    def test_heuristic(self):
        a = (0, 0)
        b = (3, 4)
        expected_distance = 7
        self.assertEqual(self.path_planning.heuristic(a, b), expected_distance)

    def test_a_star_search(self):
        start = (0, 0)
        goal = (4, 4)
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(self.path_planning.a_star_search(start, goal, grid), expected_path)

if __name__ == '__main__':
    unittest.main()