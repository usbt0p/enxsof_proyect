import sys
sys.path.insert(0, '.')
import unittest
from unittest.mock import patch
from utiles.commons.healthMonitor import update_vital
from unittest.mock import Mock

class HealthMonitorTests(unittest.TestCase):

    @patch('random.randint')
    @patch('random.uniform')
    def test_update_vital(self, mock_uniform, mock_randint):
        frame = 1
        mock_randint.side_effect = [80, 120, 37, 15, 98, 10]
        mock_uniform.return_value = 36.7

        expected_heart_rate = "080"
        expected_blood_pressure = "120/80"
        expected_body_temperature = 36.7
        expected_respiratory_rate = 15
        expected_oxygen_saturation = 98
        expected_gcs_score = 10

        # Mock labels
        heart_rate_label = Mock()
        blood_pressure_label = Mock()
        temperature_label = Mock()
        respiratory_rate_label = Mock()
        oxygen_saturation_label = Mock()
        gcs_label = Mock()

        # Call the function
        result = update_vital(frame)

        # Assert the labels were updated correctly
        heart_rate_label.config.assert_called_with(text=f"Heart Rate: {expected_heart_rate} bpm")
        blood_pressure_label.config.assert_called_with(text=f"Blood Pressure: {expected_blood_pressure}")
        ln1 = Mock()
        xdata1 = [frame]
        ydata1 = [expected_heart_rate]

        temperature_label.config.assert_called_with(text=f"Body Temperature: {expected_body_temperature}°C")
        import matplotlib.pyplot as plt

            # ...

        ax1 = plt.subplot(111)  # Define ax1 variable

            # ...

        ax1.set_xlim.assert_called_with(frame - 50, frame)

    if __name__ == '__main__':
        unittest.main()