import sys
sys.path.insert(0, '.')

from utiles.commons.air import Air
import unittest

class TestAir(unittest.TestCase):

    def test_air_creation_default_values(self):
        """
        Test the creation of an Air instance with default values.

        This test verifies that creating an instance of Air without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Air".
        - interactive and collision should be False.
        """
        self.air = Air(3, 3)
        self.assertEqual(self.air.x, 3)
        self.assertEqual(self.air.y, 3)
        self.assertEqual(self.air.literal_name, "Air")
        self.assertFalse(self.air.interactive)
        self.assertFalse(self.air.collision)


    def test_air_creation_custom_values(self):
        """
        Test the creation of an Air instance with custom values.

        This test verifies that creating an instance of Air by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - x, y should be set to 0 by default.
        - literal_name should be "CustomAirAttribute".
        - interactive and collision should be True.
        """
        self.air = Air(1, 4, "CustomAirAttribute", True, True)
        self.assertEqual(self.air.x, 1)
        self.assertEqual(self.air.y, 4)
        self.assertEqual(self.air.literal_name, "CustomAirAttribute")
        self.assertTrue(self.air.interactive)
        self.assertTrue(self.air.collision)
 
    def test_air_creation_with_invalid_values(self):
        """
        Test the creation of an Air instance with invalid values.

        This test verifies that creating an instance of Air by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Air creation with invalid values...")
        with self.assertRaises(ValueError):
            self.air1 = Air("invalid", 1)
            self.air2 = Air(1, "invalid") 
            self.air3 = Air(None, 1) 
            self.air4 = Air(1, None)
            self.air5 = Air(1.1, 4) 
            self.air6 = Air(1, 4.1) 
            if not isinstance(self.air1.x, int) or not isinstance(self.air2.y, int) or not isinstance(self.air3.x, int) or not isinstance(self.air4.y, int) or not isinstance(self.air5.x, int) or not isinstance(self.air6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
if __name__ == '__main__':
    unittest.main()
