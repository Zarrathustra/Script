from pylab import *
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

def label(xy, msg):
    y = xy[1] - 0.25
    text(xy[0], y, msg, ha = "center", family = "sans-serif", size = 14)

fig, ax = subplots()

patches = []

# add 1st part

#part1 = mpatches.Polygon([[0.1 + 0.4 / 3, 0.5], [0.1 + 0.8 / 3, 0.9]], \
#                         color = 'red')

part1 = mpatches.Polygon([[0.1 + 0.4 / 3 * 2, 0.1 + 0.8 / 3 * 2], \
                          [0.5, 0.9], \
                          [0.9 - 0.4 / 3 * 2, 0.1 + 0.8 / 3 * 2]])
patches.append(part1)

# add 2nd part

part2 = mpatches.Polygon([[0.1 + 0.4 / 3, 0.1 + 0.8 / 3], \
                          [0.1 + 0.4 / 3 * 2, 0.1 + 0.8 / 3 * 2], \
                          [0.9 - 0.4 / 3 * 2, 0.1 + 0.8 / 3 * 2], \
                          [0.9 - 0.4 / 3, 0.1 + 0.8 / 3]])
patches.append(part2)

# add 3rd part
part3 = mpatches.Polygon([[0.1, 0.1], \
                          [0.1 + 0.4 / 3, 0.1 + 0.8 / 3], \
                          [0.9 - 0.4 / 3, 0.1 + 0.8 / 3], \
                          [0.9, 0.1]])
patches.append(part3)

collection = PatchCollection(patches, alpha = 0.3)

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

fig.savefig("../Figures/Pyramid_Code.png", dpi = 200)
