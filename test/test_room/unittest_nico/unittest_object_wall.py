from utiles.commons.wall import Wall
import unittest

class TestWall(unittest.TestCase):

    def test_wall_creation_default_values(self):
        """
        Test the creation of a Wall instance with default values.

        This test verifies that creating an instance of Wall without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Wall".
        - interactive should be False and collision should be True.
        """
        self.wall = Wall(2, 2)
        self.assertEqual(self.wall.x, 2)
        self.assertEqual(self.wall.y, 2)
        self.assertEqual(self.wall.literal_name, "Wall")
        self.assertFalse(self.wall.interactive)
        self.assertTrue(self.wall.collision)


    def test_wall_creation_custom_values(self):
        """
        Test the creation of a Wall instance with custom values.

        This test verifies that creating an instance of Wall by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomWallAttribute".
        - interactive and collision should be True.
        """
        self.wall = Wall(1, 4, "CustomWallAttribute", True, False)
        self.assertEqual(self.wall.x, 1)
        self.assertEqual(self.wall.y, 4)
        self.assertEqual(self.wall.literal_name, "CustomWallAttribute")
        self.assertTrue(self.wall.interactive)
        self.assertFalse(self.wall.collision)

    def test_wall_creation_with_invalid_values(self):
        """
        Test the creation of a Wall instance with invalid values.

        This test verifies that creating an instance of Wall by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Wall creation with invalid values...")
        with self.assertRaises(ValueError):
            self.wall1 = Wall("invalid", 1)
            self.wall2 = Wall(1, "invalid") 
            self.wall3 = Wall(None, 1) 
            self.wall4 = Wall(1, None)  
            self.wall5 = Wall(1.1, 4) 
            self.wall6 = Wall(1, 4.1) 
            if not isinstance(self.wall1.x, int) or not isinstance(self.wall2.y, int) or not isinstance(self.wall3.x, int) or not isinstance(self.wall4.y, int) or not isinstance(self.wall5.x, int) or not isinstance(self.wall6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
        with self.assertRaises(ValueError):
            self.wall7 = Wall(2, 1, literal_name=None) 
            self.wall8 = Wall(1, 2, literal_name=6) 
            self.wall9 = Wall(1, 2, literal_name=6.4) 
            if not isinstance(self.wall7.literal_name, str) or not isinstance(self.wall8.literal_name, str) or not isinstance(self.wall9.literal_name, str):
                raise TypeError("literal_name must be a string.")
        
        with self.assertRaises(ValueError):
            self.wall10 = Wall(1, 5, "Wall", interactive=3) 
            self.wall11 = Wall(1, 2, "Wall", interactive="boolean") 
            self.wall12 = Wall(1, 4, "Wall", True, collision=3) 
            self.wall13 = Wall(1, 4, "Wall", True, collision="collision") 
            if not isinstance(self.wall10.interactive, bool) or not isinstance(self.wall11.interactive, bool) or not isinstance(self.wall12.collision, bool) or not isinstance(self.wall13.collision, bool):
                raise TypeError("interactive and collision must be booleans.")
            

if __name__ == '__main__':
    unittest.main()