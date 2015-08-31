from numpy import *
from pylab import *

import matplotlib.patches as mpatches

from scipy.optimize import leastsq

N = 3838

DF1 = 17963
DF2 = 18713
lam = 0.0196

u0 = pi * lam * (DF1 + DF2) / 2

print "u0 = ", u0

A = 0.07

pixelSize = 1.32

lines = open("../Data/stack_1308_FRC.txt", "r").readlines()

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 800)

scatter(X, Y, c = "black", linewidth = 1, marker = u'+');

lb = 0
rb = 1350

xlim(lb, rb)
ylim(0, 1)

xlabel("Frequency")
ylabel("FRC")

w0 = 230
w1 = 1300

X_New = []
Y_New = []

for i in range(size(X)):
    if (X[i] > w0) and (X[i] < w1):
        X_New.append(X[i])
        Y_New.append(Y[i])

X = array(X_New)
Y = array(Y_New)

def ctf(w, u):
    chi = u * w * w / (N * pixelSize) / (N * pixelSize)
    return -sqrt(1 - A * A) * sin(chi) - A * cos(chi)

def errfunc(p, y, x):
    a1, a2, b1, b2, c, u = p
    w = x / (pixelSize * N)
    err = y - (a1 * exp(-b1 * w * w) + a2 * exp(-b2 * w * w) + c) * abs(ctf(x, u))
    return err

def func(p, x):
    a1, a2, b1, b2, c, u= p
    print a1, a2, b1, b2, c, u
    w = x / (pixelSize * N)
    return (a1 * exp(-b1 * w * w) + a2 * exp(-b2 * w * w) + c) * abs(ctf(x, u))

p0 = [1, -1, 0, 0, 0, u0]

plsq = leastsq(errfunc, p0, args = (Y, X), maxfev = 20000)
print plsq[0]

X_Fit = linspace(lb, rb, 10000)
Y_Fit = func(plsq[0], X_Fit)
print Y_Fit

plot(X_Fit, Y_Fit, c = "blue", linewidth = 1)

# patchConst = mpatches.Patch(color = "red", label = "Constant")
# patchGaussian = mpatches.Patch(color = "blue", label = "Gaussian")

# legend(handles = [patchConst, patchGaussian])

savefig("../Figures/FRCFittingMultiPeakZeroPointEstimate.png", dpi = 800)
