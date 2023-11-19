import unittest
from utiles.commons.sofa import Sofa # TODO change path
class TestSofa(unittest.TestCase):

    def setUp(self):
        # Startup sttings for test
        self.sofa = Sofa(x=0, y=0)

    def test_initialization(self):
        # chek that the inizialization for test are correct
        self.assertEqual(self.sofa.x, 0)
        self.assertEqual(self.sofa.y, 0)
        self.assertEqual(self.sofa.literal_name, "Sofa")
        self.assertEqual(self.sofa.storage, ())
        self.assertTrue(self.sofa.interactive)
        self.assertTrue(self.sofa.collision)

    def test_custom_initialization(self):
        # Check initialization with custom parameters
        custom_sofa = Sofa(x=1, y=2, literal_name="CustomSofa", storage=("cushion", "blanket"), interactive=False, collision=False)
        self.assertEqual(custom_sofa.x, 1)
        self.assertEqual(custom_sofa.y, 2)
        self.assertEqual(custom_sofa.literal_name, "CustomSofa")
        self.assertEqual(custom_sofa.storage, ("cushion", "blanket"))
        self.assertFalse(custom_sofa.interactive)
        self.assertFalse(custom_sofa.collision)



if __name__ == '__main__':
    unittest.main()