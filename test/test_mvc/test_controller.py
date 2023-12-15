import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.model = MagicMock()
        self.view = MagicMock()
        self.controller = Controller(self.model, self.view)

    def test_updateFromNotification_agent_move_right(self):
        agent_index = 0
        self.controller.model.agent_move_right = MagicMock()
        self.controller.updateFromNotification(agent_move_right=agent_index)
        self.controller.model.agent_move_right.assert_called_once_with(agent_index)

    def test_updateFromNotification_random_movement(self):
        agent_index = 0
        path = [(0, 0), (1, 1), (2, 2)]
        self.controller.model.path_generator = MagicMock(return_value=path)
        self.controller.move_randomly = MagicMock()
        self.controller.updateFromNotification(random_movement=agent_index)
        self.controller.move_randomly.assert_called_once_with(path, agent_index)

    def test_updateFromNotification_invalid_key(self):
        invalid_key = 'invalid_key'
        with self.assertRaises(KeyError):
            self.controller.updateFromNotification(invalid_key=0)

    def test_move_randomly(self):
        agent_index = 0
        path = [(0, 0), (1, 1), (2, 2)]
        self.controller.model.agents = [MagicMock()]
        self.controller.model.notify = MagicMock()
        self.controller.view.after = MagicMock()
        self.controller.move_randomly(path, agent_index)
        self.assertEqual(self.controller.model.agents[agent_index].x, 0)
        self.assertEqual(self.controller.model.agents[agent_index].y, 0)
        self.controller.model.notify.assert_called_once_with(self.controller.view, agents=self.controller.model.agents)
        self.controller.view.after.assert_called_once_with(1000, self.controller.move_randomly, path[1:], agent_index)

    def test_add_agent(self):
        agent_name = "Agent1"
        position = (0, 0)
        new_agent = MagicMock()
        self.controller.model.generate_agents = MagicMock(return_value=new_agent)
        self.controller.model.add_agent = MagicMock()
        self.controller.view.update_view = MagicMock()
        self.controller.add_agent(agent_name, position)
        self.controller.model.generate_agents.assert_called_once_with(agent_name, position)
        self.controller.model.add_agent.assert_called_once_with(new_agent)
        self.controller.view.update_view.assert_called_once()

    def test_remove_agent(self):
        agent_name = "Agent1"
        self.controller.model.remove_agent = MagicMock()
        self.controller.view.update_view = MagicMock()
        self.controller.remove_agent(agent_name)
        self.controller.model.remove_agent.assert_called_once_with(agent_name)
        self.controller.view.update_view.assert_called_once()

if __name__ == '__main__':
    unittest.main()