import unittest
from utiles.commons.thing import Thing

class TestThing(unittest.TestCase):

    def test_thing_initialization(self):
        thing = Thing(10, 20, "Test Thing")
        self.assertEqual(thing.x, 10)
        self.assertEqual(thing.y, 20)
        self.assertEqual(thing.literal_name, "Test Thing")
        self.assertTrue(thing.collision)

    def test_thing_literal_name(self):
        thing = Thing(0, 0, "Original Name")
        self.assertEqual(thing.literal_name, "Original Name")
        thing.literal_name = "New Name"
        self.assertEqual(thing.literal_name, "New Name")

    def test_thing_collision(self):
        thing = Thing(0, 0, "Test Thing")
        self.assertTrue(thing.collision)
        thing.collision = False
        self.assertFalse(thing.collision)

    def test_thing_string_representation(self):
        thing = Thing(5, 10, "Test Thing")
        self.assertEqual(str(thing), "Test Thing: coords=(5, 10), collision=True")

if __name__ == '__main__':
    unittest.main()