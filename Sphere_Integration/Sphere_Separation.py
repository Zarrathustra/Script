from pylab import *

class Sphere:

    def __init__(self, radius, theta, phi):
        self.radius = radius
        self.theta = theta
        self.phi = phi

    def toCartesian(self):
        x = self.radius * sin(self.theta) * cos(self.phi)
        y = self.radius * sin(self.theta) * sin(self.phi)
        z = self.radius * cos(self.theta)
        return x, y, z


def integrateArea(radius, n, m):
    return (pi * radius) ** 2 / (4 * (n - abs(m - n)) * n) \
         * sin(m * pi / (2 * n))

def seperateSphere(limit):

    sphere = Sphere(1, 0, 0)

    n = int(ceil(sqrt((limit - 2) / 4)))

    deltaTheta = 0.5 * pi / n

    for a in range(-n, n + 1):

        sphere.phi = 0
        size = (n - abs(a)) * 4 or 1
        deltaPhi = 2 * pi / size

        for i in range(size):
            yield sphere.toCartesian()
            sphere.phi += deltaPhi

        sphere.theta += deltaTheta 
