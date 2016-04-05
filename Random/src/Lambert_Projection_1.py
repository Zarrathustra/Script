from pylab import *

N = 50

X = zeros(N * N)
Y = zeros(N * N)

PHI = linspace(0, 2 * pi, N + 1)[:-1]
THETA = linspace(0, pi, N + 1)[:-1]

figure(figsize = (10, 10), dpi = 500)

i = 0
for phi in PHI:
    for theta in THETA:
        X[i] = 2 * cos(theta / 2) * cos(phi)
        Y[i] = 2 * cos(theta / 2) * sin(phi)
        i += 1

scatter(X, Y, alpha = 0.3, color = "black", lw = 0)

savefig("../Figures/Lambert_Projection_1.png", dpi = 500)
