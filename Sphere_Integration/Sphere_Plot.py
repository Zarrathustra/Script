from pylab import *
from mpl_toolkits.mplot3d import *

import sys

lines = open("../Data/SpherePlot.txt", "r").readlines();

X = [float(line.strip().split(',')[1]) for line in lines]
Y = [float(line.strip().split(',')[2]) for line in lines]
Z = [float(line.strip().split(',')[3]) for line in lines]

fig = figure(figsize = (10, 10), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X, Y, Z)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.set_title("Integration Points of a Sphere")

savefig("../Figures/Integration_Points_Sphere.png", dpi = 300)
