from pylab import *

filename = "../Data/MKB_RL.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 5), dpi = 80)

plot(X, Y, linewidth = 2, alpha = 0.7)

xlim(0, 1.5)

title(r"Inverse Fourier Transform of Windowed Modified Kaiser Bessel Function, $m = 2, n = 3, \alpha = 0.5$")

savefig("../Figures/MKB_RL.png", dpi = 200)
