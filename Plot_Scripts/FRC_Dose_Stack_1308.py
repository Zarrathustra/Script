from pylab import *
import matplotlib.patches as mpatches
from scipy.optimize import leastsq

# read in data

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_Base.txt", "r").readlines();
XBase = [line.strip().split()[0] for line in lines]
YBase = [line.strip().split()[1] for line in lines]
XBase = array([float(x) for x in XBase])
YBase = array([float(y) for y in YBase])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_3.txt", "r").readlines();
X3_5 = [line.strip().split()[0] for line in lines]
Y3_5 = [line.strip().split()[1] for line in lines]
X3_5 = array([float(x) for x in X3_5])
Y3_5 = array([float(y) for y in Y3_5])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_6.txt", "r").readlines();
X6_8 = [line.strip().split()[0] for line in lines]
Y6_8 = [line.strip().split()[1] for line in lines]
X6_8 = array([float(x) for x in X6_8])
Y6_8 = array([float(y) for y in Y6_8])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_9.txt", "r").readlines();
X9_11 = [line.strip().split()[0] for line in lines]
Y9_11 = [line.strip().split()[1] for line in lines]
X9_11 = array([float(x) for x in X9_11])
Y9_11 = array([float(y) for y in Y9_11])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_12.txt", "r").readlines();
X12_14 = [line.strip().split()[0] for line in lines]
Y12_14 = [line.strip().split()[1] for line in lines]
X12_14 = array([float(x) for x in X12_14])
Y12_14 = array([float(y) for y in Y12_14])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_15.txt", "r").readlines();
X15_17 = [line.strip().split()[0] for line in lines]
Y15_17 = [line.strip().split()[1] for line in lines]
X15_17 = array([float(x) for x in X15_17])
Y15_17 = array([float(y) for y in Y15_17])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_18.txt", "r").readlines();
X18_20 = [line.strip().split()[0] for line in lines]
Y18_20 = [line.strip().split()[1] for line in lines]
X18_20 = array([float(x) for x in X18_20])
Y18_20 = array([float(y) for y in Y18_20])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_21.txt", "r").readlines();
X21_23 = [line.strip().split()[0] for line in lines]
Y21_23 = [line.strip().split()[1] for line in lines]
X21_23 = array([float(x) for x in X21_23])
Y21_23 = array([float(y) for y in Y21_23])

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_24.txt", "r").readlines();
X24_26 = [line.strip().split()[0] for line in lines]
Y24_26 = [line.strip().split()[1] for line in lines]
X24_26 = array([float(x) for x in X24_26])
Y24_26 = array([float(y) for y in Y24_26])

# set parameters

A = 0.07
N = 3838
DF1 = 17963
DF2 = 18713
lam = 0.0196
pixelSize = 1.32
lb = 0
rb = 1350
w0 = 180
w1 = 1300

u0 = pi * lam * (DF1 + DF2) / 2

# fitting function

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
X_Fit = linspace(lb, rb, 10000)

figure(figsize = (10, 10), dpi = 800)

def fitFRC(Y, X, color, label):

    plsq = leastsq(errfunc, p0, args = (Y, X), maxfev = 20000)
    print plsq[0]

    Y_Fit = func(plsq[0], X_Fit)
    Y_Amp = amp(X_Fit, plsq[0][0], plsq[0][1], plsq[0][2], plsq[0][3], plsq[0][4])

    plot(X_Fit, Y_Amp, c = color, label = label)

colorBase = "black"
color3_5 = "blue"
color6_8 = "green"
color9_11 = "lightgreen"
color12_14 = "yellow"
color15_17 = "orange"
color18_20 = "red"
color21_23 = "purple"
color24_26 = "magenta"

fitFRC(YBase, XBase, colorBase, "Base")
fitFRC(Y3_5, X3_5, color3_5, "3:5")
fitFRC(Y6_8, X6_8, color6_8, "6:8")
fitFRC(Y9_11, X9_11, color9_11, "9:11")
fitFRC(Y12_14, X12_14, color12_14, "12:14")
fitFRC(Y15_17, X15_17, color15_17, "15:17")
fitFRC(Y18_20, X18_20, color18_20, "18:20")
fitFRC(Y21_23, X21_23, color21_23, "21:23")
fitFRC(Y24_26, X24_26, color24_26, "24:26")

xlim(lb, rb)
ylim(0, 0.6)

xlabel("Frequency")
ylabel("FRC")

title("FRC of a Corrected Stack")

legend()

savefig("../Figures/FRCDoseInfluence.png", dpi = 800)
