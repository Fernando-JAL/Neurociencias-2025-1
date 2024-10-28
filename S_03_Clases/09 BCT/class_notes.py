import class_notes

import scipy.io
import matplotlib.pyplot as plt
import seaborn as sns

mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"

mat_json = scipy.io.loadmat(mat_path)

mat_dict = {k:v for k, v in mat_json.items() if k[0] != '_'}

fig = plt.figure(figsize=(15, 15))
ax = sns.heatmap(mat_dict['Coactivation_matrix'], cmap='hot')
plt.show()


fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection ="3d")
x, y, z = mat_dict['Coord'][:, 0], mat_dict['Coord'][:, 1], mat_dict['Coord'][:, 2]
# Creating plot
ax.scatter3D(x, y, z)
plt.show()
