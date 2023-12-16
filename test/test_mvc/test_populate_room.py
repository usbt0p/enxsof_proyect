import unittest
from unittest.mock import patch
import utiles.agents.agent as agent
from src.mvc.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model(16, 16)

    def test_populate_room(self):
        
        room_layout = [
            "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall",
            "Wall", 0, 0, 0, "Wall", 0, 0, 0, 0, 0, "Wall", 0, "Sofa", "Sofa", 0, "Wall",
            "Wall", 0, "Sofa", 0, "Wall", 0, 0, 0, 0, 0, "Wall", 0, "Table", "Table", 0, "Wall",
            "Wall", 0, "Table", 0, "Wall", 0, 0, 0, 0, 0, "Door", 0, 0, 0, 0, "Wall",
            "Wall", 0, 0, 0, "Wall", 0, 0, "Table", 0, 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", 0, 0, 0, "Wall", 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", "Wall", "Door", "Wall", "Wall", 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", 0, 0, 0, 0, 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", 0, 0, 0, 0, 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", "Wall", "Wall", "Door", "Wall", "Wall", "Wall", "Wall", "Wall", 0, "Wall", 0, "Sofa", "Sofa", 0, "Wall",
            "Wall", 0, 0, 0, 0, 0, "Fridge", "Fridge", "Wall", 0, "Wall", 0, "Table", "Table", 0, "Wall",
            "Wall", 0, 0, 0, 0, 0, 0, 0, "Wall", 0, "Wall", 0, "Sofa", "Sofa", 0, "Wall",
            "Wall", 0, 0, 0, 0, 0, 0, 0, "Door", 0, "Door", 0, 0, 0, 0, "Wall",
            "Wall", "Fridge", 0, 0, 0, 0, 0, 0, "Wall", 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", "Fridge", 0, "Table", "Table", 0, 0, 0, "Wall", 0, "Wall", 0, 0, 0, 0, "Wall",
            "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall",
        ]

        aux = []
        
        room = Model(16, 16)
    
        file_path = 'assets/default_16x16_room.json'

        room.populate_room(file_path)

        for row in room.matrix:
            for element in row:
                if element == 0:
                    aux.append(0)
                else:
                    aux.append(element._literal_name)
                    
        self.assertEqual(aux, room_layout)
                
    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
