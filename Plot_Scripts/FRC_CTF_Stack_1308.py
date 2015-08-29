from pylab import *

lines = open("../Data/stack_1308_CTF.txt", "r").readlines();

XCTF = [line.strip().split()[0] for line in lines]
YCTF = [line.strip().split()[1] for line in lines]

XCTF = [float(x) for x in XCTF]
YCTF = [float(y) for y in YCTF]

lines = open("../Data/stack_1308_FRC.txt", "r").readlines();

XFRC = [line.strip().split()[0] for line in lines]
YFRC = [line.strip().split()[1] for line in lines]

XFRC = [float(x) for x in XFRC]
YFRC = [float(y) for y in YFRC]

figure(figsize = (10, 5), dpi = 800)

scatter(XCTF, YCTF, c = "red", linewidth = 1, marker = u'+');
plot(XCTF, YCTF, c = "red", linewidth = 0.5)
scatter(XFRC, YFRC, c = "blue", linewidth = 1, marker = u'+');

xlim(0, 1000)
ylim(0, 1)

xlabel("Frequency")

title("FRC and CTF of a Motion-Corrected Stack");

savefig("../Figures/FRC_CTF_CorrectedStack.png", dpi = 800)
