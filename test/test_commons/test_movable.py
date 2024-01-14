import sys
sys.path.insert(0, '.')

import unittest
from utiles.objects.movable import Movable

class TestMovableMethods(unittest.TestCase):
    def test_movable_init(self) -> None:
        movable = Movable(4, 4, "TestThing")
        self.assertEqual(movable.x, 4)
        self.assertEqual(movable.y, 4)
        self.assertEqual(movable.literal_name, "TestThing")
        self.assertFalse(movable.openable)

    
if __name__ == '__main__':
    unittest.main()
