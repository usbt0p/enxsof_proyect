import sys
sys.path.insert(0, '.')

from utiles.commons.fridge import Fridge
import unittest

class TestFridge(unittest.TestCase):

    def test_fridge_initialization(self):
        """
        Test the creation of a Fridge instance with default values.

        This test verifies that creating an instance of Fridge without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Fridge".
        - interactive should be True. 
        - collision should be False.
        - movable should be True.
        """
        self.fridge = Fridge(6, 8)
        self.assertEqual(self.fridge.x, 6)
        self.assertEqual(self.fridge.y, 8)
        self.assertEqual(self.fridge.literal_name, "Fridge")
        self.assertEqual(self.fridge.storage, {})
        self.assertTrue(self.fridge.interactive)
        self.assertFalse(self.fridge.collision)
        self.assertTrue(self.fridge.movable)


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
        self.fridge = Fridge(1, 4, {"view":"observer"}, "CustomFridgeAttribute", False, True, False)
        self.assertEqual(self.fridge.x, 1)
        self.assertEqual(self.fridge.y, 4)
        self.assertEqual(self.fridge.literal_name, "CustomFridgeAttribute")
        self.assertEqual(self.fridge.storage, {"view":"observer"})
        self.assertFalse(self.fridge.interactive)
        self.assertTrue(self.fridge.collision)
        self.assertFalse(self.fridge.movable)

    def test_fridge_creation_with_invalid_values(self):
        """
        Test the creation of a Fridge instance with invalid values.

        This test verifies that creating an instance of Fridge by 
        providing invalid values results in an expected exception.

        Assertions:
        - Case should raise a ValueError because x and y are not an integer.
        """
        with self.assertRaises(ValueError):
            self.fridge1 = Fridge("invalid", 1, {"view":"observer"},"Fridge") 
            self.fridge2 = Fridge(1, "invalid", {"view":"observer"},"Fridge") 
            self.fridge3 = Fridge(None, 1, {"view":"observer"},"Fridge") 
            self.fridge4 = Fridge(1, None, {"view":"observer"},"Fridge") 
            self.fridge5 = Fridge(1.1, 4, {"view":"observer"},"Fridge") 
            self.fridge6 = Fridge(1, 4.1, {"view":"observer"},"Fridge") 
            if not isinstance(self.fridge1.x, int) or not isinstance(self.fridge2.y, int) or not isinstance(self.fridge3.x, int) or not isinstance(self.fridge4.y, int) or not isinstance(self.fridge5.x, int) or not isinstance(self.fridge6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
           

if __name__ == '__main__':
    unittest.main()