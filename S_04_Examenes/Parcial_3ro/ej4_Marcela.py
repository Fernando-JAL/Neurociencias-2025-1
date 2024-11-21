import numpy as np
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from matplotlib import animation

path = r"/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
def open_mat_file(path: str):
    mat_json = scipy.io.loadmat(path)
    keys = list(mat_json.keys())
    lista = []
    for idx in range(3, len(mat_json.keys())) :
        lista.append(mat_json[keys[idx]])
    return mat_json, lista
json, [CM, coord] = open_mat_file(path)

x,y,z = coord[:,0], coord[:,1], coord[:,2]

cm = pd.DataFrame(CM)
cm[cm<=0.2]= 0
G = nx.from_pandas_adjacency(cm, create_using=nx.DiGraph)
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

sns.heatmap(cm)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

def init():
    # Se grafican los nodos
    ax.scatter(x, y, z)  # Equivalente a ax.scatter(x, y, z)
    # Se grafican las aristas
    for edge in edges:
        ax.plot(*edge.T)
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()
G = nx.from_pandas_adjacency(cm, create_using=nx.DiGraph())
nx.draw_networkx(G, arrows=True)
plt.show()
