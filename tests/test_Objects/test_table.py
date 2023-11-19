import unittest
from utiles.commons.table import Table 



class TestTable(unittest.TestCase):

    def setUp(self):
        # Initial setup for testing
        self.table = Table(x=0, y=0)

    def test_initialization(self):
        # Verify that attributes are initialized correctly
        self.assertEqual(self.table.x, 0)
        self.assertEqual(self.table.y, 0)
        self.assertEqual(self.table.literal_name, "Table")
        self.assertFalse(self.table.interactive)
        self.assertTrue(self.table.collision)

    def test_custom_initialization(self):
        # Check initialization with custom parameters
        custom_table = Table(x=1, y=2, literal_name="CustomTable", interactive=True, collision=False)
        self.assertEqual(custom_table.x, 1)
        self.assertEqual(custom_table.y, 2)
        self.assertEqual(custom_table.literal_name, "CustomTable")
        self.assertTrue(custom_table.interactive)
        self.assertFalse(custom_table.collision)

    def test_interactive_property(self):
        # Verifica que la propiedad interactive se puede cambiar después de la inicialización
        self.table.interactive = True
        self.assertTrue(self.table.interactive)

    def test_collision_property(self):
        # Verifica que la propiedad collision se puede cambiar después de la inicialización
        self.table.collision = False
        self.assertFalse(self.table.collision)

    # Puedes agregar más pruebas según las funcionalidades específicas de la clase Table

if __name__ == '__main__':
    unittest.main()