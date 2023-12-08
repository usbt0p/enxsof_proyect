
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random
import numpy as np

# Create the main window
root = tk.Tk()
root.title("Vital Constants Monitor")

# Create a frame for the labels
label_frame = ttk.Frame(root)
label_frame.pack(pady=10)

# Create labels for displaying the vitals
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

# Create a matplotlib figure and axes for ECG and heart rate
fig, ax1 = plt.subplots(figsize=(5, 4), dpi=100)
xdata, ydata_ecg, ydata_hr = [], [], []
ln_ecg, = ax1.plot([], [], 'r-', animated=True)  # ECG waveform
ax2 = ax1.twinx()  # Create a second y-axis for heart rate
ln_hr, = ax2.plot([], [], 'b-', animated=True)  # Heart rate line

def init():
    ax1.set_xlim(0, 50)
    ax1.set_ylim(-2, 2)
    ax2.set_ylim(50, 150)
    return ln_ecg, ln_hr

def simulate_ecg(x, heart_rate):
    # Improved simulation of ECG based on heart rate
    # The frequency of the waveform changes with heart rate
    period = 60 / heart_rate
    return np.sin(2 * np.pi * x / period)

def update(frame):
    heart_rate = random.randint(60, 100)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 100)
    
    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")
    temperature_label.config(text=f"Body Temperature: {body_temperature}°C")
    respiratory_rate_label.config(text=f"Respiratory Rate: {respiratory_rate} bpm")
    oxygen_saturation_label.config(text=f"Oxygen Saturation: {oxygen_saturation}%")

    # Update the ECG graph and heart rate line
    xdata.append(frame)
    ydata_ecg.append(simulate_ecg(frame, heart_rate))
    ydata_hr.append(heart_rate)
    ln_ecg.set_data(xdata, ydata_ecg)
    ln_hr.set_data(xdata, ydata_hr)
    if len(xdata) > 50:
        ax1.set_xlim(frame - 50, frame)
    return ln_ecg, ln_hr

# Embed the figure in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

ani = animation.FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True, interval=10)

# Run the application
root.mainloop()
