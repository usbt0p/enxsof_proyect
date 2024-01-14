import sys
sys.path.insert(0, '.')

import unittest
from unittest.mock import patch
from utiles.commons.vitalsGenerator import generate_vital, gaussian_update

class TestVitalSigns(unittest.TestCase):
    """
    Test suite for testing the functions gaussian_update and generate_vital
    in the vitalsGenerator module.
    """

    def test_gaussian_update_normal(self):
        """
        Test the gaussian_update function under normal conditions without any
        abnormal shifts.
        """
        # Patching the random.gauss and random.random functions to control their output.
        with patch('random.gauss') as mock_gauss, patch('random.random') as mock_random:
            # Setting the return values of the mocked functions.
            mock_gauss.return_value = 75  # Fixed value for Gaussian distribution
            mock_random.return_value = 0.1  # Low chance, no abnormal shift applied

            # Call the gaussian_update function with specific parameters.
            result = gaussian_update(70, 80, 5, 40, 180)

            # Assert that the result falls within a reasonable range, considering the function logic.
            self.assertTrue(74 <= result <= 76)

    def test_gaussian_update_abnormal(self):
        """
        Test the gaussian_update function when an abnormal shift is applied.
        """
        # Patching the random.gauss and random.random functions to control their output.
        with patch('random.gauss') as mock_gauss, patch('random.random') as mock_random:
            # Define parameters for gaussian_update call.
            current_value = 70
            average = 80
            std_dev = 5
            min_val = 40
            max_val = 180
            abnormal_chance = 1
            abnormal_shift = 10

            # Setting the return values of the mocked functions.
            mock_gauss.return_value = 85  # Fixed value for Gaussian distribution
            mock_random.return_value = 0  # High chance, abnormal shift applied

            # Calculate the expected result based on the specific logic of gaussian_update.
            adjusted_average = average + abnormal_shift
            expected_new_value = 85 + (current_value - adjusted_average) * 0.1
            expected_result = round(max(min(expected_new_value, max_val), min_val), 1)

            # Call the gaussian_update function with specific parameters.
            result = gaussian_update(current_value, average, std_dev, min_val, max_val, abnormal_chance, abnormal_shift)
            
            # Check if the result is within a small range of the expected value.
            self.assertTrue(expected_result - 1 <= result <= expected_result + 1)

    def test_generate_vital(self):
        """
        Test the generate_vital function to ensure it correctly updates all vital signs.
        """
        # Patching the gaussian_update function from the vitalsGenerator module.
        with patch('utiles.commons.vitalsGenerator.gaussian_update') as mock_gaussian_update:
            # Mock the return values for each call to gaussian_update.
            # These values correspond to the expected updated vital signs.
            mock_gaussian_update.side_effect = [70, 120, 80, 37, 18, 98, 15]

            # Call the generate_vital function with specific parameters.
            result = generate_vital(0, 0)

            # Define the expected tuple of updated vital signs.
            expected = (70, "120/80", 37, 18, 98, 15)

            # Assert that the result matches the expected outcome.
            self.assertEqual(result, expected)

# Entry point for running the tests.
if __name__ == '__main__':
    unittest.main()
