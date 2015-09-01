from numpy import *
from pylab import *

import matplotlib.patches as mpatches

from scipy.optimize import leastsq

import sys
import os

filename = sys.argv[1]

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

N = int(sys.argv[2])
DF1 = float(sys.argv[3])
DF2 = float(sys.argv[4])
lam = float(sys.argv[5])
pixelSize = float(sys.argv[6])

lb = int(sys.argv[7])
rb = int(sys.argv[8])

w0 = int(sys.argv[9])
w1 = int(sys.argv[10])

print "N = ", N
print "DF1 = ", DF1
print "DF2 = ", DF2
print "lambda = ", lam
print "pixel size = ", pixelSize
print "lb = ", lb
print "rb = ", rb
print "w0 = ", w0
print "w1 = ", w1

A = 0.07

u0 = pi * lam * (DF1 + DF2) / 2

lines = open(filename, "r").readlines()

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 800)

scatter(X, Y, c = "black", linewidth = 1, marker = u'+');

xlim(lb, rb)
ylim(0, 1)

xlabel("Frequency")
ylabel("FRC")

X_New = []
Y_New = []

for i in range(size(X)):
    if (X[i] > w0) and (X[i] < w1):
        X_New.append(X[i])
        Y_New.append(Y[i])

X = array(X_New)
Y = array(Y_New)

def ctf(x, u):
    chi = u * x * x / (N * pixelSize) / (N * pixelSize)
    return -sqrt(1 - A * A) * sin(chi) - A * cos(chi)

def amp(x, a1, a2, b1, b2, c):
    w = x / (pixelSize * N)
    return a1 * exp(-b1 * w * w) + a2 * exp(-b2 * w * w) + c

def re(x):
    if (x < 0):
        return 0
    else:
        return x

def backg(x, d, e, f):
    w = x / (pixelSize * N)
    res = d * cos(e * (w - f))
    return array([re(x) for x in res])

def func(p, x):
    a1, a2, b1, b2, c, u, d, e, f = p
    return amp(x, a1, a2, b1, b2, c) * abs(ctf(x, u)) + backg(x, d, e, f)

def errfunc(p, y, x):
    err = y - func(p, x)
    return err

p0 = [0.5, 0.5, 700, 150, 0, u0, 0.05, 5, 0.3]

plsq = leastsq(errfunc, p0, args = (Y, X), maxfev = 20000)
print plsq[0]

X_Fit = linspace(lb, rb, 10000)

Y_Fit = func(plsq[0], X_Fit)
Y_Amp = amp(X_Fit, plsq[0][0], plsq[0][1], plsq[0][2], plsq[0][3], plsq[0][4])
Y_Backg = backg(X_Fit, plsq[0][6], plsq[0][7], plsq[0][8])

plot(X_Fit, Y_Fit, c = "blue", linewidth = 1)
plot(X_Fit, Y_Amp + Y_Backg, c = "red", linewidth = 1)
plot(X_Fit, Y_Backg, c = "green", linewidth = 1)

patchAmpBackg = mpatches.Patch(color = "red", label = "Amplitude + Background")
patchBackg = mpatches.Patch(color = "green", label = "Background")

legend(handles = [patchAmpBackg, patchBackg])

savefig("../Figures/" + basename + ".png", dpi = 800)
