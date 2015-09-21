from pylab import *

from Sphere_Separation import *

def sphereArea(N):
    n = int(ceil(sqrt((N - 2) / 4)))

    area = 0
    num = 0
    for m in range(1, 2 * n):
        size = 4 * (n - abs(m - n))
        area += size * integrateArea(1, n, m)
        num += 2 * size

    return area, num

trueValue = 4 * pi
print "True Value = ", trueValue

M = 10

N = 1
error = []
for i in range(0, M):
    N *= 10
    print "N = ", N
    area, num = sphereArea(N)
    print "Sphere Area = ", area
    print "Number of Triangles", num
    print "Error = ", abs(area - trueValue)
    error.append(log10(abs(area - trueValue)))

X = range(1, M + 1)

figure(figsize = (10, 5), dpi = 200)

plot(X, error)
scatter(X, error, s = 20)

xlabel("10-Base Log of Integration Number")
ylabel("10-Base Log of Error")

xticks(range(0, M + 2))
xlim(0, M + 1)

title("Error Measurement of Sphere Integration")

savefig("../Figures/Sphere_Integration_Error.png", dpi = 200)
