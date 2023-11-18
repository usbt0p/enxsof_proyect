import unittest
from ....src.room.Model import Model  # TODO Change the path

class TestRoomInitialization(unittest.TestCase): #Testst the initialization of an array filled with zeros
    def test_room_initialized_with_zeros(self):
        # Stablish the array size
        room_width = 5
        room_height = 5
        
        # Instance the model class
        room = Model(room_width, room_height)
        
        # Check if the array is filled with zeros
        for row in room.room:
            for element in row:
                self.assertEqual(element, 0, "Room element should be initialized with zero")

if __name__ == '__main__':
    unittest.main()
