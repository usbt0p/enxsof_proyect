import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.opener import Opener

class OpenerTests(unittest.TestCase):

    def setUp(self):
        self.opener = Opener(0, 0, "Opener Object")

    def test_initial_position(self):
        self.assertEqual(self.opener.x, 0)
        self.assertEqual(self.opener.y, 0)

    def test_open_opener(self):
        self.assertFalse(self.opener.is_open)
        self.opener.open()
        self.assertTrue(self.opener.is_open)

    def test_close_opener(self):
        self.opener.open()
        self.assertTrue(self.opener.is_open)
        self.opener.close()
        self.assertFalse(self.opener.is_open)

    def test_str_representation(self):
        expected_str = f"Opener Object: coords=(0, 0), collision=True, open=False"
        self.assertEqual(str(self.opener), expected_str)

if __name__ == '__main__':
    unittest.main()