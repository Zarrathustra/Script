import sys
from pylab import *
import matplotlib.patches as mpatches

filename = "Software_HighestResolution_AverageResolution.csv"

# Data Reading and Checking 
lines = open(filename, "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
highest = [line.strip().split(",")[1] for line in lines]
average = [line.strip().split(",")[3] for line in lines]
X.pop(0)
highest.pop(0)
average.pop(0)

highest = [float(y) for y in highest]
average = [float(y) for y in average]

width = 0.3
highestPos = [x + width / 2 for x in range(len(X))]
averagePos = [x + width / 2 * 3 for x in range(len(X))]

figure(figsize = (10, 5), dpi = 80)

bar(highestPos, highest, width, color = "red", alpha = 0.5)
bar(averagePos, average, width, color = "blue", alpha = 0.5)

for i in range(len(X)):
    text(highestPos[i] - 0.03, highest[i] + 0.3, "%2.1f"%highest[i])
    text(averagePos[i] - 0.03, average[i] + 0.3, "%2.1f"%average[i])

xticks(averagePos, X)
ylabel(r"Resolution $\AA$")

red_patch = mpatches.Patch(color = "red", label = "Highest Resolution", alpha =
        0.5)
blue_patch = mpatches.Patch(color = "blue", label = "Average Resolution", alpha
        = 0.5)

legend(handles = [red_patch, blue_patch])

savefig("Software_Resolution.png", dpi = 200)
show()
