from pylab import *

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def seperate(self, nFraction):
        x = []
        y = []
        phi = 0
        for i in range(0, nFraction):
            x.append(self.radius * cos(phi))
            y.append(self.radius * sin(phi))
            phi += 2 * pi / nFraction
        return x, y

figure(figsize = (5, 5), dpi = 200)

colors = ["black", "blue", "green", "orange", "red"]

scatter([0], [0], c = colors[0])

circle = Circle(1)
for i in range(1, 5):
    circle.setRadius(i)
    x, y = circle.seperate(4 * i)
    scatter(x, y, color = colors[i])

def assign(j, n):
    if (j >= 0) and (j <= n):
        return j
    elif (j <= 2 * n + 1):
        return j - 1
    elif (j <= 3 * n + 2):
        return j - 2
    elif (j < 4 * n + 3):
        return j - 3
    elif (j == 4 * n + 3):
        return 0

n = 2
circle.setRadius(n)
x0, y0 = circle.seperate(4 * n)
circle.setRadius(n + 1)
x1, y1 = circle.seperate(4 * (n + 1))

for i in range(0, 4 * (n + 1)):
    plot([x1[i], x0[assign(i, n)]], [y1[i], y0[assign(i, n)]], c = "brown") 
    plot([x1[(i + 1) % (4 * (n + 1))], x0[assign(i, n)]], \
         [y1[(i + 1) % (4 * (n + 1))], y0[assign(i, n)]], c = "brown")

for i in range(0, 4 * n):
    plot([x0[i % (4 * n)], x0[(i + 1) % (4 * n)]],
         [y0[i % (4 * n)], y0[(i + 1) % (4 * n)]], c = colors[n])

for i in range(0, 4 * n + 4):
    plot([x1[i % (4 * n + 4)], x1[(i + 1) % (4 * n + 4)]],
         [y1[i % (4 * n + 4)], y1[(i + 1) % (4 * n + 4)]], c = colors[n + 1])

xlim(-5, 5)
ylim(-5, 5)

title("Pseudo-Even Sphere Separation Top View")

savefig("../Figures/Pseudo_Even_Sphere_Separation_Top_View.png", dpi = 200)
