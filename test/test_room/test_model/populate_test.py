import unittest
from ....src.room.Model import Model  # TODO Needs to be changed
from ....utiles.commons import *

class TestPopulateRoom(unittest.TestCase):
    def test_populate_room_with_small_json(self):
        # Arrange
        file_path = 'test_config.json'  
        room = Model(3, 3)  # Dimensions have to match the json dictionary

        # Create the room 
        room.populate_room(file_path)

        # Check if the final array is filled with objects
        for row in room.room:
            for element in row:
                self.assertIsInstance(
                    element, object,
                    "All elements in the room should be instances of class objects"
                )

if __name__ == '__main__':
    unittest.main()
