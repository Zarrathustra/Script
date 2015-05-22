import sys
from pylab import *
import scipy.io as sio

x = [float(x) / 10 for x in range(10, 501)]
y = range(100, 3010, 10)

[X, Y] = meshgrid(x, y)

mat = sio.loadmat("3D_submodel01_z.mat");

Z = mat["Z"]

print size(X)
print size(Y)
print size(Z)

figure(figsize = (10, 10), dpi = 80)

ct = contour(X, Y, Z, colors = "k", linewidth = 40)
# ct = contourf(X, Y, Z, cmap = cm.bone, linewidth = 20)

clabel(ct, fontsize = 15, inline = 1, fmt = "%3.0f", manual = True)

show()
