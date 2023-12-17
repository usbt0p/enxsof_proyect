import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import patch
from utiles.commons.vitalsGenerator import generate_vital

class TestVitalsGenerator(unittest.TestCase):

    @patch('random.randint')
    @patch('random.uniform')
    def test_generate_vital(self, mock_uniform, mock_randint):
        # Mock the random functions to return specific values
        mock_randint.side_effect = [70, 120, 80, 18, 98, 10]
        mock_uniform.return_value = 37.2

        # Call the generate_vital function
        heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score = generate_vital()

        # Assert that the generated values are correct
        self.assertEqual(heart_rate, 70)
        # FIXME aosidfjaiosdfjioanmfdnv
        self.assertEqual(blood_pressure, "120/80")
        self.assertEqual(body_temperature, 37.2)
        self.assertEqual(respiratory_rate, 18)
        self.assertEqual(oxygen_saturation, 98)
        self.assertEqual(gcs_score, 10)

if __name__ == '__main__':
    unittest.main()