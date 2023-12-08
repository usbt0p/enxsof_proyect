import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random
import numpy as np

# Function to create a single ECG cycle
def create_ecg_cycle(t, heart_rate):
    T = 60 / heart_rate  # Total time for one heart beat in seconds
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

oxygen_saturation_label = tk.Label(label_frame, text="Oxygen Saturation: --%", font=("Helvetica", 16))
oxygen_saturation_label.grid(row=2, column=0, padx=10)

pulse_oximetry_label = tk.Label(label_frame, text="Pulse Oximetry: --%", font=("Helvetica", 16))
pulse_oximetry_label.grid(row=2, column=1, padx=10)

# Create a matplotlib figure with two subplots
fig = Figure(figsize=(5, 6), dpi=100)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

xdata1, ydata1 = [], []
xdata2, ydata2 = [], []

ax2.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax2.grid(which='minor', linestyle='-', linewidth='0.5', color=(1, 0.7, 0.7))

ln1, = ax1.plot([], [], 'r-', animated=True)
ln2, = ax2.plot([], [], 'r-', animated=True)

def init():
    ax1.set_xlim(0, 50)
    ax1.set_ylim(50, 150)
    ax2.set_xlim(0, 2)  # Set initial x-axis limit for ECG
    ax2.set_ylim(-1, 1)
    return ln1, ln2

# Update function for heart rate graph
def update_heart_rate(frame):
    heart_rate = random.randint(60, 100)
    xdata1.append(frame)
    ydata1.append(heart_rate)
    ln1.set_data(xdata1, ydata1)
    if len(xdata1) > 50:
        ax1.set_xlim(frame - 50, frame)
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    return ln1,

# Update function for ECG graph
def update_ecg(frame):
    t = frame / 25  # Continuous time variable for ECG
    y = create_ecg_cycle(t, 60)
    xdata2.append(t)
    ydata2.append(y)
    ln2.set_data(xdata2, ydata2)
    if t > ax2.get_xlim()[1]:  # Update x-axis limit as time progresses
        ax2.set_xlim(ax2.get_xlim()[0] + 1, ax2.get_xlim()[1] + 1)
    return ln2,

# Embed the figure in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Create two separate FuncAnimation objects
ani1 = animation.FuncAnimation(fig, update_heart_rate, frames=np.linspace(0, 1000, 1000), init_func=init, blit=True, interval=1000)
ani2 = animation.FuncAnimation(fig, update_ecg, frames=np.linspace(0, 1000, 1000), init_func=init, blit=True, interval=100)

# Run the application
root.mainloop()
