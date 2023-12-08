import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random

def update_vitals(frame, xdata, ydata, line):
    # Simulate heart rate, blood pressure, oxygen saturation, and respiratory rate
    heart_rate = random.randint(60, 100)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    oxygen_saturation = random.randint(95, 100)  # Typical range: 95-100%
    respiratory_rate = random.randint(12, 20)    # Typical range: 12-20 breaths per minute

    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")
    oxygen_saturation_label.config(text=f"Oxygen Saturation: {oxygen_saturation}%")
    respiratory_rate_label.config(text=f"Respiratory Rate: {respiratory_rate} breaths/min")

    # Update the graph
    xdata.append(frame)
    ydata.append(heart_rate)
    line.set_data(xdata, ydata)

    # Adjust the x-axis to show the last 50 data points
    if len(xdata) > 50:
        ax.set_xlim(frame - 50, frame)

    return line,

# Create the main window
root = tk.Tk()
root.title("Vital Constants Monitor")

# Create labels for displaying the vitals
heart_rate_label = tk.Label(root, text="Heart Rate: -- bpm", font=("Helvetica", 16))
heart_rate_label.pack(pady=10)

blood_pressure_label = tk.Label(root, text="Blood Pressure: --/--", font=("Helvetica", 16))
blood_pressure_label.pack(pady=10)

oxygen_saturation_label = tk.Label(root, text="Oxygen Saturation: --%", font=("Helvetica", 16))
oxygen_saturation_label.pack(pady=10)

respiratory_rate_label = tk.Label(root, text="Respiratory Rate: -- breaths/min", font=("Helvetica", 16))
respiratory_rate_label.pack(pady=10)

# Create a figure for the plot and add a subplot
fig = Figure()
ax = fig.add_subplot(111)
xdata, ydata = [], []
line, = ax.plot(xdata, ydata, 'r-')

# Embed the plot in a Tkinter Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Initialize the animation
ani = animation.FuncAnimation(fig, update_vitals, fargs=(xdata, ydata, line), frames=range(1000),
                              blit=True, interval=100)

# Run the application
root.mainloop()
