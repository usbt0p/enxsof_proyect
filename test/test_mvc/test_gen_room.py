import unittest
from src.mvc.model import Model

class TestGenerateEmptyRoom(unittest.TestCase):

    def setUp(self):
        self.test_instance = Model(16, 16)
        
    def test_generate_empty_room(self):
        room = self.test_instance.generate_empty_room()
        self.assertEqual(len(room), 16)
        self.assertEqual(len(room[0]), 16)
        self.assertEqual(room[1][1], 0)

    def test_generate_empty_room_positive(self):
        self.test_instance.x_size = 3
        self.test_instance.y_size = 4
        result = self.test_instance.generate_empty_room()
        expected_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(result, expected_result)

    def test_generate_empty_room_with_zero_size(self):
        self.test_instance.x_size = 0
        self.test_instance.y_size = 0
        result = self.test_instance.generate_empty_room()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_generate_empty_room_with_negative_size(self):
        self.test_instance.x_size = -2
        self.test_instance.y_size = 3
        with self.assertRaises(ValueError):
            self.test_instance.generate_empty_room()
            raise ValueError("Size of the room must be positive")

if __name__ == '__main__':
    unittest.main()
