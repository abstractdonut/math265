import numpy as np


# yp is a function with parameters t and y, such as lambda t, y: 3t + 4y
# p0 is the initial condition y(p0[0]) = p0[1]
# dt is the change in t
# tf is the final value of t in the table
def euler(yp, p0, tf, dt):
    t0, y0 = p0
    n = (tf - t0 + dt) / dt
    T = list(np.linspace(t0, tf, n))
    Y = [y0]
    for i in range(0, len(T) - 1):
        Y.append(Y[i] + yp(T[i], Y[i]) * dt)
    YP = [yp(t, y) for (t, y) in zip(T, Y)]
    return (T, Y, YP)
