import os
import sys

from pylab import *
from mpl_toolkits.mplot3d import *

filename = "../Data/HEALPix_Grid.txt"

lines = open(filename, "r").readlines();

x = [float(line.strip().split(" ")[0]) for line in lines]
y = [float(line.strip().split(" ")[1]) for line in lines]
z = [float(line.strip().split(" ")[2]) for line in lines]

fig = figure(figsize = (10, 10), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.set_title("HEALPix Grid")

savefig("../Figures/HEALPix_Grid.png", dpi = 300)
