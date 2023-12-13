import unittest
from unittest.mock import patch
from utiles.commons.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("John", 0, 0)

    def test_agent_pick_object(self):
        # Create a mock object
        mock_object = type('Object', (object,), {'x': 0, 'y': 0})()

        # Test picking up an object at the same position
        self.assertTrue(self.owner.agent_pick_object(mock_object))
        self.assertEqual(len(self.owner.inventory), 1)
        self.assertEqual(self.owner.inventory[0], mock_object)

        # Test picking up an object at a different position
        mock_object.x = 1
        self.assertFalse(self.owner.agent_pick_object(mock_object))
        self.assertEqual(len(self.owner.inventory), 1)

    def test_agent_drop_object(self):
        # Create a mock object
        mock_object = type('Object', (object,), {'x': 0, 'y': 0})()

        # Add an object to the inventory
        self.owner.inventory.append(mock_object)

        # Test dropping the object
        dropped_object = self.owner.agent_drop_object()
        self.assertEqual(dropped_object, mock_object)
        self.assertEqual(len(self.owner.inventory), 0)

if __name__ == '__main__':
    unittest.main()