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
    # Time intervals for P, QRS, T waves based on heart rate
    T = 60 / heart_rate  # Total time for one heart beat in seconds
    p_duration = 0.25 * T
    qrs_duration = 0.1 * T
    t_duration = 0.4 * T

    # ECG wave components
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


# Create a matplotlib figure and axes
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(50, 150)
    return ln,

def update(frame):
    heart_rate = random.randint(60, 100)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 100)
    pulse_oximetry = random.randint(95, 100)
    
    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")
    temperature_label.config(text=f"Body Temperature: {body_temperature}°C")
    respiratory_rate_label.config(text=f"Respiratory Rate: {respiratory_rate} bpm")
    oxygen_saturation_label.config(text=f"Oxygen Saturation: {oxygen_saturation}%")
    pulse_oximetry_label.config(text=f"Pulse Oximetry: {pulse_oximetry}%")

    # Update the graph
    xdata.append(frame)
    ydata.append(heart_rate)
    ln.set_data(xdata, ydata)
    if len(xdata) > 50:
        ax.set_xlim(frame - 50, frame)
    return ln,

# Embed the figure in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

ani = animation.FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True, interval=1000)

# Run the application
root.mainloop()


# Initialize plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax.grid(which='minor', linestyle='-', linewidth='0.5', color=(1, 0.7, 0.7))
ln, = plt.plot([], [], 'r-', linewidth=1)

def init():
    ax.set_xlim(0, 2)  # Set initial x-axis limit to show 2 cycles
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    heart_rate = 60  # Example heart rate
    t = frame / 25  # Continuous time variable
    y = create_ecg_cycle(t, heart_rate)
    xdata.append(t)
    ydata.append(y)

    if t > ax.get_xlim()[1]:  # Update x-axis limit as time progresses
        ax.set_xlim(ax.get_xlim()[0] + 1, ax.get_xlim()[1] + 1)

    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1000, 10000), init_func=init, blit=True, interval=10)
plt.show()