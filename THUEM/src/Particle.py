from pylab import *

filename = "../Data/Particle_Round_1/Particle0005.par"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[4]) for line in lines]
Y = [float(line.strip().split()[5]) for line in lines]
W = [float(line.strip().split()[6]) for line in lines]

figure(figsize = (20, 10), dpi = 500)

subplot(1, 2, 1)

size = [len(lines) * w for w in W]

scatter(X, Y, s = size, alpha = 0.5, linewidth = 0, color = "black")

xlabel("X")
ylabel("Y")

neff = 0
for i in range(len(W)):
    neff += W[i] * W[i]
print "neff = ", 1.0 / neff

subplot(1, 2, 2)

savefig("../Figures/Particle_Round_1.png", dpi = 500)
