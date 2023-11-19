from utiles.commons.door import Door
from utiles.commons.obstacle import Obstacle
import unittest

class TestDoor(unittest.TestCase):

    def test_door_creation_default_values(self):
        """
        Test the creation of a door instance with default values.

        This test verifies that creating an instance of Door without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Door".
        - interactive and collision should be True.
        """
        self.door = Door(3, 3)
        self.assertEqual(self.door.x, 3)
        self.assertEqual(self.door.y, 3)
        self.assertEqual(self.door.literal_name, "Door")
        self.assertTrue(self.door.interactive)
        self.assertTrue(self.door.collision)


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
        self.door = Door(1, 4, "CustomDoorAttribute", False, False)
        self.assertEqual(self.door.x, 1)
        self.assertEqual(self.door.y, 4)
        self.assertEqual(self.door.literal_name, "CustomDoorAttribute")
        self.assertFalse(self.door.interactive)
        self.assertFalse(self.door.collision)

    def test_door_creation_with_invalid_values(self):
        """
        Test the creation of a Door instance with invalid values.

        This test verifies that creating an instance of Door by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Door creation with invalid values...")
        with self.assertRaises(ValueError):
            self.door1 = Door("invalid", 1) 
            self.door2 = Door(1, "invalid") 
            self.door3 = Door(None, 1) 
            self.door4 = Door(1, None) 
            self.door5 = Door(1.1, 4) 
            self.door6 = Door(1, 4.1) 
            if not isinstance(self.door1.x, int) or not isinstance(self.door2.y, int) or not isinstance(self.door3.x, int) or not isinstance(self.door4.y, int) or not isinstance(self.door5.x, int) or not isinstance(self.door6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
        with self.assertRaises(ValueError):
            self.door7 = Door(2, 1, literal_name=None) 
            self.door8 = Door(1, 2, literal_name=6) 
            self.door9 = Door(1, 2, literal_name=6.4) 
            if not isinstance(self.door7.literal_name, str) or not isinstance(self.door8.literal_name, str) or not isinstance(self.door9.literal_name, str):
                raise TypeError("literal_name must be a string.")
        
        with self.assertRaises(ValueError):
            self.door10 = Door(1, 5, "Door", 3) 
            self.door11 = Door(1, 2, "Door", "boolean") 
            self.door12 = Door(1, 4, "Door", True, 3) 
            self.door13 = Door(1, 4, "Door", True, "collision") 
            if not isinstance(self.door10.interactive, bool) or not isinstance(self.door11.interactive, bool) or not isinstance(self.door12.collision, bool) or not isinstance(self.door13.collision, bool):
                raise TypeError("interactive and collision must be a boolean.")

    def test_door_close(self):
        """
        Test the close method of a Door instance.

        This test verifies that the close method of Door instance
        sets the is_open attribute to False.

        Assertion:
        - is_open should be False.
        """
        self.door = Door(1, 2, "Door")
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
        self.door = Door(1, 2, "Door")
        self.door.open()
        self.assertTrue(self.door.is_open)

    def test_inheritance(self):
        """
        Test to verify that Door class inherits from Thing class.

        Assertions:
        - Door should be an instance of Obstacle class.
        """
        self.door = Door(1, 2, "Door")
        self.assertIsInstance(self.door, Obstacle)

if __name__ == '__main__':
    unittest.main()

