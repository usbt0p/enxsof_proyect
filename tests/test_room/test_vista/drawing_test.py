import sys
sys.path.insert(0, '.')

import unittest
from tkinter import Tk, Canvas
from src.mvc.view import View, HouseModel

class TestDrawGrid(unittest.TestCase):
    """Test suite for verifying the grid drawing functionality in the view"""

    def setUp(self):
        """Set up conditions for the test"""
        self.root = Tk()  # Create an instance of Tkinter to simulate a window
        self.canvas = Canvas(self.root)  # Create a canvas within the simulated window
        self.view = View("Test View", matrix=[], height=400, width=400)  # Create an instance of the View class
        self.view.canvas = self.canvas  # Assign the canvas to the view's canvas attribute

    def test_draw_grid(self):
        """Verify if the grid is drawn correctly on the canvas"""
        width = 400
        height = 400
        cell_size = self.view.CELL_SIZE  # Expected cell size

        # Call the draw_grid method
        self.view.draw_grid(width, height)

        # Check if grid lines are drawn at the correct intervals
        expected_horizontal_lines = height / cell_size
        expected_vertical_lines = width / cell_size

        # Get all the grid lines drawn on the canvas
        all_lines = self.canvas.find_withtag('grid_line')

        # Check if the number of horizontal and vertical lines match the expected count
        horizontal_lines = [line for line in all_lines if self.canvas.coords(line)[1] == self.canvas.coords(line)[3]]
        vertical_lines = [line for line in all_lines if self.canvas.coords(line)[0] == self.canvas.coords(line)[2]]

        self.assertEqual(len(horizontal_lines), expected_horizontal_lines)
        self.assertEqual(len(vertical_lines), expected_vertical_lines)

    def tearDown(self):
        """Clean up after the test"""
        self.root.destroy()  # Destroy the simulated window

if __name__ == '__main__':
    unittest.main()
