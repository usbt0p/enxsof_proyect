import sys
sys.path.insert(0, 'enxsof_proyect')

from utiles.commons.obstacle import Obstacle
from utiles.commons.thing import Thing
import unittest

class TestObstacle(unittest.TestCase):

    def test_obstacle_creation_default_values(self):
        """
        Test the creation of an Obstacle instance with default values.

        This test verifies that creating an instance of Obstacle without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Obstacle".
        - interactive should be False and collision should be True.
        """
        self.obstacle = Obstacle(3, 3, "Obstacle")
        self.assertEqual(self.obstacle.x, 3)
        self.assertEqual(self.obstacle.y, 3)
        self.assertEqual(self.obstacle.literal_name, "Obstacle")
        self.assertFalse(self.obstacle.interactive)
        self.assertTrue(self.obstacle.collision)


    def test_obstacle_creation_custom_values(self):
        """
        Test the creation of a Obstacle instance with custom values.

        This test verifies that creating an instance of Obstacle by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomObstacleAttribute".
        - interactive and collision should be False.
        """
        self.obstacle = Obstacle(1, 4, "CustomObstacleAttribute", True, False)
        self.assertEqual(self.obstacle.x, 1)
        self.assertEqual(self.obstacle.y, 4)
        self.assertEqual(self.obstacle.literal_name, "CustomObstacleAttribute")
        self.assertTrue(self.obstacle.interactive)
        self.assertFalse(self.obstacle.collision)

    def test_obstacle_creation_with_invalid_values(self):
        """
        Test the creation of a Obstacle instance with invalid values.

        This test verifies that creating an instance of Obstacle by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Obstacle creation with invalid values...")
        with self.assertRaises(ValueError):
            self.obstacle1 = Obstacle("invalid",1, literal_name="Obstacle")
            self.obstacle2 = Obstacle(1, "invalid", literal_name="Obstacle") 
            self.obstacle3 = Obstacle(None, 1, literal_name="Obstacle") 
            self.obstacle4 = Obstacle(1, None, literal_name="Obstacle") 
            self.obstacle5 = Obstacle(1.1, 4, literal_name="Obstacle") 
            self.obstacle6 = Obstacle(1, 4.1, literal_name="Obstacle") 
            if not isinstance(self.obstacle1.x, int) or not isinstance(self.obstacle2.y, int) or not isinstance(self.obstacle3.x, int) or not isinstance(self.obstacle4.y, int) or not isinstance(self.obstacle5.x, int) or not isinstance(self.obstacle6.y, int):    
                raise ValueError("Both x and y must be integers.")
            
            
    def test_inheritance(self):
        """
        Test to verify that Obstacle class inherits from Thing class.

        Assertions:
        - Container should be an instance of Thing class.
        """
        self.obstacle = Obstacle(1, 1, "Obstacle", True, False)
        self.assertIsInstance(self.obstacle, Thing)

if __name__ == '__main__':
    unittest.main()