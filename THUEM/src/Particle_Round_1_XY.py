from pylab import *

N = 1000

filename = "../Data/Particle_Round_1/Particle0005.par"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[4]) for line in lines]
Y = [float(line.strip().split()[5]) for line in lines]
W = [N * float(line.strip().split()[6]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

scatter(X[:N], Y[:N], s = W[:N], alpha = 0.5, linewidth = 0, color = "black")

xlabel("X")
ylabel("Y")

neff = 0
for i in range(len(W)):
    neff += W[i] * W[i]
print "neff = ", N * N / neff

savefig("../Figures/Particle_Round_1.png", dpi = 500)
