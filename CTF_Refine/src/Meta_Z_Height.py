import os
import sys

from pylab import *
from mpl_toolkits.mplot3d import *

import scipy.linalg

N = int(sys.argv[3])

M = 600

def quat_norm(quat):
    w, x, y, z = quat
    return np.sqrt(w ** 2 + x ** 2 + y ** 2 + z ** 2)

def quat_conj(quat):
    w, x, y, z = quat
    return np.array([w, -x, -y, -z], dtype = np.float64)

def quat_mult(quat1, quat2):
    w0, x0, y0, z0 = quat1
    w1, x1, y1, z1 = quat2
    return np.array([-x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
                     x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
                     -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
                     x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0], dtype = np.float64)

lines = open(sys.argv[1], "r").readlines();

nM = int(sys.argv[2])

S = array([float(line.strip().split()[11]) for line in lines]) == nM

# print S

X = array([float(line.strip().split()[9]) for line in lines])[S]
Y = array([float(line.strip().split()[10]) for line in lines])[S]

Z = array([(float(line.strip().split()[1])  \
          + float(line.strip().split()[2])) \
         / 2 \
         * (float(line.strip().split()[22]) - 1) \
           for line in lines])[S]

# print X
# print Y
# print Z

quat = np.c_[array([float(line.strip().split()[13]) for line in lines])[S], \
             array([float(line.strip().split()[14]) for line in lines])[S], \
             array([float(line.strip().split()[15]) for line in lines])[S], \
             array([float(line.strip().split()[16]) for line in lines])[S]]

# for i in range(quat.shape[0]):
#     print quat_norm(quat[i, :])

# print quat

dire = np.zeros(quat.shape)

dire[:, 3] = 1

# print quat.shape

for i in range(quat.shape[0]):
    dire[i, :] = quat_mult(dire[i, :], quat_conj(quat[i, :]))
    dire[i, :] = quat_mult(quat[i, :], dire[i, :])

# for i in range(dire.shape[0]):
#     print quat_norm(dire[i, :])

fig = figure(figsize = (10, 10), dpi = 80)

ax = fig.add_subplot(111, projection = '3d')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#ax.quiver(X, Y, Z, dire[:, 1], dire[:, 2], dire[:, 3] / N * (2 * M), length = N / 20, arrow_length_ratio = 0.5)
ax.scatter(X, Y, Z)

#C,_,_,_ = scipy.linalg.lstsq(np.c_[X, Y, np.ones(len(X))], Z)

C,_,_,_ = scipy.linalg.lstsq(np.c_[np.ones(len(X)), \
                                   X,
                                   Y,
                                   X * Y,
                                   X ** 2,
                                   Y ** 2], Z)

print C

meshX, meshY = np.meshgrid(np.arange(0, N, N / 10), \
                           np.arange(0, N, N / 10))

#meshZ = C[0] * meshX + C[1] * meshY + C[2]

meshZ = np.dot(np.c_[np.ones(meshX.flatten().shape), \
                     meshX.flatten(), \
                     meshY.flatten(), \
                     meshX.flatten() * meshY.flatten(), \
                     meshX.flatten() ** 2, \
                     meshY.flatten() ** 2], \
               C).reshape(meshX.shape)

ax.plot_wireframe(meshX, meshY, meshZ, rstride = 1, cstride = 1, color = 'red', alpha = 0.5)

# xticks([500, 1500, 2500, 3500])
# yticks([500, 1500, 2500, 3500])

ax.set_xlim(0, N)
ax.set_ylim(0, N)
ax.set_zlim(-M, M)

xticks([0, N / 4, N / 2, N / 4 * 3, N])
yticks([0, N / 4, N / 2, N / 4 * 3, N])

show()
