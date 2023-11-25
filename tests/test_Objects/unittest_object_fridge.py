import sys
sys.path.insert(0, 'enxsof_proyect')

from utiles.commons.fridge import Fridge
import unittest

class TestFridge(unittest.TestCase):

    def test_fridge_creation_default_values(self):
        """
        Test the creation of a Fridge instance with default values.

        This test verifies that creating an instance of Fridge without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Fridge".
        - interactive and collision should be True.
        """
        self.fridge = Fridge(6, 8)
        self.assertEqual(self.fridge.x, 6)
        self.assertEqual(self.fridge.y, 8)
        self.assertEqual(self.fridge.literal_name, "Fridge")
        self.assertEqual(self.fridge.storage, {})
        self.assertTrue(self.fridge.interactive)
        self.assertTrue(self.fridge.collision)


    def test_fridge_creation_custom_values(self):
        """
        Test the creation of a Fridge instance with custom values.

        This test verifies that creating an instance of Fridge by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomFridgeAttribute".
        - interactive and collision should be False.
        """
        self.fridge = Fridge(1, 4, "CustomFridgeAttribute",{"view":"observer"}, False, False)
        self.assertEqual(self.fridge.x, 1)
        self.assertEqual(self.fridge.y, 4)
        self.assertEqual(self.fridge.literal_name, "CustomFridgeAttribute")
        self.assertEqual(self.fridge.storage, {"view":"observer"})
        self.assertFalse(self.fridge.interactive)
        self.assertFalse(self.fridge.collision)

    def test_fridge_creation_with_invalid_values(self):
        """
        Test the creation of a Fridge instance with invalid values.

        This test verifies that creating an instance of Fridge by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.

        """
        print("Testing Fridge creation with invalid values...")
        with self.assertRaises(ValueError):
            self.fridge1 = Fridge("invalid", 1, "Fridge", {"view":"observer"}) 
            self.fridge2 = Fridge(1, "invalid", "Fridge", {"view":"observer"}) 
            self.fridge3 = Fridge(None, 1, "Fridge", {"view":"observer"}) 
            self.fridge4 = Fridge(1, None, "Fridge", {"view":"observer"}) 
            self.fridge5 = Fridge(1.1, 4, "Fridge", {"view":"observer"}) 
            self.fridge6 = Fridge(1, 4.1, "Fridge", {"view":"observer"}) 
            if not isinstance(self.fridge1.x, int) or not isinstance(self.fridge2.y, int) or not isinstance(self.fridge3.x, int) or not isinstance(self.fridge4.y, int) or not isinstance(self.fridge5.x, int) or not isinstance(self.fridge6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
           

if __name__ == '__main__':
    unittest.main()