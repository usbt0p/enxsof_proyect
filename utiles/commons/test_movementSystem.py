import unittest
from unittest.mock import patch
from utiles.commons.movementSystem import pathPlanning

class TestPathPlanning(unittest.TestCase):

    def setUp(self):
        self.path_planning = pathPlanning()

    def test_generate_random_position(self):
        max_x = 10
        max_y = 10
        position = self.path_planning.generate_random_position(max_x, max_y)
        self.assertTrue(0 <= position[0] <= max_x)
        self.assertTrue(0 <= position[1] <= max_y)

    def test_is_valid_position(self):
        x = 5
        y = 5
        max_x = 10
        max_y = 10
        self.assertTrue(self.path_planning.is_valid_position(x, y, max_x, max_y))

        x = -1
        y = 5
        self.assertFalse(self.path_planning.is_valid_position(x, y, max_x, max_y))

        x = 5
        y = 11
        self.assertFalse(self.path_planning.is_valid_position(x, y, max_x, max_y))

        # Mocking is_position_occupied method
        with patch.object(pathPlanning, 'is_position_occupied', return_value=True):
            x = 5
            y = 5
            self.assertFalse(self.path_planning.is_valid_position(x, y, max_x, max_y))

    def test_a_star_search(self):
        start = (0, 0)
        goal = (5, 5)
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        path = self.path_planning.a_star_search(start, goal, grid)
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])

if __name__ == '__main__':
    unittest.main()