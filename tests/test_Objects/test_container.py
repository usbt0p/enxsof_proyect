import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.container import Container

class ContainerTests(unittest.TestCase):

    def setUp(self):
        self.container = Container(0, 0, [], "Container 1")

    def test_initial_storage(self):
        self.assertEqual(self.container.storage, [])

    def test_set_storage(self):
        new_storage = [1, 2, 3]
        self.container.storage = new_storage
        self.assertEqual(self.container.storage, new_storage)

    def test_str_representation(self):
        expected_str = f"Container 1: coords=(0, 0), collision=True, storage=[]"
        self.assertEqual(str(self.container), expected_str)

if __name__ == '__main__':
    unittest.main()