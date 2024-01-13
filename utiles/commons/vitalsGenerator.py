import sys
sys.path.insert(0, '.')

'''
import random


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
    body_temperature = round(random.uniform(36.5, 40.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 99)
    gcs_score = random.randint(3, 15)
    return heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score




def generate_vital():
    """
    Update function for vital signs animation. Generates realistic random data for vitals and updates the graph.

    Returns:
    tuple: A tuple containing the updated vital signs.
    """
    global heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score

    # Define realistic ranges for vital signs
    heart_rate_range = range(60, 100)
    systolic_bp_range = range(110, 130)
    diastolic_bp_range = range(70, 90)
    body_temp_range = (36.0, 37.5)
    respiratory_rate_range = range(12, 18)
    oxygen_saturation_range = range(95, 100)
    gcs_score_range = range(13, 15)

    # Simulate gradual changes in vital signs
    heart_rate += random.choice([-1, 0, 1])
    systolic_bp = random.choice([-1, 0, 1]) + random.choice(systolic_bp_range)
    diastolic_bp = random.choice([-1, 0, 1]) + random.choice(diastolic_bp_range)
    body_temperature += round(random.uniform(-0.1, 0.1), 1)
    respiratory_rate += random.choice([-1, 0, 1])
    oxygen_saturation += random.choice([-1, 0, 1])
    gcs_score = random.choice([-1, 0, 1]) + random.choice(gcs_score_range)

    # Ensure values stay within defined ranges
    heart_rate = max(min(heart_rate, max(heart_rate_range)), min(heart_rate_range))
    systolic_bp = max(min(systolic_bp, max(systolic_bp_range)), min(systolic_bp_range))
    diastolic_bp = max(min(diastolic_bp, max(diastolic_bp_range)), min(diastolic_bp_range))
    body_temperature = max(min(body_temperature, body_temp_range[1]), body_temp_range[0])
    respiratory_rate = max(min(respiratory_rate, max(respiratory_rate_range)), min(respiratory_rate_range))
    oxygen_saturation = max(min(oxygen_saturation, max(oxygen_saturation_range)), min(oxygen_saturation_range))
    gcs_score = max(min(gcs_score, max(gcs_score_range)), min(gcs_score_range))

    # Update global variables
    blood_pressure = f"{systolic_bp}/{diastolic_bp}"

    return heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score

'''


import random

# Initial values for vital signs
heart_rate = 70
systolic_bp = 120
diastolic_bp = 80
body_temperature = 37.0
respiratory_rate = 16
oxygen_saturation = 98
gcs_score = 15

def gaussian_update(current_value, average, std_dev, min_val, max_val, abnormal_chance=0, abnormal_shift=0):
    """
    Updates a vital sign value using a Gaussian distribution for realism.

    Parameters:
    - current_value: The current value of the vital sign.
    - average: The average (mean) value around which the vital sign normally fluctuates.
    - std_dev: Standard deviation, determining the range of fluctuation.
    - min_val: Minimum plausible value for the vital sign.
    - max_val: Maximum plausible value for the vital sign.
    - abnormal_chance: Probability of an abnormal shift (to simulate illness).
    - abnormal_shift: The amount by which the average is shifted in case of an abnormality.

    Returns:
    - Updated value of the vital sign.
    """
    # Randomly decide whether to apply an abnormal shift
    if random.random() < abnormal_chance:
        print("Abnormality detected!")
        average += abnormal_shift
    
    # Calculate new value based on Gaussian distribution
    new_value = random.gauss(average, std_dev) + (current_value - average) * 0.1

    # Ensure the value stays within defined limits
    return round(max(min(new_value, max_val), min_val),1)

def generate_vital(abnormal_chance, abnormal_shift):
    """
    Updates all vital signs.

    Returns:
    - A tuple containing the updated values of all vital signs.
    """
    global heart_rate, systolic_bp, diastolic_bp, body_temperature, respiratory_rate, oxygen_saturation, gcs_score
    

    # Update each vital sign using realistic parameters
    heart_rate = gaussian_update(heart_rate, 80, 5, 40, 180, abnormal_chance, abnormal_shift)
    systolic_bp = gaussian_update(systolic_bp, 120, 8, 70, 200, abnormal_chance, abnormal_shift)
    diastolic_bp = gaussian_update(diastolic_bp, 80, 5, 40, 120, abnormal_chance, abnormal_shift)
    body_temperature = gaussian_update(body_temperature, 37.0, 0.2, 34.0, 42.0, abnormal_chance, abnormal_shift)
    respiratory_rate = gaussian_update(respiratory_rate, 16, 2, 8, 30, abnormal_chance, abnormal_shift)
    oxygen_saturation = gaussian_update(oxygen_saturation, 98, 1, 70, 100, abnormal_chance, abnormal_shift)
    gcs_score = gaussian_update(gcs_score, 15, 0.5, 3, 15, abnormal_chance, abnormal_shift)

    return (heart_rate, f"{round(systolic_bp, 1)}/{round(diastolic_bp, 1)}", round(body_temperature, 1), round(respiratory_rate, 1), round(oxygen_saturation, 1), round(gcs_score, 1))