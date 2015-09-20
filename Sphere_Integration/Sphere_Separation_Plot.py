from pylab import *
from mpl_toolkits.mplot3d import *

from Sphere_Separation import *

x = []
y = []
z = []
for point in seperateSphere(1000):
    x.append(point[0])
    y.append(point[1])
    z.append(point[2])

fig = figure(figsize = (10, 10), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.set_title("Pseudo-Even Sphere Seperation")

savefig("../Figures/Sphere_Seperation.png", dpi = 300)
