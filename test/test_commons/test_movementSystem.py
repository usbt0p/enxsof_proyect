import sys
sys.path.insert(0, '.')

import unittest

from utiles.commons.movementSystem import (Movements, pathPlanning)

class TestMovementsMethods(unittest.TestCase):
    def setUp(self):
        class MockMovements(Movements):
            def __init__(self):
                self.x = 0
                self.y = 0
                self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Example grid

        self.movements_instance = MockMovements()

    def test_generate_random_position(self):
        max_x = 10
        max_y = 10
        position = self.path_planning.generate_random_position(max_x, max_y)
        self.assertTrue(0 <= position[0] <= max_x)
        self.assertTrue(0 <= position[1] <= max_y)

    def test_is_position_occupied(self):
        self.assertFalse(self.movements_instance.is_position_occupied(1, 1))  # Position (1, 1) is not occupied

    def test_object_teleport(self):
        self.movements_instance.matrix[0][0] = 1
        self.movements_instance.object_teleport(0, 0, 2, 2)
        self.assertEqual(self.movements_instance.matrix[2][2], 1)  # Object teleported successfully

class TestPathPlanningMethods(unittest.TestCase):
    def setUp(self):
        class MockPathPlanning(pathPlanning):
            def __init__(self):
                self.agents = [{'x': 0, 'y': 0}, {'x': 1, 'y': 1}]  # Example agents

        self.path_planning_instance = MockPathPlanning()

    def test_generate_random_position(self):
        position = self.path_planning_instance.generate_random_position(5, 5)
        self.assertTrue(0 <= position[0] <= 5)
        self.assertTrue(0 <= position[1] <= 5)

    def test_is_valid_position(self):
        self.assertTrue(self.path_planning_instance.is_valid_position(2, 2, 5, 5))
        self.assertFalse(self.path_planning_instance.is_valid_position(10, 10, 5, 5))

    def test_a_star_search(self):
        start = (0, 0)
        goal = (2, 2)
        path = self.path_planning_instance.a_star_search(start, goal, 
                                                         [[0, 0, 0], 
                                                          [0, 1, 0], 
                                                          [0, 0, 0]])
        self.assertEqual(path, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])  # Example path

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
