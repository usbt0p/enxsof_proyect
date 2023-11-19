from utiles.commons.fridge import Fridge 
import unittest
class TestFridge(unittest.TestCase):

    def setUp(self):
        # Initial setup for testing
        self.fridge = Fridge(x=0, y=0)

    def test_initialization(self):
        #Verify that attributes are initialized correctly
        self.assertEqual(self.fridge.x, 0)
        self.assertEqual(self.fridge.y, 0)
        self.assertEqual(self.fridge.literal_name, "Fridge")
        self.assertEqual(self.fridge.storage, {})
        self.assertTrue(self.fridge.interactive)
        self.assertTrue(self.fridge.collision)

    def test_custom_initialization(self):
        #Check initialization with custom parameters
        custom_fridge = Fridge(x=1, y=2, literal_name="CustomFridge", storage={"item": 3}, interactive=False, collision=False)
        self.assertEqual(custom_fridge.x, 1)
        self.assertEqual(custom_fridge.y, 2)
        self.assertEqual(custom_fridge.literal_name, "CustomFridge")
        self.assertEqual(custom_fridge.storage, {"item": 3})
        self.assertFalse(custom_fridge.interactive)
        self.assertFalse(custom_fridge.collision)

   

if __name__ == '__main__':
    unittest.main()