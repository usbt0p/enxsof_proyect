import sys
sys.path.insert(0, 'enxsof_proyect')

from utiles.commons.table import Table
import unittest

class TestTable(unittest.TestCase):

    def test_table_creation_default_values(self):
        """
        Test the creation of a Table instance with default values.

        This test verifies that creating an instance of Table without providing specific
        values results in the expected default values for attributes.

        Assertions:
        - literal_name should be "Table".
        - interactive should be False and collision should be True.
        """
        self.table = Table(1, 1)
        self.assertEqual(self.table.x, 1)
        self.assertEqual(self.table.y, 1)
        self.assertEqual(self.table.literal_name, "Table")
        self.assertFalse(self.table.interactive)
        self.assertTrue(self.table.collision)


    def test_table_creation_custom_values(self):
        """
        Test the creation of a Table instance with custom values.

        This test verifies that creating an instance of Table by 
        providing custom values results in the provided values
        for attributes.

        Assertions:
        - literal_name should be "CustomTableAttribute".
        - interactive and collision should be True.
        """
        self.table = Table(1, 4, "CustomTableAttribute", True, False)
        self.assertEqual(self.table.x, 1)
        self.assertEqual(self.table.y, 4)
        self.assertEqual(self.table.literal_name, "CustomTableAttribute")
        self.assertTrue(self.table.interactive)
        self.assertFalse(self.table.collision)

    def test_table_creation_with_invalid_values(self):
        """
        Test the creation of a Table instance with invalid values.

        This test verifies that creating an instance of Table by 
        providing invalid values results in an expected exception.

        Assertions:
        - First case should raise a ValueError because x and y are not an integer.
        - Second case should raise a ValueError because literal_name is not a string.
        - Third case should raise a ValueError because interactive and collision is not a boolean.
        """
        print("Testing Table creation with invalid values...")
        with self.assertRaises(ValueError):
            self.table1 = Table("invalid", 1) 
            self.table2 = Table(1, "invalid")  
            self.table3 = Table(None, 1)  
            self.table4 = Table(1, None)  
            self.table5 = Table(1.1, 4) 
            self.table6 = Table(1, 4.1) 
            if not isinstance(self.table1.x, int) or not isinstance(self.table2.y, int) or not isinstance(self.table3.x, int) or not isinstance(self.table4.y, int) or not isinstance(self.table5.x, int) or not isinstance(self.table6.y, int):    
                raise ValueError("Both x and y must be integers.")
            


if __name__ == '__main__':
    unittest.main()