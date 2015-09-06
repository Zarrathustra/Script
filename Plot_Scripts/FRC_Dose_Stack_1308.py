from pylab import *
import matplotlib.patches as mpatches
from scipy.optimize import leastsq

# read in data

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

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_27.txt", "r").readlines();
X27_29 = [line.strip().split()[0] for line in lines]
Y27_29 = [line.strip().split()[1] for line in lines]
X27_29 = array([float(x) for x in X24_26])
Y27_29 = array([float(y) for y in Y24_26])

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

    Y_Amp = amp(X_Fit, plsq[0][0], plsq[0][1], plsq[0][2], plsq[0][3], plsq[0][4])

    plot(X_Fit,
         Y_Amp,
         c = color,
         label = label + " Amplitude",
         linestyle = "-",
         linewidth = 1.5)

color15_17 = "blue"
color18_20 = "green"
color21_23 = "orange"
color24_26 = "red"
color27_29 = "purple"

fitFRC(Y15_17, X15_17, color15_17, "15:17")
fitFRC(Y18_20, X18_20, color18_20, "18:20")
fitFRC(Y21_23, X21_23, color21_23, "21:23")
fitFRC(Y24_26, X24_26, color24_26, "24:26")
fitFRC(Y27_29, X27_29, color27_29, "27:29")

xlim(lb, rb)
ylim(0, 0.6)

xlabel("Frequency")
ylabel("FRC")

title("The Influence of Irradiation Injury on FRC")

legend()

savefig("../Figures/FRCDoseInfluence.png", dpi = 800)
