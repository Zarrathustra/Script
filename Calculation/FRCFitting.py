from numpy import *
from pylab import *

import matplotlib.patches as mpatches

from scipy.optimize import leastsq

N = 3838

A = 0.07

DF1 = 17963
DF2 = 18713
lam = 0.0196

pixelSize = 1.32

arc = arctan(A / sqrt(1 - A * A))
con = 2 / (pi * lam * (DF1 + DF2))

def zeroPoint(n):
    return sqrt(con * (-arc + n * pi))

w1 = zeroPoint(1)
w2 = zeroPoint(2)

zeroPoint1 =  w1 * N * pixelSize
zeroPoint2 =  w2 * N * pixelSize

lines = open("../Data/stack_1308_FRC.txt", "r").readlines()

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 800)

scatter(X, Y, c = "black", linewidth = 1, marker = u'+');

plot([264.2, 264.2], [0, 1], c = "blue", linewidth = 1, linestyle = "-.")
plot([375.8, 375.8], [0, 1], c = "blue", linewidth = 1, linestyle = "-.")

xlim(250, 400)
ylim(0, 1)

xlabel("Frequency")
ylabel("FRC")

X_New = []
Y_New = []

for i in range(size(X)):
    if (X[i] > zeroPoint1) and (X[i] < zeroPoint2):
        X_New.append(X[i])
        Y_New.append(Y[i])

X = array(X_New)
Y = array(Y_New)

def ctf(w):
    chi = pi * lam * w * w / (N * pixelSize) / (N * pixelSize) * (DF1 + DF2) / 2
    return -sqrt(1 - A * A) * sin(chi) - A * cos(chi)

CTF_X = ctf(X)
CTF_X2 = CTF_X ** 2
CTF_X_Y = CTF_X * Y

amp = CTF_X_Y.sum() / CTF_X2.sum()

print "Amplitude = ", amp

Y_Fit = amp * CTF_X

print "Res = ", ((Y - Y_Fit) ** 2).sum()

plot(X, Y_Fit, c = "red", linewidth = 1)

savefig("../Figures/FRCFittingConst.png", dpi = 800)

def errfunc(p, y, x):
    a1, a2, b1, b2, c = p
    w = x / (pixelSize * N)
    err = y - (a1 * exp(-b1 * w * w) + a2 * exp(-b2 * w * w) + c) * ctf(x)
    return err

def func(p, x):
    a1, a2, b1, b2, c = p
    print a1, a2, b1, b2, c
    w = x / (pixelSize * N)
    return (a1 * exp(-b1 * w * w) + a2 * exp(-b2 * w * w) + c) * ctf(x)

p0 = [0, 0, 0, 0, 0]

plsq = leastsq(errfunc, p0, args = (Y, X), maxfev = 10000)
print plsq[0]

Y_Fit = func(plsq[0], X)
print Y_Fit

plot(X, Y_Fit, c = "blue", linewidth = 1)

patchConst = mpatches.Patch(color = "red", label = "Constant")
patchGaussian = mpatches.Patch(color = "blue", label = "Gaussian")

legend(handles = [patchConst, patchGaussian])

savefig("../Figures/FRCFittingGaussian.png", dpi = 800)

# Fitting 1st zero point and 10st zero point
w1 = zeroPoint(1)
w10 = zeroPoint(10)

zeroPoint1 =  w1 * N * pixelSize
zeroPoint10 =  w10 * N * pixelSize

print zeroPoint1, zeroPoint10
