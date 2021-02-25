import numpy as np


# yp is a function with parameters t and y, such as lambda t, y: 3t + 4y
# p0 is the initial condition y(p0[0]) = p0[1]
# dt is the change in t
# tf is the final value of t in the table
def euler(yp, p0, dt, tf):
    t0, y0 = p0
    n = (tf - t0 + dt) / dt
    t = list(np.linspace(t0, tf, n))
    y = [y0]
    for i in range(0, len(t)):
        y.append(y[i] + yp(t[i], y[i]) * dt)
    return (t, y)
