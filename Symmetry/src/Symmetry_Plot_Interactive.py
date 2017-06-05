import os
import sys

from pylab import *
from mpl_toolkits.mplot3d import *

filename = sys.argv[1]

lines = open(filename, "r").readlines();

#X = [float(line.strip().split(" ")[0]) for line in lines]
#Y = [float(line.strip().split(" ")[1]) for line in lines]
#Z = [float(line.strip().split(" ")[2]) for line in lines]
X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]
Z = [float(line.strip().split()[2]) for line in lines]

filename = os.path.splitext(filename)[-2]
filename = filename.split("/")[-1]

S = set()
for i in range(len(X)):
    S.add((X[i], Y[i], Z[i]))

X = [s[0] for s in S]
Y = [s[1] for s in S]
Z = [s[2] for s in S]

fig = figure(figsize = (10, 10), dpi = 80)

ax = fig.add_subplot(111, projection = '3d')

for i in range(len(X)):
    ax.plot([0, X[i]], [0, Y[i]], [0, Z[i]], color = "grey", alpha = 0.1)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

ax.set_xticks([-1, 1])
ax.set_yticks([-1, 1])
ax.set_zticks([-1, 1])

ax.set_title(filename + " Symmetry")

ax.scatter(X, Y, Z)

show()
