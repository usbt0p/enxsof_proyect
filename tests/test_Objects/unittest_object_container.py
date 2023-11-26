import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.container import Container
from utiles.commons.thing import Thing

class TestContainer(unittest.TestCase):

    def test_container_initialization(self):
        """
        Test the creation of a Container instance with default values.

        This test verifies that the instance of Container without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - interactive should be True.
        - collision should be False.
        - movable should be True.
        - storage should be a list.
        - literal_name should be "Container".
        """
        self.container = Container(1, 2, storage=[1,2], literal_name="Container")
        self.assertEqual(self.container.x, 1)
        self.assertEqual(self.container.y, 2)
        self.assertEqual(self.container.literal_name, "Container")
        self.assertEqual(self.container.storage, [1,2])
        self.assertTrue(self.container.interactive)
        self.assertFalse(self.container.collision)
        self.assertTrue(self.container.movable)

    def test_container_assignment(self):
        """
        Test the creation of a Container instance with new assigment for storage.

        Verify the instance of Container without providing a new storage
        value results in the expected default values for attributes and new updated
        attribute for prove the setter method.

        Assertions:
        - literal_name should be "Container".
        - interactive should be True.
        - collision should be False.
        - movable should be True.
        - storage should be [].
        - literal_name should be "Container".
        """
        self.container = Container(1, 2, storage=[1,2], literal_name="Container" )
        new_storage = [3,4,5]
        self.container.storage = new_storage
        self.assertEqual(self.container.x, 1)
        self.assertEqual(self.container.y, 2)
        self.assertEqual(self.container.literal_name, "Container")
        self.assertEqual(self.container.storage, new_storage)
        self.assertTrue(self.container.interactive)
        self.assertFalse(self.container.collision)
        self.assertTrue(self.container.movable)

    def test_str_representation(self):
        """
        Test the creation of a Container instance with the correct string representation.

        Verify the instance of Container it is represented like is expected to prove __str__ method.

        Assertions:
        - Represenation should be "Container: coords=(1,2), interactive=True, collision=False,
        movable=True, storage=[]"
        """
        self.container = Container(1,2,storage=[4,6], literal_name="Container")
        expected_str = "Container: coords=(1, 2), interactive=True, collision=False, movable=True, storage=[4, 6]"
        self.assertEqual(str(self.container), expected_str)

    def test_container_creation_custom_values(self):
        """
        Test the creation of a Container instance with custom values.

        Verify the instance of Container by providing specific
        values results in the expected default values for attributes.

        Assertions:
        - interactive and collision should be False.
        - storage should be a list.
        - literal_name should be "CustomContainer".
        """
        container = Container(2, 5,storage=[3,5], literal_name="CustomContainer", interactive=False, collision=False, movable=False)
        self.assertEqual(container.x, 2)
        self.assertEqual(container.y, 5)
        self.assertEqual(container.literal_name, "CustomContainer")
        self.assertEqual(container.storage,[3,5])
        self.assertFalse(container.interactive)
        self.assertFalse(container.collision)
        self.assertFalse(container.movable)
        
    def test_container_creation_with_invalid_values(self):
        """
        Test the creation of a Container instance with invalid values.

        This test verifies that creating an instance of Air by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a TypeError because x and y are not an integer.
        - Second case should raise a TypeError because literal_name is not an string.
        """
        with self.assertRaises(ValueError):
            self.container1 = Container("invalid", 1,storage=[2,3,4],literal_name="Container") 
            self.container2 = Container(1, "invalid",storage=[2,3,4],literal_name="Container")
            self.container3 = Container(None, 1,storage=[2,3,4],literal_name="Container") 
            self.container4 = Container(1, None,storage=[2,3,4],literal_name="Container") 
            self.container5 = Container(5.8, 1,storage=[2,3,4],literal_name="Container")
            self.container6 = Container(1, 4.1,storage=[2,3,4],literal_name="Container")
            if not isinstance(self.container1.x, int) or not isinstance(self.container2.y, int) or not isinstance(self.container3.x, int) or not isinstance(self.container4.y, int) or not isinstance(self.container5.x, int) or not isinstance(self.container6.y, int):    
                raise ValueError("Both x and y must be integers.")
        
        with self.assertRaises(TypeError):
            self.container7 = Container(1, 3,storage=[2,6,4], literal_name=4)  
            self.container8 = Container(1, 2,storage=[2,6,4], literal_name=4.1)  
            self.container9 = Container(1, 2,storage=[2,6,4], literal_name=True)  
            if not isinstance(self.container7.literal_name, str) or not isinstance(self.container8.literal_name, str) or not isinstance(self.container9.literal_name, str):
                raise TypeError("literal_name must be a string.")

    def test_inheritance(self):
        """
        Test to verify that Container class inherits from Thing class.

        Assertions:
        - Container should be an instance of Thing class.
        """
        self.container = Container(1, 2, storage=[1,2],literal_name="Container")
        self.assertIsInstance(self.container, Thing)

if __name__ == '__main__':
    unittest.main()