from pylab import *

N = 100000

filename = "../Data/Phi_Theta_Random_Direction_3D.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (20, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-0.5, 2 * pi + 0.5)
ylim(-0.5, pi + 0.5)

xticks([0, pi, 2 * pi], ["0", r"$\pi$", r"$2\pi$"])
yticks([0, pi], ["0", r"$\pi$"])

xlabel(r"$\phi$")
ylabel(r"$\theta$")

title(r"$\phi$ and $\theta$ of an Uniform Sphere Ditribution")

savefig("../Figures/Phi_Theta_Sphere.png", dpi = 500)
