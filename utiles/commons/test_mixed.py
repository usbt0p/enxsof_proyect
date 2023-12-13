import unittest
from utiles.commons.mixed import Mixed

class TestMixed(unittest.TestCase):

    def setUp(self):
        self.mixed = Mixed(0, 0, "Mixed Container", {})

    def test_add_storage(self):
        self.mixed.add_storage(apples=5)
        self.assertEqual(self.mixed.storage, {'apples': 5})

        self.mixed.add_storage(oranges=3)
        self.assertEqual(self.mixed.storage, {'apples': 5, 'oranges': 3})

    def test_remove_stock(self):
        self.mixed.add_storage(apples=5, oranges=3)

        self.mixed.remove_stock(apples=2)
        self.assertEqual(self.mixed.storage, {'apples': 3, 'oranges': 3})

        self.mixed.remove_stock(oranges=1)
        self.assertEqual(self.mixed.storage, {'apples': 3, 'oranges': 2})

    def test_str(self):
        self.assertEqual(str(self.mixed), "Mixed Container, storage={}")

        self.mixed.add_storage(apples=5, oranges=3)
        self.assertEqual(str(self.mixed), "Mixed Container, storage={'apples': 5, 'oranges': 3}")

if __name__ == '__main__':
    unittest.main()