from numpy import *
from pylab import *

import matplotlib.patches as mpatches

from scipy.optimize import leastsq

import sys
import os

filenameA = sys.argv[1]
filenameB = sys.argv[2]

basenameA = os.path.basename(filenameA)
basenameA = os.path.splitext(basenameA)[0]
basenameB = os.path.basename(filenameB)
basenameB = os.path.splitext(basenameB)[0]

N = int(sys.argv[3])
DF1 = float(sys.argv[4])
DF2 = float(sys.argv[5])
lam = float(sys.argv[6])
pixelSize = float(sys.argv[7])

lb = int(sys.argv[8])
rb = int(sys.argv[9])

w0 = int(sys.argv[10])
w1 = int(sys.argv[11])

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

def readIn(filename):
    lines = open(filename, "r").readlines()

    X = [line.strip().split()[0] for line in lines]
    Y = [line.strip().split()[1] for line in lines]

    X = [float(x) for x in X]
    Y = [float(y) for y in Y]

    X_New = []
    Y_New = []

    for i in range(size(X)):
        if (X[i] > w0) and (X[i] < w1):
            X_New.append(X[i])
            Y_New.append(Y[i])

    X = array(X_New)
    Y = array(Y_New)

    return X, Y

XA, YA = readIn(filenameA)
XB, YB = readIn(filenameB)

figure(figsize = (10, 10), dpi = 800)

xlim(lb, rb)
ylim(0, 0.2)

xlabel("Frequency")
ylabel("FRC")

title("FRC Comparison Between Local and Total Motion Correction")

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

p0 = [0.5, 0.5, 700, 150, 0, u0, 0.05, 5, 0.35]

lw = 1.5

def lsqSolve(Y, X, ls, lab):
    plsq = leastsq(errfunc, p0, args = (Y, X), maxfev = 20000)
    print plsq[0]

    X_Fit = linspace(lb, rb, 10000)

    Y_Amp = amp(X_Fit, plsq[0][0], plsq[0][1], plsq[0][2], plsq[0][3], plsq[0][4])
    Y_Backg = backg(X_Fit, plsq[0][6], plsq[0][7], plsq[0][8])

    plot(X_Fit, Y_Amp + Y_Backg, c = "red", linewidth = lw, linestyle = ls,
         label = lab + "  Amplitude + Background")
    plot(X_Fit, Y_Backg, c = "green", linewidth = lw, linestyle = ls,
         label = lab + "  Background")
    plot(X_Fit, Y_Amp, c = "blue", linewidth = lw, linestyle = ls,
         label = lab + "  Amplitude")

lsqSolve(YA, XA, "--", "Local")
lsqSolve(YB, XB, "-", "Total")

legend()

savefig("../Figures/" + basenameA + basenameB + ".png", dpi = 800)
