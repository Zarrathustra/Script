from pylab import *

X = [2012, 2013, 2014, 2015]
Y = [0, 3, 5, 5]

figure(figsize = (10, 5), dpi = 80)
colors = [float(y) for y in Y]

width = 0.4

bar(X, Y, width, alpha = 0.5)

xlim(2012, 2016)
ylim(0, 8)

x = [x + width / 2 for x in X]

xticks(x, X)
yticks(range(9))

xlabel("Year")
ylabel("Number of Papers Published")

title("Structures Near Atomic Resolution " + r"($2.2\AA$ to $4.5\AA$)")

for i in range(4):
    text(x[i], Y[i] + 0.2, "%d"%int(Y[i]))

savefig("cryoEM_Development.png", dpi = 200)
show()
