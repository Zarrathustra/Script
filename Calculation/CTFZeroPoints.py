from numpy import *

N = 512

A = 0.07

DF1 = 1e4
DF2 = 2e4
lam = 0.01

arc = arctan(A / sqrt(1 - A * A))
con = 2 / (pi * lam * (DF1 + DF2))

w1 = sqrt(con * (-arc + pi))
w2 = sqrt(con * (-arc + 2 * pi))

print w1
print w2

print w1 * N
print w2 * N
