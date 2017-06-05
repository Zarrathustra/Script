import os
import sys

from pylab import *

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

quat = np.c_[array([float(line.strip().split()[0]) for line in lines]), \
             array([float(line.strip().split()[1]) for line in lines]), \
             array([float(line.strip().split()[2]) for line in lines]), \
             array([float(line.strip().split()[3]) for line in lines])]

dire = np.zeros(quat.shape)

dire[:, 3] = 1

for i in range(quat.shape[0]):
    dire[i, :] = quat_mult(dire[i, :], quat_conj(quat[i, :]))
    dire[i, :] = quat_mult(quat[i, :], dire[i, :])
    print '{: .8f} {: .8f} {: .8f}'.format(dire[i, 1], dire[i, 2], dire[i, 3])
