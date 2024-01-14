import sys
sys.path.insert(0, '.')

import unittest
from src.mvc.model import Model
import utiles.agents.agent as agent

class TestModel(unittest.TestCase):

    def setUp(self) -> None:
        self.test_instance = Model(16, 16)
        
    def test_generate_empty_room(self) -> None:
        room = self.test_instance.generate_empty_room()
        self.assertEqual(len(room), 16)
        self.assertEqual(len(room[0]), 16)
        self.assertEqual(room[1][1], 0)

    def test_generate_empty_room_positive(self) -> None:
        self.test_instance.x_size = 3
        self.test_instance.y_size = 4
        result = self.test_instance.generate_empty_room()
        expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(result, expected_result)

    def test_generate_empty_room_with_zero_size(self) -> None:
        self.test_instance.x_size = 0
        self.test_instance.y_size = 0
        result = self.test_instance.generate_empty_room()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_generate_empty_room_with_negative_size(self) -> None:
        self.test_instance.x_size = -2
        self.test_instance.y_size = 3
        with self.assertRaises(ValueError):
            self.test_instance.generate_empty_room()
            raise ValueError("Size of the room must be positive")
        
    def test_read_grid_config_file(self) -> None:
        # Crea un archivo JSON temporal para las pruebas
        with open('test_config.json', 'w') as f:
            f.write('{"key": "value"}')

        data = self.test_instance.read_grid_config_file('test_config.json')

        self.assertEqual(data, {"key": "value"})

    def test_read_grid_config_file_file_not_found(self) -> None:
        data = self.test_instance.read_grid_config_file('nonexistent_file.json')

        self.assertIsNone(data)

    def test_read_grid_config_file_invalid_json(self) -> None:
        # Crea un archivo JSON temporal con sintaxis JSON no válida
        with open('invalid_config.json', 'w') as f:
            f.write('{"key": "value",}')

        data = self.test_instance.read_grid_config_file('invalid_config.json')

        self.assertIsNone(data)

    def test_read_invalid_config_file(self) -> None:
        # Verifica que se maneje adecuadamente un archivo de configuración inválido
        with open('invalid_config.json', 'w') as f:
            f.write('{"key": "value",')

        data = self.test_instance.read_grid_config_file('invalid_config.json')

        self.assertIsNone(data)

    def test_populate_room(self) -> None:
        
        room_layout = [
    ["Wall", "Wall", "Wall", "Wall", "Wall", 2, 0, 2, 2, 2, "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"],
    ["Wall", "Armario", "Vater1", 0, "Wall", 2, 0, 0, 2, 2, "Wall", 0, "Sofa", "Sofa", "Armario", "Wall"],
    ["Wall", 0, 0, 0, "Wall", 2, 2, 0, 2, 2, "Wall", 0, "Table", "Table", 0, "Wall"],
    ["Wall", 0, 0, 0, "Wall", 2, 2, 0, 2, 2, "Wall", 0, 0, 0, 0, "Wall"],
    ["Wall", 0, 0, 0, "Wall", "Wall", "Wall", "Door_main", "Wall", "Wall", "Wall", 0, 0, 0, "Base", "Wall"],
    ["Wall", 0, 0, "Planta1", "Wall", 0, 0, 0, 0, 0, "Wall", 0, 0, 0, "Cama_g", "Wall"],
    ["Wall", "Wall", "Door", "Wall", "Wall", 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall"],
    ["Wall", "Base", 0, 0, 0, 0, 0, 0, 0, 0, "Door", 0, 0, 0, 0, "Wall"],
    ["Wall", 0, 0, 0, 0, 0, 0, 0, 0, 0, "Wall", 0, 0, 0, 0, "Wall"],
    ["Wall", "Wall", "Wall", "Door", "Wall", "Wall", "Wall", "Wall", "Wall", 0, "Wall", 0, "Sofa", "Sofa", 0, "Wall"],
    ["Wall", 0, 0, 0, 0, 0, "Fridge", "Fridge", "Wall", 0, "Wall", 0, "Table", "Table", 0, "Wall"],
    ["Wall", 0, "Cama", 0, 0, 0, 0, 0, "Wall", 0, "Wall", 0, "Sofa", "Sofa", 0, "Wall"],
    ["Wall", 0, 0, 0, 0, 0, 0, 0, "Door", 0, "Door", 0, 0, 0, 0, "Wall"],
    ["Wall", 0, 0, 0, 0, 0, "Planta3", 0, "Wall", 0, "Wall", 0, 0, 0, 0, "Wall"],
    ["Wall", "Fridge", 0, "Table", "Table", 0, 0, 0, "Wall", 0, "Wall", 0, "Silla2", 0, "Juego", "Wall"],
    ["Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"]
    ]

        aux = []
        room = Model(16, 16)
        file_path = 'assets/default_16x16_room.json'
        room.populate_room(file_path)

        for row in room.matrix:
            row_list = []
            for x, element in enumerate(row):
                if element == 0:
                    row_list.append(0)
                elif element == 2:
                    row_list.append(2)
                else:
                    row_list.append(element._literal_name)
            aux.append(row_list)

        self.assertEqual(aux, room_layout)

    def test_move_object(self) -> None:
        
        initial_value = self.test_instance.matrix[4][7]
        
        
        room = Model(16, 16)

        file_path = 'assets/default_16x16_room.json'

        room.populate_room(file_path)

        gato = agent.Agent("Gato", 7, 7)
        room.generate_agents(gato)

        room.object_teleport(7, 4, 1, 1)
        
        final_value = self.test_instance.matrix[1][1]

        self.assertEqual(final_value, initial_value)

if __name__ == '__main__':
    unittest.main()
