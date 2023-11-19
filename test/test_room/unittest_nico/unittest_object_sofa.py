from utiles.commons.sofa import Sofa
import unittest

class TestSofa(unittest.TestCase):

    def test_sofa_creation_default_values(self):
        """
        Test the creation of a Sofa instance with default values.

        This test verifies that creating an instance of Sofa without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Sofa".
        - interactive and collision should be True.
        """
        self.sofa = Sofa(5, 5)
        self.assertEqual(self.sofa.x, 6)
        self.assertEqual(self.sofa.y, 8)
        self.assertEqual(self.sofa.literal_name, "Sofa")
        self.assertEqual(self.sofa.storage, ())
        self.assertTrue(self.sofa.interactive)
        self.assertTrue(self.sofa.collision)


    def test_sofa_creation_custom_values(self):
        """
        Test the creation of a Sofa instance with custom values.

        This test verifies that creating an instance of Sofa by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomSofaAttribute".
        - interactive and collision should be False.
        """
        self.sofa = Sofa(1, 4, "CustomSofaAttribute",(6,6), False, False)
        self.assertEqual(self.sofa.x, 1)
        self.assertEqual(self.sofa.y, 4)
        self.assertEqual(self.sofa.literal_name, "CustomSofaAttribute")
        self.assertEqual(self.sofa.storage, (6,6))
        self.assertFalse(self.sofa.interactive)
        self.assertFalse(self.sofa.collision)

    def test_sofa_creation_with_invalid_values(self):
        """
        Test the creation of a Sofa instance with invalid values.

        This test verifies that creating an instance of Sofa by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Sofa creation with invalid values...")
        with self.assertRaises(ValueError):
            self.sofa1 = Sofa("invalid", 1,"Sofa", storage=(6,1))
            self.sofa2 = Sofa(1, "invalid","Sofa", storage=(6,1)) 
            self.sofa3 = Sofa(None, 1,"Sofa", storage=(6,1)) 
            self.sofa4 = Sofa(1, None,"Sofa", storage=(6,1)) 
            self.sofa5 = Sofa(1.1, 4,"Sofa", storage=(6,1)) 
            self.sofa6 = Sofa(1, 4.1,"Sofa", storage=(6,1)) 
            if not isinstance(self.sofa1.x, int) or not isinstance(self.sofa2.y, int) or not isinstance(self.sofa3.x, int) or not isinstance(self.sofa4.y, int) or not isinstance(self.sofa5.x, int) or not isinstance(self.sofa6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
        with self.assertRaises(ValueError):
            self.sofa7 = Sofa(2, 1, literal_name=None, storage=(3, 0))
            self.sofa8 = Sofa(1, 2, literal_name=6, storage=(3, 0)) 
            self.sofa9 = Sofa(1, 2, literal_name=6.4, storage=(3, 0)) 
            if not isinstance(self.sofa7.literal_name, str) or not isinstance(self.sofa8.literal_name, str) or not isinstance(self.sofa9.literal_name, str):
                raise TypeError("literal_name must be a string.")
        
        with self.assertRaises(ValueError):
            self.sofa10 = Sofa(1, 5, "Sofa", storage=(3, 2), interactive=3) 
            self.sofa11 = Sofa(1, 2, "Sofa", storage=(3, 2), interactive="boolean") 
            self.sofa12 = Sofa(1, 4, "Sofa", storage=(3, 2), interactive=True, collision=3) 
            self.sofa13 = Sofa(1, 4, "Sofa", storage=(3, 2), interactive=True, collision="collision") 
            if not isinstance(self.sofa10.interactive, bool) or not isinstance(self.sofa11.interactive, bool) or not isinstance(self.sofa12.collision, bool) or not isinstance(self.sofa13.collision, bool):
                raise TypeError("interactive and collision must be a boolean.")


if __name__ == '__main__':
    unittest.main()