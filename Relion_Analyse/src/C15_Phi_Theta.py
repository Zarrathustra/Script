from pylab import *

filename = "../Data/C15_Phi_Theta.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

X = [x / 180 * pi for x in X]
Y = [y / 180 * pi for y in Y]

figure(figsize = (10, 10), dpi = 500)

scatter(X, Y, alpha = 0.2, linewidth = 0, color = "black")

xlim([-pi / 15 - 0.05, pi / 15 + 0.05])
ylim([-0.05, pi + 0.05])

xticks([-pi / 15, pi / 15], [r"$-\frac{\pi}{15}$", r"$\frac{\pi}{15}$"])
xlabel(r"$\phi$")
ylabel(r"$\theta$")

title(r"$\phi$ and $\theta$ Distribution of Relion Auto-refine")

savefig("../Figures/C15_Phi_Theta.png", dpi = 500)
