import unittest
from utiles.commons.thing import Thing 

class TestThing(unittest.TestCase):

    def setUp(self):
        # Initial setup for testing
        self.thing = Thing(x=0, y=0, literal_name="TestThing", interactive=True, collision=True)

    def test_initialization(self):
        # Verify that attributes are initialized correctly
        self.assertEqual(self.thing.x, 0)
        self.assertEqual(self.thing.y, 0)
        self.assertEqual(self.thing.literal_name, "TestThing")
        self.assertTrue(self.thing.interactive)
        self.assertTrue(self.thing.collision)

    def test_properties(self):
        # Verifies that properties can be obtained and set correctly
        self.thing.literal_name = "NewThing"
        self.assertEqual(self.thing.literal_name, "NewThing")

        self.thing.interactive = False
        self.assertFalse(self.thing.interactive)

        self.thing.collision = False
        self.assertFalse(self.thing.collision)

    def test_str_method(self):
        # Verify that the __str__ method generates the expected string representation
        expected_str = "TestThing: coords=(0, 0), interactive=True, collision=True"
        self.assertEqual(str(self.thing), expected_str)

if __name__ == '__main__':
    unittest.main()