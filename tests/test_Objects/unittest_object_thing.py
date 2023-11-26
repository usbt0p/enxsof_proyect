import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.thing import Thing

class TestThing(unittest.TestCase):  
    def test_thing_initialization(self):
        """
        Test the creation of a Thing instance with default values.

        This test verifies that the instance of Thing without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - interactive and collision should be True.
        - literal_name should be "Thing".
        - movable should be True.
        
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=True, movable=True)
        self.assertEqual(self.thing.x, 1)
        self.assertEqual(self.thing.y, 2)
        self.assertEqual(self.thing.literal_name, "Thing")
        self.assertTrue(self.thing.interactive)
        self.assertTrue(self.thing.collision)
        self.assertTrue(self.thing.movable)

    def test_thing_str_representation(self):
        """
        Test the creation of a Thing instance with the correct string representation.

        Verify the instance of Thing is represented like is expected to prove __str__ method.

        Assertions:
        - Represenation should be "Thing: coords=(1,2), interactive=True, collision=True,.
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=False, movable=True)
        expected_str = "Thing: coords=(1, 2), interactive=True, collision=False, movable=True"
        self.assertEqual(str(self.thing), expected_str)

    def test_thing_interactive_setter(self):
        """
        Test the interactive setter method of a Thing instance.

        This test verifies that the interactive setter method of Thing instance
        sets interactive attribute to True or False.

        Assertion:
        - interactive should be False.
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=True, movable=False)
        self.thing.interactive = False
        self.assertFalse(self.thing.interactive)

    def test_thing_collision_setter(self):
        """
        Test the collision setter method of a Thing instance.

        This test verifies that the collision setter method of Thing instance
        sets collision attribute to True or False.

        Assertion:
        - collision should be True.
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=False, movable=False)
        self.thing.collision = True
        self.assertTrue(self.thing.collision)

    def test_thing_movable_setter(self):
        """
        Test the movable setter method of a Thing instance.

        This test verifies that the movable setter method of Thing instance
        sets movable attribute to True or False.

        Assertion:
        - movable should be True.
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=False, movable=True)
        self.thing.movable = False
        self.assertFalse(self.thing.movable)


    def test_thing_literal_name_setter(self):
        """
        Test the literal_name setter method of a Thing instance.

        This test verifies that the literal_name setter method of Thing instance
        sets literal_name attribute to True or False.

        Assertion:
        - literal_name should be "Thing".
        """
        self.thing = Thing(1, 2, "Cosa", interactive=True, collision=True, movable=False)
        self.thing.literal_name = "Thing"
        self.assertEqual(self.thing.literal_name, "Thing")

    def test_thing_creation_with_invalid_values(self):
        """
        Test the creation of a Thing instance with invalid values.

        This test verifies that creating an instance of Thing by 
        providing invalid values results in an expected exception.

        Assertions:
        - Case should raise a ValueError because x and y are not an integer.
        """
        with self.assertRaises(ValueError):
            self.thing1 = Thing("invalid", 1, "Thing", True,True, True) 
            self.thing2 = Thing(1, "invalid", "Thing", True,True, True)
            self.thing3 = Thing(None, 1, "Thing", True,True, True) 
            self.thing4 = Thing(1, None, "Thing", True,True, True) 
            self.thing5 = Thing(1.1, 4, "Thing", True,True, True)
            self.thing6 = Thing(1, 4.1, "Thing", True,True, True) 
            if not isinstance(self.thing1.x, int) or not isinstance(self.thing2.y, int) or not isinstance(self.thing3.x, int) or not isinstance(self.thing4.y, int) or not isinstance(self.thing5.x, int) or not isinstance(self.thing6.y, int):    
                raise ValueError("Both x and y must be integers.")
            


if __name__ == '__main__':
    unittest.main()