from pylab import *

X = [-1, -1, 1, 1]
Y = [-1, 1, -1, 1]

fontSize = 12
dotSize = 70

figure(figsize = (8, 8), dpi = 80)
# subplot(1, 1, 1)
# axes([0.025, 0.025, 0.95, 0.95])

scatter(X, Y, c = "black", s = dotSize, alpha = 0.7)
annotate(r"$(x_0, y_0, f(x_0, y_0))$",
         xy = (-1, -1),
         xycoords = "data",
         xytext = (-30, 10),
         textcoords = "offset points",
         fontsize = fontSize)
annotate(r"$(x_0+1, y_0, f(x_0+1, y_0))$",
         xy = (1, -1),
         xycoords = "data",
         xytext = (-30, 10),
         textcoords = "offset points",
         fontsize = fontSize)
annotate(r"$(x_0, y_0+1, f(x_0, y_0+1))$",
         xy = (-1, 1),
         xycoords = "data",
         xytext = (-30, 10),
         textcoords = "offset points",
         fontsize = fontSize)
annotate(r"$(x_0+1, y_0+1, f(x_0+1, y_0+1))$",
         xy = (1, 1),
         xycoords = "data",
         xytext = (-30, 10),
         textcoords = "offset points",
         fontsize = fontSize)

plot([-1, 1], [-1, -1], c = "black", linewidth = 2, linestyle = "--")
plot([-1, 1], [1, 1], c = "black", linewidth = 2, linestyle = "--")
scatter([0.2, 0.2], [-1, 1], c = "blue", s = dotSize, alpha = 0.7)

annotate(r"$(x, y_0, f(x, y_0))$",
         xy = (0.2, -1),
         xycoords = "data",
         xytext = (-30, -30),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

annotate(r"$(x, y_0+1, f(x, y_0+1))$",
         xy = (0.2, 1),
         xycoords = "data",
         xytext = (-30, 30),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

plot([0.2, 0.2], [-1, 1], c = "blue", linewidth = 2, linestyle = "--")
scatter([0.2], [0.2], c = "green", s = dotSize, alpha = 0.7)

annotate(r"$(x, y, f(x, y))$",
         xy = (0.2, 0.2),
         xycoords = "data",
         xytext = (20, 20),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

xlim(-2.5, 2.5)
ylim(-2.5, 2.5)
xticks([])
yticks([])

savefig("2D_Linear_Interpolation_Demo.png", dpi = 200)
show()
