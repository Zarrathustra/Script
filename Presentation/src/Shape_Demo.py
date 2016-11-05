from pylab import *
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

grid = mgrid[0.2:0.8:2j, 0.2:0.8:2j].reshape(2, -1).T

print "Grid Coordinates:\n", grid

def label(xy, msg):
    y = xy[1] - 0.25
    text(xy[0], y, msg, ha = "center", family = "sans-serif", size = 14)

fig, ax = subplots()

patches = []

# add a cirlce

circle = mpatches.Circle(grid[0], 0.2, ec = "none")
patches.append(circle)
label(grid[0], "Circle")

# add a rectangle

rect = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.2, ec = "none")
patches.append(rect)
label(grid[1], "Rectangle")

# add a wedge

wedge = mpatches.Wedge(grid[2], 0.2, 30, 270, ec = "none")
patches.append(wedge)
label(grid[2], "Wedge")

# add a Polygon

polygon = mpatches.RegularPolygon(grid[3], 5, 0.2)
patches.append(polygon)
label(grid[3], "Polygen")

colors = linspace(0, 1, len(patches))

collection = PatchCollection(patches, cmap = cm.hsv, alpha = 0.3)
collection.set_array(array(colors))

ax.add_collection(collection)

# fill this figure
subplots_adjust(left = 0.1, \
                right = 0.9, \
                bottom = 0.1, \
                top = 0.9)

# make X axis and Y axis have the same length
axis('equal')

# do not display axis
axis('off')

fig.savefig("../Figures/Shape_Demo.png", dpi = 200)
