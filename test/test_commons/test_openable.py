import unittest
from utiles.commons.openable import Openable

class TestOpenable(unittest.TestCase):

    def setUp(self):
        self.openable = Openable(0, 0, "Test Openable")

    def test_init(self):
        self.assertEqual(self.openable.x, 0)
        self.assertEqual(self.openable.y, 0)
        self.assertEqual(self.openable.literal_name, "Test Openable")
        self.assertFalse(self.openable.is_open)
        self.assertFalse(self.openable.movable)

    def test_isOpen(self):
        self.assertFalse(self.openable.isOpen)
        self.openable.open()
        self.assertTrue(self.openable.isOpen)
        self.openable.close()
        self.assertFalse(self.openable.isOpen)

    def test_open(self):
        self.assertFalse(self.openable.is_open)
        self.openable.open()
        self.assertTrue(self.openable.is_open)

    def test_close(self):
        self.openable.open()
        self.assertTrue(self.openable.is_open)
        self.openable.close()
        self.assertFalse(self.openable.is_open)

    def test_str(self):
        expected_str = "Test Openable: coords=(0, 0), collision=True, open=False"
        self.assertEqual(str(self.openable), expected_str)

if __name__ == '__main__':
    unittest.main()