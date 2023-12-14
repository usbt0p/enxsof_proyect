import sys
sys.path.insert(0, '.')


import random
import numpy as np


# Global variable for heart rate
heart_rate = 60  # Initializing to prevent crash due to uninitialized variable
blood_pressure = "120/80"  # Example initialization
body_temperature = 36.6  # Example initialization
respiratory_rate = 16  # Example initialization
oxygen_saturation = 98  # Example initialization
gcs_score = 15  # Example initialization


def generate_vital():
    """
    Update function for vital signs animation. Generates random data for vitals and updates the graph.

    Args:
    frame (int): The current frame number in the animation.

    Returns:
    tuple: A tuple containing the updated line object (ln1).
    """
    
    
    # Randomly generate new vital signs values
    heart_rate = random.randint(60, 140)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 99)
    gcs_score = random.randint(3, 15)
    return heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score
