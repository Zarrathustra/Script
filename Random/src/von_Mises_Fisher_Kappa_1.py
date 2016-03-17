import os
import sys

N = 10000

from pylab import *
from mpl_toolkits.mplot3d import *

filename = "../Data/von_Mises_Fisher_Kappa_1.txt"

lines = open(filename, "r").readlines();

# print lines[0].strip().split(" ")

x = [float(line.strip().split(" ")[0]) for line in lines]
y = [float(line.strip().split(" ")[1]) for line in lines]
z = [float(line.strip().split(" ")[2]) for line in lines]
w = [float(line.strip().split(" ")[3]) for line in lines]

fig = figure(figsize = (10, 10), dpi = 500)
ax = fig.add_subplot(111, projection = '3d')

cm = get_cmap("summer")

ax.scatter(x[:N], y[:N], z[:N], alpha = 0.5, c = w,
           vmin = min(w), vmax = max(w), cmap = cm,
           linewidth = 0)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

savefig("../Figures/von_Mises_Fisher_Kappa_1.png", dpi = 500)
