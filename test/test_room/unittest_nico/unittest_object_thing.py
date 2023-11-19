import unittest
from utiles.commons.thing import Thing

class TestContainer(unittest.TestCase):  
    def test_thing_initialization(self):
        """
        Test the creation of a Thing instance with default values.

        This test verifies that the instance of Thing without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - interactive and collision should be True.
        - literal_name should be "Thing".
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=True)
        self.assertEqual(self.thing.x, 1)
        self.assertEqual(self.thing.y, 2)
        self.assertEqual(self.thing.literal_name, "TestThing")
        self.assertTrue(self.thing.interactive)
        self.assertTrue(self.thing.collision)

    def test_thing_str_representation(self):
        """
        Test the creation of a Thing instance with the correct string representation.

        Verify the instance of Thing is represented like is expected to prove __str__ method.

        Assertions:
        - Represenation should be "Thing: coords=(1,2), interactive=True, collision=True,.
        """
        self.thing = Thing(1, 2, "Thing", interactive=True, collision=False)
        expected_str = "Thing: coords=(1, 2), interactive=True, collision=False"
        self.assertEqual(str(self.thing), expected_str)

    def test_thing_interactive_setter(self):
        """
        Test the interactive setter method of a Thing instance.

        This test verifies that the interactive setter method of Thing instance
        sets interactive attribute to True or False.

        Assertion:
        - interactive should be False.
        """
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
        self.thing.collision = True
        self.assertTrue(self.thing.collision)

    def test_literal_name_setter(self):
        """
        Test the literal_name setter method of a Thing instance.

        This test verifies that the literal_name setter method of Thing instance
        sets literal_name attribute to True or False.

        Assertion:
        - collision should be "Thing".
        """
        self.thing.literal_name = "Thing"
        self.assertEqual(self.thing.literal_name, "Thing")

    def test_thing_creation_with_invalid_values(self):
        """
        Test the creation of a Thing instance with invalid values.

        This test verifies that creating an instance of Thing by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Thing creation with invalid values...")
        with self.assertRaises(ValueError):
            self.thing1 = Thing("invalid", 1) 
            self.thing2 = Thing(1, "invalid") 
            self.thing3 = Thing(None, 1) 
            self.thing4 = Thing(1, None) 
            self.thing5 = Thing(1.1, 4) 
            self.thing6 = Thing(1, 4.1) 
            if not isinstance(self.thing1.x, int) or not isinstance(self.thing2.y, int) or not isinstance(self.thing3.x, int) or not isinstance(self.thing4.y, int) or not isinstance(self.thing5.x, int) or not isinstance(self.thing6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
        with self.assertRaises(ValueError):
            self.thing7 = Thing(2, 1, literal_name=None) 
            self.thing8 = Thing(1, 2, literal_name=6) 
            self.thing9 = Thing(1, 2, literal_name=6.4) 
            if not isinstance(self.thing7.literal_name, str) or not isinstance(self.thing8.literal_name, str) or not isinstance(self.thing9.literal_name, str):
                raise TypeError("literal_name must be a string.")
        
        with self.assertRaises(ValueError):
            self.thing10 = Thing(1, 5, "Door", interactive=3) 
            self.thing11 = Thing(1, 2, "Door", interactive="boolean") 
            self.thing12 = Thing(1, 4, "Door", True, collision=3) 
            self.thing13 = Thing(1, 4, "Door", False, collision="collision") 
            if not isinstance(self.thing10.interactive, bool) or not isinstance(self.thing11.interactive, bool) or not isinstance(self.thing12.collision, bool) or not isinstance(self.thing13.collision, bool):
                raise TypeError("interactive and collision must be a boolean.")


if __name__ == '__main__':
    unittest.main()