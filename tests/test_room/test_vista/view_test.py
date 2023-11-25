import unittest
from tkinter import Tk
from src.mvc.view import View, HouseModel

class TestView(unittest.TestCase):
    """Test suite for verifying the functionality of the View class"""

    def setUp(self):
        """Set up initial conditions for the tests"""
        self.root = Tk()  
        self.view = View("Test View", matrix=[], height=640, width=640)  

    def test_view_creation(self):
        """Test if the view is properly initialized"""
        self.assertIsInstance(self.view, View)  # Check if the instance is of the View class
        self.assertEqual(self.view.height, 640)  # Verify if the view's height matches the expected value
        self.assertEqual(self.view.width, 640)  # Verify if the view's width matches the expected value

    def test_update_view(self):
        """Test the update_view method functionality"""
        # TODO: Test the update_view method by verifying the canvas is updated correctly
        # For example, check if objects are drawn on the canvas after calling update_view()
        pass

    def tearDown(self):
        """Clean up after the tests"""
        self.root.destroy()  # Destroy the simulated window

if __name__ == '__main__':
    unittest.main()
