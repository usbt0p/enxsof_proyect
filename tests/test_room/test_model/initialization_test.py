import sys
sys.path.insert(0, 'enxsof_proyect')

import unittest
from src.mvc.model import Model  

class TestRoomInitialization(unittest.TestCase):
    def test_room_initialized_with_zeros(self):
        """
        Test the initialization of an array filled with zeros.

        Steps:
        1. Establish the array size.
        2. Instantiate the Model class.
        3. Check if the array is filled with zeros.
        """
        # Arrange - Configuration
        room_width = 5
        room_height = 5
        
        # Act - Execution
        room = Model(room_width, room_height)
        
        # Assert - Verification
        for row in room.room:
            for element in row:
                self.assertEqual(element, 0, "Room element should be initialized with zero")

if __name__ == '__main__':
    unittest.main()
