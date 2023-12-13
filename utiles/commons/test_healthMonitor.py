import unittest
from unittest.mock import patch,Mock
from utiles.commons.healthMonitor import update_vital

class TestHealthMonitor(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or objects
        pass

    def test_update_vital(self):
        # Mock the necessary labels and graph objects
        heart_rate_label = Mock()
        blood_pressure_label = Mock()
        temperature_label = Mock()
        respiratory_rate_label = Mock()
        oxygen_saturation_label = Mock()
        gcs_label = Mock()
        ln1 = Mock()
        ax1 = Mock()

        # Call the update_vital function
        result = update_vital(1, heart_rate_label, blood_pressure_label, temperature_label,
                              respiratory_rate_label, oxygen_saturation_label, gcs_label, ln1, ax1)

        # Assert that the labels and graph objects are updated correctly
        heart_rate_label.config.assert_called_with(text="Heart Rate: 001 bpm")
        blood_pressure_label.config.assert_called_with(text="Blood Pressure: 120/80")
        temperature_label.config.assert_called_with(text="Body Temperature: 37.0°C")
        respiratory_rate_label.config.assert_called_with(text="Respiratory Rate: 15 bpm")
        oxygen_saturation_label.config.assert_called_with(text="Oxygen Saturation: 98%")
        gcs_label.config.assert_called_with(text="Glasgow Coma Scale: 08")
        ln1.set_data.assert_called_with([1], [heart_rate])
        ax1.set_xlim.assert_called_with(0, 1)

        # Assert the return value
        self.assertEqual(result, (ln1,))

if __name__ == '__main__':
    unittest.main()