import unittest
from unittest.mock import patch
from src.mvc.model import Model
from utiles.commons import agent  

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model(16, 16)

    def test_read_grid_config_file(self):
        # Crea un archivo JSON temporal para las pruebas
        with open('test_config.json', 'w') as f:
            f.write('{"key": "value"}')

        data = self.model.read_grid_config_file('test_config.json')

        self.assertEqual(data, {"key": "value"})

    def test_read_grid_config_file_file_not_found(self):
        data = self.model.read_grid_config_file('nonexistent_file.json')

        self.assertIsNone(data)

    def test_read_grid_config_file_invalid_json(self):
        # Crea un archivo JSON temporal con sintaxis JSON no válida
        with open('invalid_config.json', 'w') as f:
            f.write('{"key": "value",}')

        data = self.model.read_grid_config_file('invalid_config.json')

        self.assertIsNone(data)

    def test_read_invalid_config_file(self):
        # Verifica que se maneje adecuadamente un archivo de configuración inválido
        with open('invalid_config.json', 'w') as f:
            f.write('{"key": "value",')

        data = self.model.read_grid_config_file('invalid_config.json')

        self.assertIsNone(data)

    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
