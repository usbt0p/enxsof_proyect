
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random

# Function to create a single ECG cycle (from continuous_ecg.py)
def create_ecg_cycle(t, heart_rate):
    T = 60 / heart_rate
    p_duration = 0.25 * T
    qrs_duration = 0.1 * T
    t_duration = 0.4 * T

    p_wave = 0.1 * np.sin(2 * np.pi * t / p_duration) if t % T < p_duration else 0
    qrs_complex = 0.5 * np.sin(2 * np.pi * (t - p_duration) / qrs_duration) if p_duration <= t % T < p_duration + qrs_duration else 0
    t_wave = 0.2 * np.sin(2 * np.pi * (t - p_duration - qrs_duration) / t_duration) if p_duration + qrs_duration <= t % T < T else 0

    return p_wave + qrs_complex + t_wave

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

# Create a frame for the plots
plot_frame = ttk.Frame(root)
plot_frame.pack(pady=10)

# Create a Matplotlib figure with two subplots
fig = Figure(figsize=(10, 6), dpi=100)
ax1 = fig.add_subplot(211)  # For ECG
ax2 = fig.add_subplot(212)  # For other vital data (can be modified as needed)

# Initialize ECG plot
xdata, ydata = [], []
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax1.grid(which='minor', linestyle='-', linewidth='0.5', color=(1, 0.7, 0.7))
ln, = ax1.plot([], [], 'r-', linewidth=1)
ax1.set_xlim(0, 2)
ax1.set_ylim(-1, 1)

def init():
    return ln,

def update(frame):
    heart_rate = 140  # Example heart rate
    t = frame / 25
    y = create_ecg_cycle(t, heart_rate)
    xdata.append(t)
    ydata.append(y)

    if t > ax1.get_xlim()[1]:
        ax1.set_xlim(ax1.get_xlim()[0] + 1, ax1.get_xlim()[1] + 1)

    ln.set_data(xdata, ydata)
    return ln,

# Adding the Matplotlib figure to the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1000, 10000), init_func=init, blit=True, interval=1)

# Start the Tkinter event loop
root.mainloop()
