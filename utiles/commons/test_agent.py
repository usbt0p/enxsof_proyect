import unittest
from utiles.commons.agent import Agent

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent("Test Agent")

    def test_init(self):
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.inventory, [])
        self.assertEqual(self.agent.x, 0)
        self.assertEqual(self.agent.y, 0)

    def test_print_position(self):
        self.assertEqual(self.agent.print_position(), "(0, 0)")

    def test_position(self):
        self.agent.position(2, 3)
        self.assertEqual(self.agent.x, 2)
        self.assertEqual(self.agent.y, 3)

    def test_str(self):
        self.assertEqual(str(self.agent), "Agent: Test Agent at position (0, 0)")

    def test_animate_movement(self):
        movements = [(1, 1), (2, 2), (3, 3)]
        self.agent.animate_movement(movements)
        # Add assertions to validate the movement animation if needed

if __name__ == '__main__':
    unittest.main()