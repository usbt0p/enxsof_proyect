import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random
import numpy as np
import itertools

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

    return p_wave + qrs_complex + t_wave

# Initialize the main window using Tkinter
root = tk.Tk()
root.title("Vital Constants Monitor")

# Create a frame for displaying the vital signs labels
label_frame = ttk.Frame(root)
label_frame.pack(pady=10)

# Labels for displaying various vital signs
heart_rate_label = tk.Label(label_frame, text="Heart Rate: -- bpm", font=("Helvetica", 16))
heart_rate_label.grid(row=0, column=0, padx=10)

blood_pressure_label = tk.Label(label_frame, text="Blood Pressure: --/--", font=("Helvetica", 16))
blood_pressure_label.grid(row=0, column=1, padx=10)

temperature_label = tk.Label(label_frame, text="Body Temperature: --°C", font=("Helvetica", 16))
temperature_label.grid(row=1, column=0, padx=10)

respiratory_rate_label = tk.Label(label_frame, text="Respiratory Rate: -- bpm", font=("Helvetica", 16))
respiratory_rate_label.grid(row=1, column=1, padx=10)

oxygen_saturation_label = tk.Label(label_frame, text="Oxygen Saturation: --%", font=("Helvetica", 16))
oxygen_saturation_label.grid(row=2, column=0, padx=10)

gcs_label = tk.Label(label_frame, text="Glasgow Coma Scale: --", font=("Helvetica", 16))
gcs_label.grid(row=2, column=1, padx=10)

# Creating a matplotlib figure with two subplots for heart rate and ECG
fig = Figure(dpi=110)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Setting titles and labels for the subplots
ax1.set_title("Heart Rate Over Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Heart Rate (bpm)")

ax2.set_title("ECG Waveform")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Amplitude")

# Initializing data lists for the plots
xdata1, ydata1 = [], []  # Data for heart rate plot
xdata2, ydata2 = [], []  # Data for ECG plot

# Styling for ax1 - Heart Rate plot
ax1.set_facecolor('#f0f8ff')  # Set background color to light azure
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='blue')  # Major grid lines
ax1.minorticks_on()
ax1.grid(which='minor', linestyle=':', linewidth='0.2', color='blue')  # Minor grid lines
ax1.set_xticks(np.arange(0, 60, 5))  # Major ticks every 5 seconds
ax1.set_xticks(np.arange(0, 60, 1), minor=True)  # Minor ticks every 1 second
ax1.set_yticks(np.arange(50, 150, 10))  # Major ticks every 10 bpm
ax1.set_yticks(np.arange(50, 150, 2), minor=True)  # Minor ticks every 2 bpm

# Styling for ax2 - ECG plot
ax2.set_facecolor('#FFF0F0')  # Set background color to light pink (ECG paper style)
ax2.grid(which='major', linestyle='-', linewidth='0.5', color='red')  # Major grid lines
ax2.set_xticks(np.arange(0, 2, 0.2))  # 0.2s intervals for x-axis
ax2.set_yticks(np.arange(-1, 1.5, 0.5))  # 0.5mV intervals for y-axis
ax2.grid(which='minor', linestyle=':', linewidth='0.2', color='red')  # Minor grid lines
ax2.set_xticks(np.arange(0, 2, 0.04), minor=True)  # 0.04s intervals for x-axis
ax2.set_yticks(np.arange(-1, 1.5, 0.1), minor=True)  # 0.1mV intervals for y-axis

# Line plots for heart rate and ECG
ln1, = ax1.plot([], [], color='#FF6848', linestyle='-', label='Heart Rate', animated=True)
ln2, = ax2.plot([], [], 'r-', label='ECG', animated=True)

# Adding legends to the plots
ax1.legend(loc="upper right")
ax2.legend(loc="upper right")

# Ensuring proper layout of the plots within the figure
fig.tight_layout()

def init():
    """
    Initialize the plot limits and return the line objects for animation.
    
    Returns:
    tuple: A tuple of line objects (ln1, ln2).
    """
    ax1.set_xlim(0, 50)  # Set initial x-axis limit for heart rate plot
    ax1.set_ylim(50, 150)  # Set y-axis limits for heart rate plot
    ax2.set_xlim(0, 2)  # Set initial x-axis limit for ECG plot
    ax2.set_ylim(-1, 1)  # Set y-axis limits for ECG plot
    return ln1, ln2

def update_vital(frame):
    """
    Update function for vital signs animation. Generates random data for vitals and updates the graph.

    Args:
    frame (int): The current frame number in the animation.

    Returns:
    tuple: A tuple containing the updated line object (ln1).
    """
    global heart_rate
    # Randomly generate new vital signs values
    heart_rate = random.randint(60, 140)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 99)
    gcs_score = random.randint(3, 15)

    # Formatting values for display
    formatted_heart_rate = f"{heart_rate:03}"
    formatted_gcs_score = f"{gcs_score:02}"

    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {formatted_heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")
    temperature_label.config(text=f"Body Temperature: {body_temperature}°C")
    respiratory_rate_label.config(text=f"Respiratory Rate: {respiratory_rate} bpm")
    oxygen_saturation_label.config(text=f"Oxygen Saturation: {oxygen_saturation}%")
    gcs_label.config(text=f"Glasgow Coma Scale: {formatted_gcs_score}")

    # Update heart rate graph
    xdata1.append(frame)
    ydata1.append(heart_rate)
    ln1.set_data(xdata1, ydata1)

    # Adjust x-axis limits for scrolling effect
    if len(xdata1) > 50:
        ax1.set_xlim(frame - 50, frame)

    # Maintain a fixed buffer size for the data
    buffer_length = 500
    if len(xdata1) > buffer_length:
        xdata1.pop(0)
        ydata1.pop(0)

    return (ln1,)

def update_ecg(frame):
    """
    Update function for the ECG waveform animation. Generates ECG waveform based on heart rate.

    Args:
    frame (int): The current frame number in the animation.

    Returns:
    tuple: A tuple containing the updated line object (ln2).
    """
    global heart_rate

    # Continuous time variable for ECG
    t = frame / 50

    # Generate ECG waveform data
    y = create_ecg_cycle(t, heart_rate)
    xdata2.append(t)
    ydata2.append(y)

    # Maintain a fixed buffer size for the data
    buffer_length = 500
    if len(xdata2) > buffer_length:
        xdata2.pop(0)
        ydata2.pop(0)

    # Update ECG line plot
    ln2.set_data(xdata2, ydata2)

    # Adjust x-axis limits for a scrolling effect
    if t > ax2.get_xlim()[1]:  
        ax2.set_xlim(ax2.get_xlim()[0] + 1.6, ax2.get_xlim()[1] + 1.6)

    return (ln2,)

# Embedding the matplotlib figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Creating animations for vital signs and ECG waveform
ani1 = animation.FuncAnimation(fig, update_vital, interval=500, frames=itertools.count(), init_func=init, blit=True, cache_frame_data=False)
ani2 = animation.FuncAnimation(fig, update_ecg, interval=20, frames=itertools.count(), init_func=init, blit=True, cache_frame_data=False)



# Starting the Tkinter event loop to run the application
if __name__ == "__main__":
    root.mainloop()
