
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
    p_wave = 0.1 * np.sin(2 * np.pi * t / p_duration) if t % T < p_duration else 0
    qrs_complex = 0.5 * np.sin(2 * np.pi * (t - p_duration) / qrs_duration) if p_duration <= t % T < p_duration + qrs_duration else 0
    t_wave = 0.2 * np.sin(2 * np.pi * (t - p_duration - qrs_duration) / t_duration) if p_duration + qrs_duration <= t % T < T else 0

    return p_wave + qrs_complex + t_wave

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

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1000, 10000), init_func=init, blit=True, interval=1)
plt.show()
