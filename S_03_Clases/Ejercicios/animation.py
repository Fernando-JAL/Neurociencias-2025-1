import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize = (15, 15))
ax = plt.axes(projection="3d")

# Creating dataset
x = np.random.randint(80, size=200)
y = np.random.randint(60, size=200)
z = np.random.randint(100, size=200)

def init():
    ax.scatter3D(x, y, z)
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

plt.show()
