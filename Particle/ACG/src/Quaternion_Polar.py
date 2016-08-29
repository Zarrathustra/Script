from pylab import *
import os

def angle(w, x, y, z):

    phi = math.atan2(x * z + w * y, w * x - y * z)

    if (phi < 0):
        phi += 2 * pi
    
    x = w ** 2 - x ** 2 - y ** 2 + z ** 2
    if (x >= 1):
        theta = 0
    elif (x <= -1):
        theta = 0
    else:
        theta = math.acos(x)

    return phi, theta

filename = sys.argv[1]

lines = open(filename, "r").readlines()

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

figure(figsize = (10, 10), dpi = 500)

subplot(111, projection = 'polar')

c = scatter(PHI, THETA, c = "black", linewidth = 0)
c.set_alpha(0.1)

ylim([0, pi])
yticks([0, pi / 4, pi / 2, pi / 4 * 3, pi],
       [0,
        r"$\frac{\pi}{4}$",
        r"$\frac{\pi}{2}$",
        r"$\frac{3\pi}{4}$",
        r"$\pi$"])

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + "_Polar.png", dpi = 500)
