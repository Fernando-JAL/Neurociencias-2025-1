import numpy as np
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from matplotlib import animation

path = r"/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_json = scipy.io.loadmat(path)
mat_dict = {k: v for k, v in mat_json.items() if k[0] != '_'}

x,y,z = mat_dict['Coord'][:,0], mat_dict['Coord'][:,1], mat_dict['Coord'][:,2]

mat_dict = {k: v for k, v in mat_json.items() if k[0] != '_'}
cm = pd.DataFrame(mat_dict['Coactivation_matrix'])
G = nx.from_pandas_adjacency(cm, create_using=nx.DiGraph)

for node in G.nodes():
    edges = G[node]
    if edges:
        i_max = max(edges.items(), key=lambda x: x[1]['weight'])[0]
        for adj in list(edges.keys()):
            if adj != i_max:
                G.remove_edge(node, adj)

nx.draw(G, node_color='k', node_size=50)

cm_adj = nx.to_pandas_adjacency(G)
CM = cm_adj.to_numpy()

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(x, y, z, color='k')

for i in range(len(CM)):
    for j in range(len(CM)):
        peso = CM[i, j]
        if peso > 0:
            ax.plot(
                [x[i], x[j]],
                [y[i], y[j]],
                [z[i], z[j]],
            )

ax.view_init(elev=20., azim=30)
plt.show()