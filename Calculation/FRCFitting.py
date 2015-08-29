from numpy import *

N = 7676

A = 0.07

DF1 = 24146 * 4
DF2 = 24258 * 4
lam = 0.019

arc = arctan(A / sqrt(1 - A * A))
con = 2 / (pi * lam * (DF1 + DF2))

def zeroPoint(n):
    return sqrt(con * (-arc + n * pi))

w1 = zeroPoint(1)
w2 = zeroPoint(2)

print w1
print w2

print w1 * N
print w2 * N
