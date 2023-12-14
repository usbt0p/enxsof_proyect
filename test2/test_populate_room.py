import unittest
from unittest.mock import patch

from mvc.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model(16, 16)

    @patch('builtins.input', side_effect=["assets/default_16x16_room.json"])
    def test_populate_room(self, mock_input):
        self.model.populate_room("assets/default_16x16_room.json")
        # TODO Agrega aquí tus aserciones para verificar que la matriz de la habitación se haya poblado correctamente
        
    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
