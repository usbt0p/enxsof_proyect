import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from src.mvc.view import View

class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View("Test View", 400, 400)
        self.view.update = MagicMock()

    def test_resize_window(self):
        self.view.resize_window()
        self.assertEqual(self.view.winfo_reqwidth(), 400)
        self.assertEqual(self.view.winfo_reqheight(), 430)

    def test_set_controller(self):
        controller = MagicMock()
        self.view.set_controller(controller)
        self.assertEqual(self.view.controller, controller)

    def test_draw_grid(self):
        self.view.draw_grid(400, 400)
        self.assertEqual(len(self.view.canvas.find_withtag("grid_line")), 20)

    def test_updateFromNotification_agents(self):
        agents = ["Agent1", "Agent2", "Agent3"]
        self.view.draw_agents = MagicMock()
        self.view.updateFromNotification(agents=agents)
        self.view.draw_agents.assert_called_once_with(agents)

    def test_updateFromNotification_matrix(self):
        matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        self.view.draw_map = MagicMock()
        self.view.updateFromNotification(matrix=matrix)
        self.view.draw_map.assert_called_once_with(matrix)

if __name__ == '__main__':
    unittest.main()