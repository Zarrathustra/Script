import os
import sys

from pylab import *
from mpl_toolkits.mplot3d import *

filename = "../Data/Random_Direction_3D.txt"

lines = open(filename, "r").readlines();

x = [float(line.strip().split(" ")[0]) for line in lines]
y = [float(line.strip().split(" ")[1]) for line in lines]
z = [float(line.strip().split(" ")[2]) for line in lines]

fig = figure(figsize = (10, 10), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

ax.set_title("Random Direction in 3D")

savefig("../Figures/Random_Direction_3D.png", dpi = 300)
