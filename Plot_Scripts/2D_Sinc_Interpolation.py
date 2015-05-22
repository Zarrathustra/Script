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
         xytext = (-30, -20),
         textcoords = "offset points",
         fontsize = fontSize)
annotate(r"$(x_0+1, y_0, f(x_0+1, y_0))$",
         xy = (1, -1),
         xycoords = "data",
         xytext = (-30, -20),
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

scatter([0.2], [0.2], c = "green", s = dotSize, alpha = 0.7)

annotate(r"$(x, y, f(x, y))$",
         xy = (0.2, 0.2),
         xycoords = "data",
         xytext = (20, 0),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

plot([-1, 0.2], [-1, 0.2], linewidth = 2, linestyle = "--",
     c = "green", alpha = 0.5)
plot([-1, 0.2], [1, 0.2], linewidth = 2, linestyle = "--",
     c = "green", alpha = 0.5)
plot([1, 0.2], [-1, 0.2], linewidth = 2, linestyle = "--",
     c = "green", alpha = 0.5)
plot([1, 0.2], [1, 0.2], linewidth = 2, linestyle = "--",
     c = "green", alpha = 0.5)

plot([-1, -1], [-1, 0.2], linewidth = 2, linestyle = "--",
     c = "black", alpha = 0.5)
annotate(r"$y_d$",
         xy = (-1, -0.4),
         xycoords = "data",
         xytext = (5, 0),
         textcoords = "offset points",
         fontsize = fontSize)
annotate(r"$x_d$",
         xy = (-0.4, 0.2),
         xycoords = "data",
         xytext = (0, -15),
         textcoords = "offset points",
         fontsize = fontSize)
plot([-1, 0.2], [0.2, 0.2], linewidth = 2, linestyle = "--",
     c = "black", alpha = 0.5)

xlim(-2.5, 2.5)
ylim(-2.5, 2.5)
xticks([])
yticks([])

savefig("2D_Sinc_Interpolation_Demo.png", dpi = 200)
show()
