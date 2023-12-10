import sys
sys.path.insert(0, '.')

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random
import numpy as np
import itertools

global heart_rate
global blood_pressure
global body_temperature
global respiratory_rate
global oxygen_saturation
global gcs_score
global ecg

# Global variable for heart rate
heart_rate = 60  # Initializing to prevent crash due to uninitialized variable

def create_ecg_cycle(t, heart_rate):
    """
    Create a single ECG cycle based on time 't' and heart rate.

    Args:
    t (float): The time variable.
    heart_rate (int): The heart rate in beats per minute.

    Returns:
    float: The ECG waveform value at time 't'.
    """
    T = 60 / heart_rate  # Total time for one heart beat in seconds
    p_duration = 0.25 * T  # Duration of P wave
    qrs_duration = 0.1 * T  # Duration of QRS complex
    t_duration = 0.4 * T  # Duration of T wave

    # ECG waveform components (P wave, QRS complex, T wave)
    p_wave = 0.1 * np.sin(2 * np.pi * t / p_duration) if t % T < p_duration else 0
    qrs_complex = 0.5 * np.sin(2 * np.pi * (t - p_duration) / qrs_duration) if p_duration <= t % T < p_duration + qrs_duration else 0
    t_wave = 0.2 * np.sin(2 * np.pi * (t - p_duration - qrs_duration) / t_duration) if p_duration + qrs_duration <= t % T < T else 0

    ecg = p_wave + qrs_complex + t_wave

def generate_vital():
    """
    Update function for vital signs animation. Generates random data for vitals and updates the graph.

    Args:
    frame (int): The current frame number in the animation.

    Returns:
    tuple: A tuple containing the updated line object (ln1).
    """
    
    global heart_rate, blood_pressure, body_temperature, respiratory_rate, oxygen_saturation, gcs_score
    
    # Randomly generate new vital signs values
    heart_rate = random.randint(60, 140)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 99)
    gcs_score = random.randint(3, 15)

    