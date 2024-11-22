import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.io

fig = plt.figure(figsize = (15, 15))
ax = plt.axes(projection="3d")

mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_dict = scipy.io.loadmat(mat_path)

x, y, z = mat_dict['Coord'][:, 0], mat_dict['Coord'][:, 1], mat_dict['Coord'][:, 2]

n = len(mat_dict['Coord'])
random_sizes = np.random.randint(50, 200, size=n)

def init():
    ax.scatter3D(x, y, z, s=random_sizes, marker='<')
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

plt.show()
