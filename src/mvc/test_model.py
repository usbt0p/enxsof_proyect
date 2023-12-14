import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.model import Model

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model(16, 16)

    def test_generate_empty_room(self):
        room = self.model.generate_empty_room()
        self.assertEqual(len(room), 16)
        self.assertEqual(len(room[0]), 16)
        self.assertEqual(room[0][0], 0)

    def test_generate_agents(self):
        agent1 = MagicMock()
        agent2 = MagicMock()
        self.model.generate_agents(agent1, agent2)
        self.assertEqual(len(self.model.agents), 2)
        self.assertEqual(self.model.agents[0], agent1)
        self.assertEqual(self.model.agents[1], agent2)

    def test_populate_room(self):
        filepath = 'assets/default_16x16_room.json'
        self.model.read_grid_config_file = MagicMock(return_value=[
            ["Wall", "Wall", "Wall", "Wall"],
            ["Wall", "Sofa", "Table", "Wall"],
            ["Wall", "Door", "Fridge", "Wall"],
            ["Wall", "Wall", "Wall", "Wall"]
        ])
        self.model.populate_room(filepath)
        self.assertEqual(len(self.model.matrix), 16)
        self.assertEqual(len(self.model.matrix[0]), 16)
        self.assertEqual(self.model.matrix[0][0].__class__.__name__, "Thing")
        self.assertEqual(self.model.matrix[1][1].__class__.__name__, "Movable")
        self.assertEqual(self.model.matrix[2][2].__class__.__name__, "Mixed")
        self.assertEqual(self.model.matrix[2][1].__class__.__name__, "Openable")

    def test_read_grid_config_file(self):
        filepath = 'assets/default_16x16_room.json'
        data = {
            "map": [
                ["Wall", "Wall", "Wall", "Wall"],
                ["Wall", "Sofa", "Table", "Wall"],
                ["Wall", "Door", "Fridge", "Wall"],
                ["Wall", "Wall", "Wall", "Wall"]
            ]
        }
        self.model.open = MagicMock(return_value=data)
        result = self.model.read_grid_config_file(filepath)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()