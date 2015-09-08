from pylab import *

N = 3838

A = 0.07

DF1 = 17963
DF2 = 18713
lam = 0.0196

pixelSize = 1.32

def ctf(w):
    chi = pi * lam * w * w / (N * pixelSize) / (N * pixelSize) * (DF1 + DF2) / 2
    return -sqrt(1 - A * A) * sin(chi) - A * cos(chi)

lines = open("../Data/stack_1308_FRC.txt", "r").readlines();

XFRC = [line.strip().split()[0] for line in lines]
YFRC = [line.strip().split()[1] for line in lines]

XFRC = [float(x) for x in XFRC]
YFRC = [float(y) for y in YFRC]

XCTF = linspace(XFRC[0], XFRC[-1], 10000)
YCTF = [abs(ctf(x)) for x in XCTF]

figure(figsize = (10, 5), dpi = 800)

plot(XCTF, YCTF, c = "red", linewidth = 1)
scatter(XFRC, YFRC, c = "blue", linewidth = 1, marker = u'+');

xlim(0, 1000)
ylim(0, 1)

xlabel("Frequency")

title("FRC and CTF of a Motion-Corrected Stack");

savefig("../Figures/FRC_CTF_CorrectedStack.png", dpi = 800)
