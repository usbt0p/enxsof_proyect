import sys
sys.path.insert(0, '.')

import random

# Initial values for vital signs
heart_rate = 70
systolic_bp = 120
diastolic_bp = 80
body_temperature = 37.0
respiratory_rate = 16
oxygen_saturation = 98
gcs_score = 15

def gaussian_update(current_value, average, std_dev, min_val, max_val, abnormal_chance=0, abnormal_shift=0) -> float:
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

def generate_vital(abnormal_chance, abnormal_shift) -> tuple:
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