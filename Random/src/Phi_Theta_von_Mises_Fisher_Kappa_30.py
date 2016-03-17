from pylab import *

N = 100000

filename = "../Data/Phi_Theta_von_Mises_Fisher_Kappa_30.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]
W = [float(line.strip().split()[2]) for line in lines]

figure(figsize = (20, 10), dpi = 500)

cm = get_cmap("Spectral")

scatter(X[:N], Y[:N], alpha = 0.5, c = W,
        vmin = min(W), vmax = max(W), cmap = cm,
        linewidth = 0)

# scatter(X[:N], Y[:N], alpha = 0.2, linewidth = 0, color = "black")

xlim(-0.5, 2 * pi + 0.5)
ylim(-0.5, pi + 0.5)

xticks([0, pi, 2 * pi], ["0", r"$\pi$", r"$2\pi$"])
yticks([0, pi], ["0", r"$\pi$"])


xlabel(r"$\phi$")
ylabel(r"$\theta$")

savefig("../Figures/Phi_Theta_von_Mises_Fisher_Kappa_30.png", dpi = 500)
