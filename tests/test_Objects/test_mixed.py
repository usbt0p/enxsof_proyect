import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.mixed import Mixed

class MixedTests(unittest.TestCase):

    def setUp(self):
        self.mixed = Mixed(0, 0, "Mixed Object")

    def test_initial_position(self):
        self.assertEqual(self.mixed.x, 0)
        self.assertEqual(self.mixed.y, 0)


    def test_open_mixed(self):
        self.assertFalse(self.mixed.is_open)
        self.mixed.open()
        self.assertTrue(self.mixed.is_open)

    def test_close_mixed(self):
        self.mixed.open()
        self.assertTrue(self.mixed.is_open)
        self.mixed.close()
        self.assertFalse(self.mixed.is_open)

    def test_str_representation(self):
        expected_str = f"Mixed Object: coords=(0, 0), collision=True, open=False"
        self.assertEqual(str(self.mixed), expected_str)

if __name__ == '__main__':
    unittest.main()