import os
import sys

from pylab import *
from mpl_toolkits.mplot3d import *

filename = "../Data/HEALPix_Grid.txt"

lines = open(filename, "r").readlines()

x = [float(line.strip().split(" ")[0]) for line in lines]
y = [float(line.strip().split(" ")[1]) for line in lines]
z = [float(line.strip().split(" ")[2]) for line in lines]

filename = "../Data/HEALPix_Coarse_Fine.txt"
lines = open(filename, "r").readlines();

fineX = [float(line.strip().split(" ")[0]) for line in lines]
fineY = [float(line.strip().split(" ")[1]) for line in lines]
fineZ = [float(line.strip().split(" ")[2]) for line in lines]

coarseX = fineX.pop(0);
coarseY = fineY.pop(0);
coarseZ = fineZ.pop(0);

fig = figure(figsize = (10, 10), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(x, y, z, alpha = 0.2)

ax.scatter(coarseX, coarseY, coarseZ, c = "green")
ax.scatter(fineX, fineY, fineZ, c = "red")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

ax.set_title("Neighbor Search Using HEALPix Framework")

savefig("../Figures/HEALPix_Coarse_Fine.png", dpi = 300)
