from pylab import *

N = 10000

filename = "../Data/2D_Gaussian.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-5, 5)
ylim(-5, 5)

title(r"2D Gaussian Distribution with $\sigma_1 = 1, \sigma_2 = 1, \rho = 0.5$")

savefig("../Figures/2D_Gaussian.png", dpi = 500)
