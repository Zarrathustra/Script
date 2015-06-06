import sys
from pylab import *
import scipy.io as sio

x = [float(x) / 10 for x in range(10, 501)]
y = range(300, 1510, 10)

[X, Y] = meshgrid(x, y)

mat = sio.loadmat("3D_submodel02_z.mat");

Z = mat["Z"]

print size(X)
print size(Y)
print size(Z)

figure(figsize = (10, 10), dpi = 80)

ctf = contourf(X, Y, Z, cmap = cm.hot, linewidth = 20)

clabel(ctf, colors = "k", fontsize = 15, inline = 1, fmt = "%3.0f", manual = True)

show()
