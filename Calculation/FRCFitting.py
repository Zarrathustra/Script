from numpy import *

N = 3838

A = 0.07

DF1 = 17963
DF2 = 18713
lam = 0.0196

pixelSize = 1.32

arc = arctan(A / sqrt(1 - A * A))
con = 2 / (pi * lam * (DF1 + DF2))

def zeroPoint(n):
    return sqrt(con * (-arc + n * pi))

w1 = zeroPoint(1)
w2 = zeroPoint(2)

print w1
print w2

print w1 * N * pixelSize
print w2 * N * pixelSize
