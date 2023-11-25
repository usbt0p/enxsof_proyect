import sys
sys.path.insert(0, '.')

import unittest
from src.mvc.model import Model  
from utiles.commons import *

class TestPopulateRoom(unittest.TestCase):

    def __init__(self, path):
        self.path = path


    def test_populate_room_with_small_json(self):
        """
        Test the population of the room with objects from a small JSON file.

        Steps:
        1. Arrange the necessary parameters and the room instance.
        2. Populate the room from the JSON file.
        3. Check if all elements in the room are instances of class objects.
        """
        # Arrange - Configuration  
        room = Model(3, 3)  # Las dimensiones deben coincidir con el diccionario JSON

        # Act - Execution
        room.populate_room(self.path)

        # Assert - Verification
        for row in room.room:
            for element in row:
                self.assertIsInstance(
                    element, object,
                    "All elements in the room should be instances of class objects"
                )

if __name__ == '__main__':
    unittest.main()
