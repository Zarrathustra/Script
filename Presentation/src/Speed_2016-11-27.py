from pylab import *

from scipy.optimize import leastsq

figure(figsize = (16, 9), dpi = 200)

nNode = [17, 30, 50, 100, 150]

nCore = [24 * i for i in nNode]

print nCore

time = [360, 200, 120, 60, 50]

print time

def residuals(p, y, x):
    return y - p / x

plsq = leastsq(residuals, 1, args = (time, nCore))

S = plsq[0][0]

X = linspace(50, 3800, 1000)
Y = [S / x for x in X]

plot(X, Y, "k--", label = "Hyperbola")
plot(800, \
     510, \
     "+", \
     color = "red", \
     markersize = 20, \
     markeredgewidth = 3, \
     label = "RELION")
plot(nCore, \
     time, \
     "+", \
     color = "darkolivegreen", \
     markersize = 20, \
     markeredgewidth = 3, \
     label = "THUEM")

xlabel("Number of Cores", fontsize = "x-large")
ylabel("Time (Minutes)", fontsize = "x-large")

xlim([0, 4000])
ylim([0, 600])

xticks(fontsize = 20, rotation = 30)
yticks(fontsize = 20)

legend(fontsize = "xx-large")

subplots_adjust(top = 0.9, bottom = 0.15)

savefig("../Figures/Speed_2016-11-27.png", dpi = 200)
