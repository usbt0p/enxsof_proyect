import unittest
from utiles.commons.mixed import Mixed
from utiles.commons.agent import Agent
class TestAgentMethods(unittest.TestCase):
    def test_agent_init(self):
        agent = Agent(name="test_agent", x=1, y=2)
        self.assertEqual(agent.name, "test_agent")
        self.assertEqual(agent.x, 1)
        self.assertEqual(agent.y, 2)
        self.assertEqual(agent.inventory, [])

    def test_agent_position(self):
        agent = Agent(name="test_agent")
        agent.position(3, 4)
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 4)

class TestMixedMethods(unittest.TestCase):
    def test_mixed_init(self):
        mixed = Mixed(4, 4, "Thing", {})
        self.assertEqual(mixed.x, 4)
        self.assertEqual(mixed.y, 4)
        self.assertEqual(mixed.literal_name, "Thing")
        self.assertEqual(mixed.storage, {})

    def test_add_storage(self):
        mixed = Mixed(0, 0, "TestMixed", {})
        mixed.add_storage(thing1=1, thing2=2)
        self.assertEqual(mixed.storage, {'thing1': 1, 'thing2': 2})
        
        mixed.add_storage(thing1=2, thing2=14)
        self.assertEqual(mixed.storage, {'thing1': 3, 'thing2': 16})

    def test_remove_stock(self):
        mixed = Mixed(0, 0, "TestMixed", {'thing1': 3, 'thing2': 16})
        mixed.remove_stock(thing1=1, thing2=2)
        self.assertEqual(mixed.storage, {'thing1': 2, 'thing2': 14})

        with self.assertRaises(ValueError):
            mixed.remove_stock(thing3=1)

if __name__ == '__main__':
    unittest.main()
