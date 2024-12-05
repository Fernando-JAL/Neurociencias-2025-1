import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.io
import seaborn as sns
import matplotlib.colors as colors
import matplotlib.cm as cmx

mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_dict = scipy.io.loadmat(mat_path)

cij = mat_dict['Coactivation_matrix']
cij = cij[:10, :10]
activation_dummy = cij# > 0.2
# activation_dummy = np.zeros(cij.shape)
# for idx in range(len(cij)):
#     maximum_idx_value_h = np.where(cij[idx, :] == max(cij[idx, :]))[0]
#     maximum_idx_value_v = np.where(cij[:, idx] == max(cij[:, idx]))[0]
#     activation_dummy[idx, maximum_idx_value_h] = cij[idx, maximum_idx_value_h]
#     activation_dummy[maximum_idx_value_v, idx] = cij[maximum_idx_value_v, idx]

sns.heatmap(cij, cmap='jet')
plt.show()
sns.heatmap(activation_dummy, cmap='jet')
plt.show()


G = nx.from_numpy_array(activation_dummy)
nodes = mat_dict['Coord']
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])
# choose color map
color_values = [activation_dummy[u, v] for u, v in G.edges()]
jet = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=min(color_values), vmax=max(color_values))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

def init():
    ax.scatter(*nodes.T, alpha=0.2, s=30, color="blue")
    for idx, vizedge in enumerate(edges):
        colorVal = scalarMap.to_rgba(color_values[idx])
        ax.plot(*vizedge.T, color=colorVal, linewidth=3.0)
    ax.grid(False)
    ax.set_axis_off()z
    plt.tight_layout()
    return


def _frame_update(index):
    ax.view_init(index * 0.2, index * 0.5)
    return


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# ani = animation.FuncAnimation(
#     fig,
#     _frame_update,
#     init_func=init,
#     interval=50,
#     cache_frame_data=False,
#     frames=100,
# )
init()
plt.colorbar(scalarMap)
plt.show()

degrees = dict(G.degree())
plt.hist(degrees.values())
plt.show()
