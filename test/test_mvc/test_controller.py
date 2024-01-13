import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import MagicMock
from src.mvc.controller import Controller
from utiles.agents import agent
import unittest
from unittest.mock import MagicMock
from src.mvc.controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.model = MagicMock()
        self.view = MagicMock()
        self.event_manager = MagicMock()
        self.controller = Controller(self.model, self.view, self.event_manager)

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
        self.controller.move_randomly.assert_called_once_with(path, agent_index, path[0])

    def test_updateFromNotification_invalid_key(self):
        invalid_key = 'invalid_key'
        with self.assertRaises(KeyError):
            self.controller.updateFromNotification(invalid_key=0)

    def test_add_agent(self):
        agent_name = "Agent1"
        x, y  = 0, 0
        new_agent = MagicMock()
        self.controller.model.create_agent = MagicMock(return_value=new_agent)
        self.controller.model.generate_agents = MagicMock()
        self.controller.model.notify = MagicMock()
        self.controller.add_agent(agent_name, x, y)
        self.controller.model.create_agent.assert_called_once_with(agent_name, x, y)
        self.controller.model.generate_agents.assert_called_once_with(new_agent)
        self.controller.model.notify.assert_called_once_with(self.controller.view, agents=self.controller.model.agents)

    def test_remove_agent(self):
        agent_name = "Agent1"
        self.controller.model.remove_agent = MagicMock()
        self.controller.view.update_view = MagicMock()
        self.controller.remove_agent(agent_name)
        self.controller.model.remove_agent.assert_called_once_with(agent_name)
        self.controller.view.update_view.assert_called_once()

    def test_handle_owner_event(self):
        event = "owner_event"
        agent_index = 0
        self.controller.model.agents = [MagicMock()]
        self.controller.model.notify = MagicMock()
        self.controller.handle_click(event)
        self.controller.model.agents[agent_index].owner_event.assert_called_once()
        self.controller.model.notify.assert_called_once_with(self.controller.view, agents=self.controller.model.agents)

    def test_handle_enfermera_event(self):
        event = "enfermera_event"
        agent_index = 0
        self.controller.model.agents = [MagicMock()]
        self.controller.model.notify = MagicMock()
        self.controller.handle_click(event)
        self.controller.model.agents[agent_index].enfermera_event.assert_called_once()
        self.controller.model.notify.assert_called_once_with(self.controller.view, agents=self.controller.model.agents)

    def test_parse_command_speed(self):
        command = "speed 1000"
        self.controller.parse_command(command)
        self.assertEqual(self.controller.animation_speed, 1000)

    def test_parse_command_tp(self):
        command = "tp 1 2 3 4"
        self.controller.model.object_teleport = MagicMock()
        self.controller.model.notify = MagicMock()
        self.controller.parse_command(command)
        self.controller.model.object_teleport.assert_called_once_with(1, 2, 3, 4)
        self.controller.model.notify.assert_called_once_with(self.controller.view, matrix=self.controller.model.matrix)

    def test_parse_command_spawn_agent(self):
        command = "spawn agent 0 0"
        self.controller.spawn_agent = MagicMock()
        self.controller.parse_command(command)
        self.controller.spawn_agent.assert_called_once_with(['spawn', 'Gato', '0', '0'], self.controller.check_numeric_arguments)

if __name__ == '__main__':
    unittest.main()