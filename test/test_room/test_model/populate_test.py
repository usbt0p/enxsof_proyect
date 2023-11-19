import unittest
from ....src.room.Model import Model  # TODO Cambiar la ruta
from ....utiles.commons import *

class TestPopulateRoom(unittest.TestCase):
    def test_populate_room_with_small_json(self):
        """
        Test the population of the room with objects from a small JSON file.

        Steps:
        1. Arrange the necessary parameters and the room instance.
        2. Populate the room from the JSON file.
        3. Check if all elements in the room are instances of class objects.
        """
        # Arrange - Configuration
        file_path = 'test_config.json'  
        room = Model(3, 3)  # Las dimensiones deben coincidir con el diccionario JSON

        # Act - Execution
        room.populate_room(file_path)

        # Assert - Verification
        for row in room.room:
            for element in row:
                self.assertIsInstance(
                    element, object,
                    "All elements in the room should be instances of class objects"
                )

if __name__ == '__main__':
    unittest.main()
