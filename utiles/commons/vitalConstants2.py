import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Initialize the plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(50, 150)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(random.randint(60, 100))  # Simulate heart rate
    ln.set_data(xdata, ydata)
    if len(xdata) > 50:  # Keep the x-axis moving
        ax.set_xlim(frame - 50, frame)
    return ln,

ani = animation.FuncAnimation(fig, update, frames=range(1000),
                              init_func=init, blit=True, interval=100)

plt.show()
