# plot a High-Pass-Filter

import math
from pylab import *

N = 3000 # the number of samplings

threshold = 0.4
edgeWidth = 0.1

X = linspace(0, sqrt(2) / 2, N)

def highPass(x):
    if (x > threshold):
        return 1
    elif (x < threshold - edgeWidth):
        return 0
    else:
        return cos((threshold - x) * pi / edgeWidth) / 2 + 0.5

Y = [highPass(x) for x in X]

plot(X, Y)

plot([threshold, threshold], [0, 1.2], linestyle = "--")

fontSize = 15

annotate("threshold",
         xy = (threshold, 0),
         xycoords = "data",
         xytext = (50, 30),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->"))

annotate("edgeWidth",
         xy = (threshold - edgeWidth / 2, 0),
         xycoords = "data",
         xytext = (-120, 30),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->"))

ax = gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

xlim(0, 0.7)
ylim(0, 1.2)

yticks(linspace(0, 1.2, 7))

xlabel("Frequency")
ylabel("Alpha")

title("High Pass Filter")

savefig("../Figures/HighPassFilter.png", dpi = 200)
