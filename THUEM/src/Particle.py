from pylab import *

filename = "../Data/Particle_Round_1/Particle0005.par"

lines = open(filename, "r").readlines();

N = len(lines)

X = array([float(line.strip().split()[4]) for line in lines])
Y = array([float(line.strip().split()[5]) for line in lines])
W = array([float(line.strip().split()[6]) for line in lines])

figure(figsize = (20, 10), dpi = 500)

subplot(1, 2, 1)

size = 5 * N * W

scatter(X, Y, s = size, alpha = 0.5, lw = 0, c = "black")

xlabel("X")
ylabel("Y")

neff = sum(W * W)
print "neff = ", 1.0 / neff

subplot(1, 2, 2)

I = array([float(line.strip().split()[0]) for line in lines])
J = array([float(line.strip().split()[1]) for line in lines])
K = array([float(line.strip().split()[2]) for line in lines])
L = array([float(line.strip().split()[3]) for line in lines])

PHI = arctan((J * L + I * K) / (I * J - K * L))
for i in range(N):
    if (PHI[i] < 0):
        PHI[i] += 2 * pi
THETA = arccos(I * I - J * J - K * K + L * L)

x = zeros(N)
y = zeros(N)

for i in range(N):
    x[i] = 2 * cos(THETA[i] / 2) * cos(PHI[i])
    y[i] = 2 * cos(THETA[i] / 2) * sin(PHI[i])
    # x[i] = cos(PHI[i])
    # y[i] = sin(PHI[i])

scatter(x, y, s = size, alpha = 0.5, lw = 0, c = "black")

xlim([-4, 4])
ylim([-4, 4])

savefig("../Figures/Particle_Round_1.png", dpi = 500)
