N = 5000

def f(x):
    return 2.0 * x / (1 + x * x)
    # return 1.0 / x

def g(x):
    return x * N

w = 1
for i in range(20):
    c = g(w)
    w = f(c) * w
    print c
