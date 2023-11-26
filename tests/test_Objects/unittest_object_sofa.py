import sys
sys.path.insert(0, '.')

from utiles.commons.sofa import Sofa
import unittest

class TestSofa(unittest.TestCase):

    def test_sofa_initialization(self):
        """
        Test the creation of a Sofa instance with default values.

        This test verifies that creating an instance of Sofa without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Sofa".
        - interactive should be True.
        - collision should be False.
        - movable should be True.
        """
        self.sofa = Sofa(5, 5)
        self.assertEqual(self.sofa.x, 5)
        self.assertEqual(self.sofa.y, 5)
        self.assertEqual(self.sofa.literal_name, "Sofa")
        self.assertEqual(self.sofa.storage, [])
        self.assertTrue(self.sofa.interactive)
        self.assertFalse(self.sofa.collision)
        self.assertTrue(self.sofa.movable)


    def test_sofa_creation_custom_values(self):
        """
        Test the creation of a Sofa instance with custom values.

        This test verifies that creating an instance of Sofa by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomSofaAttribute".
        - interactive should be False.
        - collision should be True.
        - movable should be False.
        """
        self.sofa = Sofa(1, 4,[6,6], "CustomSofaAttribute", False,True, False)
        self.assertEqual(self.sofa.x, 1)
        self.assertEqual(self.sofa.y, 4)
        self.assertEqual(self.sofa.literal_name, "CustomSofaAttribute")
        self.assertEqual(self.sofa.storage, [6,6])
        self.assertFalse(self.sofa.interactive)
        self.assertTrue(self.sofa.collision)
        self.assertFalse(self.sofa.movable)

    def test_sofa_creation_with_invalid_values(self):
        """
        Test the creation of a Sofa instance with invalid values.

        This test verifies that creating an instance of Sofa by 
        providing invalid values results in an expected exception.

        Assertions:
        - Case should raise a ValueError because x and y are not an integer.
        """
        with self.assertRaises(ValueError):
            self.sofa1 = Sofa("invalid", 1, storage=(6,1))
            self.sofa2 = Sofa(1, "invalid", storage=(6,1)) 
            self.sofa3 = Sofa(None, 1, storage=(6,1)) 
            self.sofa4 = Sofa(1, None, storage=(6,1)) 
            self.sofa5 = Sofa(1.1, 4, storage=(6,1)) 
            self.sofa6 = Sofa(1, 4.1, storage=(6,1)) 
            if not isinstance(self.sofa1.x, int) or not isinstance(self.sofa2.y, int) or not isinstance(self.sofa3.x, int) or not isinstance(self.sofa4.y, int) or not isinstance(self.sofa5.x, int) or not isinstance(self.sofa6.y, int):    
                raise ValueError("Both x and y must be integers.")
            


if __name__ == '__main__':
    unittest.main()