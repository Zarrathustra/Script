from pylab import *
import matplotlib.patches as mpatches

filename = "Year_Map_Resolution.csv"

# Data Reading and Checking 
# Collecting and Cleaning Data
lines = open(filename, "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Y4A = [line.strip().split(",")[-1] for line in lines]
Y6A = [line.strip().split(",")[-3] for line in lines]
X.pop(0)
Y4A.pop(0)
Y6A.pop(0)
X = [int(x) for x in X]
Y4A = [int(y) for y in Y4A]
Y6A = [int(y) for y in Y6A]
Y4To6A = [Y6A[i] - Y4A[i] for i in range(len(X))]

figure(figsize = (10, 5), dpi = 80)

width = 0.5
alpha = 0.7

pos = [x + width / 2 for x in range(len(X))]
tickPos = [x + width for x in range(len(X))]
bar(pos, Y4A, width, color = "blue", alpha = alpha)
bar(pos, Y4To6A, width, color = "lightblue", bottom = Y4A, alpha = alpha)

xticks(tickPos, X)
ylim([0, 100])
xlabel("year")
ylabel("number of maps published")

bluePatch = mpatches.Patch(color = "blue", label = r"Resolution $\leq 4\AA$", alpha =
        alpha)
lightbluePatch = mpatches.Patch(color = "lightblue", label = r"Resolution $>4\AA, \leq 6\AA$", alpha = alpha) 

legend(handles = [bluePatch, lightbluePatch])

savefig("Year_Map_Resolution.png", dpi = 200)
show()
