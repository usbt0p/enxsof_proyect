import unittest
from utiles.commons.movable import Movable

class TestMovable(unittest.TestCase):

    def setUp(self):
        self.movable = Movable(0, 0, "Test Movable")

    def test_init(self):
        self.assertEqual(self.movable.x, 0)
        self.assertEqual(self.movable.y, 0)
        self.assertEqual(self.movable.literal_name, "Test Movable")
        self.assertFalse(self.movable.openable)

if __name__ == '__main__':
    unittest.main()