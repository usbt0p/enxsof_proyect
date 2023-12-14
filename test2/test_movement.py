import unittest
from src.mvc.model import Model
import utiles.commons.agent as agent

class TestModel(unittest.TestCase):
    
    def setUp(self):
        self.model = Model(16, 16)
            
    def test_move_object(self):
            
            initial_value = self.model.matrix[4][7]
            
            
            room = Model(16, 16)

            file_path = 'assets/default_16x16_room.json'

            room.populate_room(file_path)

            gato = agent.Agent("Gato", 7, 7)
            room.generate_agents(gato)

            room.object_teleport(7, 4, 1, 1)
            
            final_value = self.model.matrix[1][1]

            self.assertEqual(final_value, initial_value)
            
    def tearDown(self):
        # Realiza la limpieza de recursos si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
