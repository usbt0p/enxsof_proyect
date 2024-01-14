import sys
sys.path.insert(0, '.')

import unittest
from utiles.objects.mixed import Mixed

class TestMixedMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.mixed = Mixed(0, 0, "Mixed Container", {})

    def test_mixed_init(self) -> None:
        mixed = Mixed(4, 4, "Thing", {})
        self.assertEqual(mixed.x, 4)
        self.assertEqual(mixed.y, 4)
        self.assertEqual(mixed.literal_name, "Thing")
        self.assertEqual(mixed.storage, {})

    def test_str(self) -> None:
        self.assertEqual(str(self.mixed), "Mixed Container: coords=(0, 0), collision=True, open=False, storage={}")

        self.mixed.add_storage(apples=5, oranges=3)
        self.assertEqual(str(self.mixed), 
                         "Mixed Container: coords=(0, 0), collision=True, open=False, storage={'apples': 5, 'oranges': 3}")

    def test_add_storage(self) -> None:
        mixed = Mixed(0, 0, "TestMixed", {})
        mixed.add_storage(thing1=1, thing2=2)
        self.assertEqual(mixed.storage, {'thing1': 1, 'thing2': 2})
        
        mixed.add_storage(thing1=2, thing2=14)
        self.assertEqual(mixed.storage, {'thing1': 3, 'thing2': 16})

    def test_remove_stock(self) -> None:
        mixed = Mixed(0, 0, "TestMixed", {'thing1': 3, 'thing2': 16})
        mixed.remove_stock(thing1=1, thing2=2)
        self.assertEqual(mixed.storage, {'thing1': 2, 'thing2': 14})

        with self.assertRaises(ValueError):
            mixed.remove_stock(thing3=1)

    

if __name__ == '__main__':
    unittest.main()
