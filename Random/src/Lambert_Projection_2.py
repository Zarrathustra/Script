from pylab import *

filename = "../Data/Random_Direction_3D.txt"

lines = open(filename, "r").readlines();

X = array([float(line.strip().split(" ")[0]) for line in lines])
Y = array([float(line.strip().split(" ")[1]) for line in lines])
Z = array([float(line.strip().split(" ")[2]) for line in lines])

THETA = arccos(Z)

N = len(X)

PHI = zeros(N)

for i in range(N):
    if (Y[i] >= 0):
        PHI[i] = arctan(Y[i] / X[i])
    else:
        PHI[i] = arctan(Y[i] / X[i]) + pi

x = zeros(N)
y = zeros(N)

for i in range(N):
    x[i] = 2 * cos(THETA[i] / 2) * cos(PHI[i])
    y[i] = 2 * cos(THETA[i] / 2) * sin(PHI[i])

figure(figsize = (10, 10), dpi = 500)

scatter(x, y, alpha = 0.05, color = "black", lw = 0)

xlim([-3, 3])
ylim([-3, 3])

title("Lambert Projection (Equal Area Projection) of Uniform Distribution Sphere Sampling")

savefig("../Figures/Lambert_Projection_2.png", dpi = 500)
