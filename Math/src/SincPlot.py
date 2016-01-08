# plot the normalized sinc function

import math
from pylab import *

N = 3000 # the number of samplings
M = 16 # the number of cycles plotted

X = range(-N / 2, N / 2)

value = []

for i in X:
    if i != 0:
        par = math.pi * i * M / N
        value.append(math.sin(par) / (par))
    else:
        value.append(1)

figure(figsize = (10, 5), dpi = 80)

plot(X, value, linewidth = 2, color = "black")

ax = gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

xTicks = range(-M / 2, M / 2 + 1)
xTicksPos = [x * N / M for x in xTicks]

xticks(xTicksPos, xTicks)

yticks([1], [1])

title("Normalized Sinc")

savefig("../Figures/Normalized_Sinc.png", dpi = 200)
