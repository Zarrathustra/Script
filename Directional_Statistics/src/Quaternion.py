from pylab import *
import os

def angle(w, x, y, z):

    phi = math.atan2(x * z + w * y, w * x - y * z)

    if (phi < 0):
        phi += 2 * pi

    theta = math.acos(w ** 2 - x ** 2 - y ** 2 + z **2)

    return phi, theta

filename = sys.argv[1]

lines = open(filename, "r").readlines();

W = [float(line.strip().split()[0]) for line in lines]
X = [float(line.strip().split()[1]) for line in lines]
Y = [float(line.strip().split()[2]) for line in lines]
Z = [float(line.strip().split()[3]) for line in lines]

PHI= []
THETA = []

for w, x, y, z in zip(W, X, Y, Z):
    phi, theta = angle(w, x, y, z)
    PHI.append(phi)
    THETA.append(theta)

figure(figsize = (20, 10), dpi = 500)

scatter(PHI, THETA, alpha = 0.5,
        linewidth = 0, color = "black")

xlim(-0.5, 2 * pi + 0.5)
ylim(-0.5, pi + 0.5)

xticks([0, pi, 2 * pi], ["0", r"$\pi$", r"$2\pi$"])
yticks([0, pi], ["0", r"$\pi$"])

xlabel(r"$\phi$")
ylabel(r"$\theta$")

title(sys.argv[2])

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 500)
