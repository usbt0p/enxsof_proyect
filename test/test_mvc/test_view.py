import sys
sys.path.insert(0, '.')
from utiles.objects import thing


import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from src.mvc.view import View
from utiles.agents import (agent)

class TestView(unittest.TestCase):

    def setUp(self) -> None:
        self.view = View("Test View", 400, 400)
        self.view.update = MagicMock()

    def test_resize_window(self) -> None:
        default_width_px = 198
        default_height_px = 4
        self.view.resize_window()
        self.assertEqual(self.view.winfo_reqwidth(), 400 + default_width_px)
        self.assertEqual(self.view.winfo_reqheight(), 400 + default_height_px)
        
    def test_set_controller(self) -> None:
        controller = MagicMock()
        self.view.set_controller(controller)
        self.assertEqual(self.view.controller, controller)

    def test_draw_grid(self) -> None:
        self.view.draw_grid(400, 400)
        self.assertEqual(len(self.view.canvas.find_withtag("grid_line")), 40)

    def test_updateFromNotification_agents(self) -> None:
        agents = ["Agent1", "Agent2", "Agent3"]
        self.view.draw_agents = MagicMock()
        self.view.updateFromNotification(agents=agents)
        self.view.draw_agents.assert_called_once_with(agents)

    def test_updateFromNotification_matrix(self) -> None:
        matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        self.view.draw_map = MagicMock()
        self.view.updateFromNotification(matrix=matrix)
        self.view.draw_map.assert_called_once_with(matrix)

    def test_draw_map(self) -> None:

            mockthing = thing.Thing(0, 0, "Test Thing")
            mockthing2 = thing.Thing(2, 0, "Test Thing")
            mockthing3 = thing.Thing(1, 1, "Test Thing")
            map = [[mockthing, 0, mockthing2], 
                    [0, mockthing3, 0], 
                    [mockthing, 0, mockthing]]
            self.view.canvas = MagicMock()
            self.view.img_dict = {
                "Test Thing": "image1",
            }
            self.view.draw_map(map)
            '''self.assertEqual(self.view.canvas.delete.call_count, 1)
            self.assertEqual(self.view.canvas.create_image.call_count, 5)'''
            self.view.canvas.create_image.assert_any_call(0, 0, image="image1", anchor='nw', tags="object")
            self.view.canvas.create_image.assert_any_call(80, 0, image="image1", anchor='nw', tags="object")
            self.view.canvas.create_image.assert_any_call(40, 40, image="image1", anchor='nw', tags="object")

            self.view.update.assert_called_once()

    def test_draw_agents(self) -> None:
        agent1, agent2 = agent.Agent("Agent1", 0, 0), agent.Agent("Agent2", 0, 0)

        agents = [agent1, agent2]
        self.view.canvas = MagicMock()
        self.view.img_dict = {
            "Agent1": "image1",
            "Agent2": "image2"
        }
        self.view.draw_agents(agents)
        self.assertEqual(self.view.canvas.delete.call_count, 1)
        self.assertEqual(self.view.canvas.create_image.call_count, 2)
        self.view.canvas.create_image.assert_any_call(0, 0, image="image1", anchor='nw', tags="agent")
        self.view.canvas.create_image.assert_any_call(0, 0, image="image2", anchor='nw', tags="agent")
        self.view.update.assert_called_once()

    def test_button1_clicked(self) -> None:
        self.view.controller = MagicMock()
        self.view.button1_clicked()
        self.view.controller.handle_click.assert_called_once_with("movement")

if __name__ == '__main__':
    unittest.main()


