import bct

import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"

mat_json = scipy.io.loadmat(mat_path)

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

x, y, z = mat_json['Coord'][:, 0], mat_json['Coord'][:, 1], mat_json['Coord'][:, 2]
# Creating plot
ax.scatter3D(x, y, z)
plt.show()
