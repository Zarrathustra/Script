from pylab import *

N = 6000

filename = "../Data/Particle_C5.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (20, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.5, linewidth = 0, color = "black")

xlim(-0.5, 2 * pi + 0.5)
ylim(-0.5, pi + 0.5)

xticks([0, 2 * pi / 5, pi, 2 * pi], ["0", r"$\frac{2\pi}{5}$", r"$\pi$", r"$2\pi$"])
yticks([0, pi], ["0", r"$\pi$"])

xlabel(r"$\phi$")
ylabel(r"$\theta$")

title(r"$\phi$ and $\theta$ of Uniform Distribution of C5 Symmetry Sphere")

savefig("../Figures/Phi_Theta_Symmetry_C5.png", dpi = 500)

X = [float(line.strip().split()[3]) for line in lines]
Y = [float(line.strip().split()[4]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.5, linewidth = 0, color = "black")

xlim(-40, 40)
ylim(-40, 40)

xticks([-30, 30], [-30, 30])
yticks([-30, 30], [-30, 30])

xlabel("X")
ylabel("y")

title("X and Y of a Particle Filter Initialization")

savefig("../Figures/X_Y_Symmetry_C5.png", dpi = 500)
