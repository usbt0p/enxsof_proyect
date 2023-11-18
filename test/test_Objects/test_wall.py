import unittest
from ...utiles.commons.wall import Wall # TODO change path
class TestWall(unittest.TestCase):

    def setUp(self):
        # Initial setup for testing
        self.wall = Wall(x=0, y=0)

    def test_initialization(self):
        # chek that the inizialization for test are correct
        self.assertEqual(self.wall.x, 0)
        self.assertEqual(self.wall.y, 0)
        self.assertEqual(self.wall.literal_name, "Wall")
        self.assertFalse(self.wall.interactive)
        self.assertTrue(self.wall.collision)

    def test_custom_initialization(self):
        # Check initialization with custom parameters
        custom_wall = Wall(x=1, y=2, literal_name="CustomWall", interactive=True, collision=False)
        self.assertEqual(custom_wall.x, 1)
        self.assertEqual(custom_wall.y, 2)
        self.assertEqual(custom_wall.literal_name, "CustomWall")
        self.assertTrue(custom_wall.interactive)
        self.assertFalse(custom_wall.collision)

   

if __name__ == '__main__':
    unittest.main()