
import unittest

from src.mvc.model import Model
from utiles.commons import agent


class TestModel(unittest.TestCase):
    """
    Unit tests for the Model class.
    """

    def setUp(self):
        self.model = Model(16, 16)
        self.agent = agent.Agent("Test Agent")
        
    def test_generate_agents(self):
        # Verifica que se generen agentes correctamente
        agent1 = agent.Agent("Agente1", 3, 4)
        agent2 = agent.Agent("Agente2", 5, 6)

        self.model.generate_agents(agent1, agent2)

        self.assertEqual(len(self.model.agents), 2)
        self.assertIn(agent1, self.model.agents)
        self.assertIn(agent2, self.model.agents)

    # Check correct initialization
    def test_init(self):
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.inventory, [])
        self.assertEqual(self.agent.x, 0)
        self.assertEqual(self.agent.y, 0)

    # Check correct position printing
    def test_print_position(self):
        self.assertEqual(self.agent.print_position(), "(0, 0)")

    # Check correct position setting
    def test_position(self):
        self.agent.position(2, 3)
        self.assertEqual(self.agent.x, 2)
        self.assertEqual(self.agent.y, 3)

    # Check correct string representation
    def test_str(self):
        self.assertEqual(str(self.agent), "Agent: Test Agent at position (0, 0)")
    
    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
