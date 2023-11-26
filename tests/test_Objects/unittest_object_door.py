import sys
sys.path.insert(0, '.')

from utiles.commons.door import Door
from utiles.commons.obstacle import Obstacle
import unittest

class TestDoor(unittest.TestCase):

    def test_door_initialization(self):
        """
        Test the creation of a door instance with default values.

        This test verifies that creating an instance of Door without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Door".
        - interactive should be True.
        - collision should be False.
        - movable should be False.
        """
        self.door = Door(3, 3)
        self.assertEqual(self.door.x, 3)
        self.assertEqual(self.door.y, 3)
        self.assertEqual(self.door.literal_name, "Door")
        self.assertTrue(self.door.interactive)
        self.assertFalse(self.door.collision)
        self.assertFalse(self.door.movable)


    def test_air_creation_custom_values(self):
        """
        Test the creation of a Door instance with custom values.

        This test verifies that creating an instance of Door by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomDoorAttribute".
        - interactive and collision should be False.
        """
        self.door = Door(1, 4, "CustomDoorAttribute", False, False, True)
        self.assertEqual(self.door.x, 1)
        self.assertEqual(self.door.y, 4)
        self.assertEqual(self.door.literal_name, "CustomDoorAttribute")
        self.assertFalse(self.door.interactive)
        self.assertFalse(self.door.collision)
        self.assertTrue(self.door.movable)

    def test_door_creation_with_invalid_values(self):
        """
        Test the creation of a Door instance with invalid values.

        This test verifies that creating an instance of Door by 
        providing invalid values results in an expected exception.

        Assertions:
        - Case should raise a ValueError because x and y are not an integer.
        """
        with self.assertRaises(ValueError):
            self.door1 = Door("invalid", 1) 
            self.door2 = Door(1, "invalid") 
            self.door3 = Door(None, 1) 
            self.door4 = Door(1, None) 
            self.door5 = Door(1.1, 4) 
            self.door6 = Door(1, 4.1) 
            if not isinstance(self.door1.x, int) or not isinstance(self.door2.y, int) or not isinstance(self.door3.x, int) or not isinstance(self.door4.y, int) or not isinstance(self.door5.x, int) or not isinstance(self.door6.y, int):    
                raise ValueError("Both x and y must be integers.")
            

    def test_door_close(self):
        """
        Test the close method of a Door instance.

        This test verifies that the close method of Door instance
        sets the is_open attribute to False.

        Assertion:
        - is_open should be False.
        """
        self.door = Door(1, 2)
        self.door.close()
        self.assertFalse(self.door.is_open)
    
    def test_door_open(self):
        """
        Test the close method of a Door instance.

        This test verifies that the close method of Door instance
        sets the is_open attribute to True.

        Assertion:
        - is_open should be True.
        """
        self.door = Door(1, 2)
        self.door.open()
        self.assertTrue(self.door.is_open)

    def test_inheritance(self):
        """
        Test to verify that Door class inherits from Thing class.

        Assertions:
        - Door should be an instance of Obstacle class.
        """
        self.door = Door(1, 2)
        self.assertIsInstance(self.door, Obstacle)

if __name__ == '__main__':
    unittest.main()

