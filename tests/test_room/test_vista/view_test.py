import sys
sys.path.insert(0, '.')

import unittest
import tkinter as tk
from src.mvc.view import View, HouseModel

class TestView(unittest.TestCase):
    """Test suite for verifying the functionality of the View class"""

    def setUp(self):
        """Set up initial conditions for the tests"""
        self.root = tk.Tk()
        self.view = View("Test View", matrix=[], agent_list=[], height=640, width=640)
        self.view.canvas = tk.Canvas(self.root)  # Assign the canvas to the view's canvas attribute
        self.view.canvas.pack()

    def test_view_creation(self):
        """Test if the view is properly initialized"""
        self.assertIsInstance(self.view, View)  # Check if the instance is of the View class
        self.assertEqual(self.view.height, 640)  # Verify if the view's height matches the expected value
        self.assertEqual(self.view.width, 640)  # Verify if the view's width matches the expected value

    def test_update_view(self):
        """Test the update_view method functionality"""
        # Call update_view method to simulate the update
        self.view.update_view()

        # Get all the objects drawn on the canvas
        all_objects = self.view.canvas.find_all()

        # Check if objects are drawn on the canvas
        self.assertGreater(len(all_objects), 0)  # Verify if there are objects drawn on the canvas

    def tearDown(self):
        """Clean up after the tests"""
        self.root.destroy()  # Destroy the simulated window

if __name__ == '__main__':
    unittest.main()