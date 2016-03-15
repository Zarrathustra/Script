from pylab import *

N = 10000

figure(figsize = (20, 10), dpi = 500)

subplot(1, 2, 1)

filename = "../Data/2D_Gaussian_Src.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-5, 5)
ylim(-10, 10)

title(r"2D Gaussian Distribution with $\sigma_1 = 1, \sigma_2 = 2, \rho = 0.5$")

subplot(1, 2, 2)

filename = "../Data/2D_Gaussian_Dst.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-5, 5)
ylim(-10, 10)

title("2D Gaussian Distribution of Statistics Covariance Matrix")

savefig("../Figures/Stat_2D_Gaussian.png", dpi = 500)
