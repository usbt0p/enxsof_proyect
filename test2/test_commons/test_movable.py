import unittest
from utiles.commons.movable import Movable

class TestMovableMethods(unittest.TestCase):
    def test_movable_init(self):
        movable = Movable(4, 4, "TestThing")
        self.assertEqual(movable.x, 4)
        self.assertEqual(movable.y, 4)
        self.assertEqual(movable.literal_name, "TestThing")
        self.assertFalse(movable.openable)

    def test_move_up(self):
        movable = Movable(0, 0, "TestMovable")
        movable.move_up()
        self.assertEqual(movable.y, 1)

    def test_move_down(self):
        movable = Movable(0, 0, "TestMovable")
        movable.move_down()
        self.assertEqual(movable.y, -1)

    def test_move_left(self):
        movable = Movable(0, 0, "TestMovable")
        movable.move_left()
        self.assertEqual(movable.x, -1)

    def test_move_right(self):
        movable = Movable(0, 0, "TestMovable")
        movable.move_right()
        self.assertEqual(movable.x, 1)

    def test_multiple_moves(self):
        movable = Movable(0, 0, "TestMovable")
        movable.move_up()
        movable.move_down()
        movable.move_left()
        movable.move_right()
        self.assertEqual(movable.x, 0)
        self.assertEqual(movable.y, 0)

    
if __name__ == '__main__':
    unittest.main()
