from pylab import *

from scipy.optimize import leastsq

figure(figsize = (16, 9), dpi = 200)

nCore = [88, 176, 352, 528, 704]

time_1 = [0.007, 0.013, 0.027, 0.039, 0.052]

time = [1.0 / t for t in time_1]

def residuals(p, y, x):
    return y - p / x

plsq = leastsq(residuals, 1, args = (time, nCore))

S = plsq[0][0]

X = linspace(50, 750, 1000)
Y = [S / x for x in X]

plot(X, Y, "k--", label = "Hyperbola")
plot(nCore, \
     time, \
     "+", \
     color = "darkolivegreen", \
     markersize = 20, \
     markeredgewidth = 3)

xlabel("Number of Cores", fontsize = "x-large")
ylabel("Time (Minutes)", fontsize = "x-large")

xlim([0, 800])
ylim([0, 200])

legend(fontsize = "xx-large")

savefig("../Figures/Linear_Speed_Up.png", dpi = 200)
