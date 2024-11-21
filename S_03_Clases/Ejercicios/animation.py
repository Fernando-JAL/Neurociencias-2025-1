import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize = (15, 15))
ax = plt.axes(projection="3d")

# Creating dataset
#x, y, z = mat_dict['Coord'][:, 0]
#n = len(mat_dict['Coord'])
#random_sizes = np.random.randint(5,28, size=n)

def init():
    ax.scatter3D(x, y, z, s = 200, marker = '<')
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

plt.show()
