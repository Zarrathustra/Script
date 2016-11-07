from pylab import *

figure(figsize = (10, 10), dpi = 200)

subplot(111, projection = 'polar')

labels = ["Correctness", "Clarity", "Cleverness"]
theta = [-60, 10, 30]
sizes = [70, 20, 10]
colors = ["yellowgreen", "lightskyblue", "gold"]

theta = [float(i) / 100 * 2 * pi for i in theta]
sizes = [float(i) / 100 * 2 * pi for i in sizes]

bar(theta, [1, 1, 1], width = sizes, bottom = 0, color = colors, lw = 0)

#for i in range(1):
#    annotate(labels[i], \
#             (theta[i], 0))

axis("off")

savefig("../Figures/Pie_Code.png", dpi = 200)
