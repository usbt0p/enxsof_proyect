import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create a single ECG cycle
def create_ecg_cycle(t, heart_rate):
    # Time intervals for P, QRS, T waves based on heart rate
    T = 60 / heart_rate  # Total time for one heart beat in seconds
    p_duration = 0.25 * T
    qrs_duration = 0.1 * T
    t_duration = 0.4 * T

    # ECG wave components
    p_wave = 0.1 * np.sin(2 * np.pi * t / p_duration) if t < p_duration else 0
    qrs_complex = 0.5 * np.sin(2 * np.pi * (t - p_duration) / qrs_duration) if p_duration <= t < p_duration + qrs_duration else 0
    t_wave = 0.2 * np.sin(2 * np.pi * (t - p_duration - qrs_duration) / t_duration) if p_duration + qrs_duration <= t < T else 0

    return p_wave + qrs_complex + t_wave

# Initialize plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', linewidth=1)

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    t = frame / 25 % 1  # Normalized time for one ECG cycle (faster cycle)
    heart_rate = 140  # Example heart rate
    y = create_ecg_cycle(t, heart_rate)
    xdata.append(t)
    ydata.append(y)
    if len(xdata) > 100:  # Keep last 100 points
        xdata.pop(0)
        ydata.pop(0)
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=1)  # Reduced interval for quicker animation

# Show the plot indefinitely
while True:
    try:
        plt.show()
    except KeyboardInterrupt:
        break

