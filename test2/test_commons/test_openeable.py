import unittest
from utiles.commons.openable import Openable

class TestOpenable(unittest.TestCase):

    def test_openable_initialization(self):
        openable = Openable(0, 0, "Box")
        self.assertEqual(openable.x, 0)
        self.assertEqual(openable.y, 0)
        self.assertEqual(openable.literal_name, "Box")
        self.assertFalse(openable.isOpen)

    def test_openable_open(self):
        openable = Openable(0, 0, "Box")
        openable.open()
        self.assertTrue(openable.isOpen)

    def test_openable_close(self):
        openable = Openable(0, 0, "Box")
        openable.open()
        openable.close()
        self.assertFalse(openable.isOpen)

if __name__ == '__main__':
    unittest.main()
