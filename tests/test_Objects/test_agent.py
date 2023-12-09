
import sys
sys.path.insert(0, '.')

import unittest
from utiles.commons.agent import Agent

class AgentTests(unittest.TestCase):

    def setUp(self):
        self.agent = Agent("Agent 1")

    def test_initial_position(self):
        self.assertEqual(self.agent.x, 0)
        self.assertEqual(self.agent.y, 0)

    def test_move_agent(self):
        self.agent.move_agent((3, 4))
        self.assertEqual(self.agent.x, 3)
        self.assertEqual(self.agent.y, 4)

    def test_print_position(self):
        # Redirigir la salida estándar para capturarla
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        self.agent.print_position()
        sys.stdout = sys.__stdout__  # Restaurar la salida estándar

        self.assertEqual(captured_output.getvalue().strip(), "(0, 0)")

    def test_str_representation(self):
        expected_str = f"Agent: Agent 1 at position {self.agent.position}"
        self.assertEqual(str(self.agent), expected_str)

if __name__ == '__main__':
    unittest.main()