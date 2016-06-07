from pylab import *
import os

N = 100000

figure(figsize = (20, 20), dpi = 500)

lines = open("../Data/Weighted/Particle_Weighted.txt", "r").readlines();

X = [float(line.strip().split(',')[0]) for line in lines]
Y = [float(line.strip().split(',')[1]) for line in lines]

plot(X[1:N], Y[1:N], label = "Weighted")

lines = open("../Data/Weighted/Particle_Unweighted.txt", "r").readlines();

X = [float(line.strip().split(',')[0]) for line in lines]
Y = [float(line.strip().split(',')[1]) for line in lines]

plot(X[1:N], Y[1:N], label = "Unweighted")

legend()

savefig("../Figures/Weight_vs_Unweighted.png", dpi = 500)
