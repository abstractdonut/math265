import numpy as np


def euler(yp, p0, dt, tf):
    t0, y0 = p0
    n = (tf - t0 + dt) / dt
    t = list(np.linspace(t0, tf, n))
    y = [y0]
    for i in range(0, len(t)):
        y.append(y[i] + yp(t[i], y[i]) * dt)
    return (t, y)
