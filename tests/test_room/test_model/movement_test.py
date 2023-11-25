import sys
sys.path.insert(0, '.')

import unittest
from src.mvc.model import Model  # Importa tu clase Model y otras clases necesarias
from utiles.commons.fridge import Fridge

"""
TODO Este test debería funcionar si añadimos una comprobación al mover/colocar objetos que devuelva un error
 cuando ya está ocupada la casilla por cualquier objeto que no sea aire, silla, puerta etc.
"""

class TestModel(unittest.TestCase):
    def setUp(self):
        # Configura el entorno necesario para las pruebas
        self.model = Model(10, 10)  # Establece el tamaño del modelo
        file_path = 'assets/default_10x10_room.json'  # Reemplaza con la ruta a tu archivo JSON
        self.model.populate_room(file_path)  # Llena el modelo con los datos del archivo

    def test_object_placement_collision(self):
        # Intenta colocar un objeto donde ya hay otro y verifica si falla
        # Ejemplo: intentar colocar una nevera donde hay una pared
        with self.assertRaises(AssertionError):
            # Intenta colocar una nevera en una posición donde hay una pared
            self.model.matrix[0][0] = Fridge(0, 0)  # Ajusta las coordenadas según tu necesidad

if __name__ == '__main__':
    unittest.main()
