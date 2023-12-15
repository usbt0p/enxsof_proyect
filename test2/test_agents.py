
import unittest

from src.mvc.model import Model
from utiles.commons import agent


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model(16, 16)
        
    def test_generate_agents(self):
    # Verifica que se generen agentes correctamente
        agent1 = agent.Agent("Agente1", 3, 4)
        agent2 = agent.Agent("Agente2", 5, 6)

        self.model.generate_agents(agent1, agent2)

        self.assertEqual(len(self.model.agents), 2)
        self.assertIn(agent1, self.model.agents)
        self.assertIn(agent2, self.model.agents)
    
    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
