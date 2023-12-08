
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random
import itertools

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
    heart_rate = random.randint(60, 140)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    
    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")

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

ani = animation.FuncAnimation(fig, update, interval=300, frames=itertools.count(), init_func=init, blit=True, cache_frame_data=False)

# Run the application
root.mainloop()
