import sys
from pylab import *

N = 30 
X = np.random.rand(N)
Y = np.random.rand(N)

clusterCentreX = np.random.rand(3)
clusterCentreY = np.random.rand(3)

clusters = [[], [], []]

colors = ["red", "blue", "green"]
size = 50

def plotCentre(ax):
    ax.scatter(clusterCentreX, clusterCentreY,
               marker = "D", color = colors, s = size, alpha = 1)

def plotClusters(ax):
    for i in range(3):
        subX = [observation[0] for observation in clusters[i]]
        subY = [observation[1] for observation in clusters[i]]
        ax.scatter(subX, subY, color = colors[i], s = size, alpha = 0.5)

def formatSubplot(i):
    xlim(0, 1)
    ylim(0, 1)
    xticks([])
    yticks([])
    title(i)

def assign():
    global clusters
    clusters = [[], [], []]
    for x, y in zip(X, Y):
        distance = Inf
        for i in range(3):
            newDistance = (x - clusterCentreX[i]) ** 2
            newDistance += (y - clusterCentreY[i]) ** 2
            if newDistance < distance:
                distance = newDistance
                index = i
        clusters[index].append((x, y))

def update():
    global clusterCentreX, clusterCentreY
    for i in range(3):
        subX = [observation[0] for observation in clusters[i]]
        subY = [observation[1] for observation in clusters[i]]
        clusterCentreX[i] = np.mean(subX)
        clusterCentreY[i] = np.mean(subY) 

figure(figsize = (8, 12), dpi = 80)

# THE FIRST FIGURE
subplot(3, 2, 1)
ax1 = gca()
formatSubplot("A");

plotCentre(ax1)
ax1.scatter(X, Y, color = "black", s = size, alpha = 0.5)

# THE SECOND FIGURE
subplot(3, 2, 2)
ax2 = gca()
formatSubplot("B");

plotCentre(ax2)
assign()
plotClusters(ax2)

# THE THIRD FIGURE
subplot(3, 2, 3)
ax3 = gca()
formatSubplot("C");

plotClusters(ax3)
update()
plotCentre(ax3)

# THE FOURTH FIGURE
subplot(3, 2, 4)
ax4 = gca()
formatSubplot("D");

plotCentre(ax4)
assign()
plotClusters(ax4)

# THE FIFTH FIGURE
subplot(3, 2, 5)
ax5 = gca()
formatSubplot("E")

plotClusters(ax5)
update()
plotCentre(ax5)

# THE SIXTH FIGURE
subplot(3, 2, 6)
ax6 = gca()
formatSubplot("F")

plotCentre(ax6)
assign()
plotClusters(ax6)

# Save figure and show
savefig("KMeansDemo.png", dpi = 200)
show()
