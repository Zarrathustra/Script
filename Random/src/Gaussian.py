from pylab import *

N = 10000

filename = "../Data/Gaussian.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-5, 5)
ylim(-5, 5)

title("2D Gaussian Distribution by 10000 Samples")

savefig("../Figures/Gaussian.png", dpi = 500)
