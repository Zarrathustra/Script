from pylab import *
import matplotlib.patches as mpatches

lines = open("../Data/Compiler_Comparison.csv", "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Y1 = [line.strip().split(",")[1] for line in lines]
Y2 = [line.strip().split(",")[2] for line in lines]

X.pop(0)
Y1.pop(0)
Y2.pop(0)
X = [int(x) for x in X]
Y1 = [int(y) for y in Y1]
Y2 = [int(y) for y in Y2]

X_3 = [x**3 for x in X]

figure(figsize = (15, 8), dpi = 80)

lw = 2
sz = 20

plot(X_3, Y1, linewidth = lw, color = "red")
plot(X_3, Y2, linewidth = lw, color = "blue")

scatter(X_3, Y1, s = 20, color = "red")
scatter(X_3, Y2, s = 20, color = "blue")

xlabel("number of projections")
ylabel("time consumed (us)")

xlim([0, X_3[-1]])
ylim([0, float(max(Y1[-1], Y2[-1])) * 1.2])

X_ticks = [r"${%d}^3$" % x for x in X]
xticks(X_3, X_ticks)

redPatch = mpatches.Patch(color = "red", label = "g++")
bluePatch = mpatches.Patch(color = "blue", label = "icc")

legend(handles = [redPatch, bluePatch])

title("Performance Comparision Between icc and g++ in Practice")

savefig("../Figures/Compiler_Comparison.png", dpi = 200)
show()
