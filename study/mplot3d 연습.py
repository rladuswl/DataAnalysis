#%matplotlib notebook
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

r = np.linspace(0, 2, 100)
theta = np.linspace(0, 2 * np.pi, 100)
r, theta = np.meshgrid(r, theta)

z = 4 * r
x = r * np.cos(theta)
y = r * np.sin(theta)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, z, 50)
ax.contour3D(x, y, -z, 50)