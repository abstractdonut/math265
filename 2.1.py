import numpy as np
from dirfield import dirfield


# WARNING: Be careful when iteratively creating lists of functions using lambda!
# Specifically, don't allow a lambda containing a bound variable, the lambda
# captures the variable, not the value of the variable.
# https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result

# 1 (a)
sols = []
def sol(c):
    return lambda t: t/3 - 1/9 + np.exp(-2*t) + c * np.exp(-3*t)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: t + np.exp(-2 * t) - 3*y
dirfield(yp, hints=['hi-res'], solutions=sols)

# 2 (a)
sols = []
def sol(c):
    return lambda t: 2 * np.exp(2 * t) * (t ** 3) / 3 + c * np.exp(2 * t)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: (t**2) * np.exp(2 * t) + 2 * y
dirfield(yp, hints=['hi-res'], solutions=sols)

# 3 (a)
sols = []
def sol(c):
    return lambda t: t**2 * np.exp(-t) + 1 + c * np.exp(-t)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: t * np.exp(-t) - y + 1
dirfield(yp, hints=['hi-res'], solutions=sols)

# 4 (a)
sols = []
def sol(c):
    return lambda t: (3/2)*np.sin(2*t) + 3*np.cos(2*t)/(2*t) + 3*c/t
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: 3 * np.cos(2 * t) - (1/t) * y
dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 5 (a)
sols = []
def sol(c):
    return lambda t: -3 * np.exp(t) + c * np.exp(2 * t)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: 3 * np.exp(t) + 2 * y
dirfield(yp, hints=['hi-res'], solutions=sols)

# 6 (a)
sols = []
def sol(c):
    return lambda t: np.sin(t)/t**2 - np.cos(t)/t + c/t**2
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: np.sin(t) / t - 2 * y / t
dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 7 (a)
sols = []
def sol(c):
    return lambda t: (t ** 2 + c) * np.exp(- t ** 2)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: 2*t*np.exp(- t**2) - 2*t*y
dirfield(yp, hints=['hi-res'], solutions=sols)

# 8 (a)
sols = []
def sol(c):
    return lambda t: (np.arctan(t) + c) / (1 + t**2) ** 2
for c in range(-3, 4):
    sols.append( (sol(c ** 3), "red") )     # Use c ** 3 to obtain a more 
                                                   # appropriate range

yp = lambda t, y: (1 + t**2) ** (-3) - 4*t*y / (1 + t**2)
dirfield(yp, hints=['hi-res'], solutions=sols)

# 9 (a)
sols = []
def sol(c):
    return lambda t: 3*t - 6 + 3*np.exp(-t/2)*c/2
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: (3/2) * t - y/2
dirfield(yp, hints=['hi-res'], solutions=sols)

# 10 (a)
sols = []
def sol(c):
    return lambda t: -t * np.exp(-t) + t * c
for c in range(-3, 4):
    if c == 0:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(.3 * c), "red") )

yp = lambda t, y: t * np.exp(-t) + y / t
dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 11 (a)
sols = []
def sol(c):
    return lambda t: np.sin(2*t) - 2 * np.cos(2*t) + c * np.exp(-t)
for c in range(-3, 4):
    sols.append( (sol(c), "red") )

yp = lambda t, y: 5 * np.sin(2 * t) - y
dirfield(yp, hints=['hi-res'], solutions=sols)

# 12 (b)
sols = []
def sol(c):
    return lambda t: 3 * (t**2 - 4*t + 8) + 3 * c * np.exp(-t / 2) / 2
for c in range(-3, 4):
    sols.append( (sol(10 * c), "red") )

yp = lambda t, y: (3/2) * t**2 - y/2 
dirfield(yp, hints=['hi-res', 'broad'], solutions=sols)



# 21 (a)
sols = []
def sol(c):
    return lambda t: (4/5)*(2*np.sin(t) - np.cos(t)) + c * np.exp(t/2)
for c in range(-3, 4):
    if c == 0:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(c), "red") )

yp = lambda t, y: 2*np.cos(t) + y/2
dirfield(yp, fname="$2\\cos(t) + \\frac{y}{2}$", hlines=[-4/5],
             hlinecolor="purple", hlinestyle="--", hints=['med-res'],
             solutions=sols)


# 22 (a)
sols = []
def sol(c):
    return lambda t: -3 * np.exp(t / 3) + c * np.exp(t / 2)
for c in range(-3, 4):
    if c == 0:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(c), "red") )

yp = lambda t, y: (np.exp(t/3) + y) / 2
dirfield(yp, fname="$\\frac{e^{t/3} + y}{2}$", hints=['med-res'],
             hlines=[-3], hlinecolor="purple", hlinestyle="--",
             solutions=sols)


# 23 (a)
sols = []
def sol(c):
    return lambda t: -2 * np.exp(-np.pi*t/2) / (np.pi + 4) + c * np.exp(2*t/3)
for c in range(-3, 4):
    if c == 0:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(c), "red") )

yp = lambda t, y: (np.exp(-np.pi * t / 2) + 2 * y) / 3
dirfield(yp, fname="$\\frac{e^{\\pi t/2} + 2y}{3}$", hints=['med-res'],
             solutions=sols)


# 24 (a)
sols = []
def sol(c):
    return lambda t: t * np.exp(-t) + c * np.exp(-t) / t
for c in range(-3, 4):
    if c == 0:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(c ** 3), "red") )

yp = lambda t, y: 2*np.exp(-t) - (t + 1) * y / t
dirfield(yp, fname="$2e^{-t} - \\frac{t+1}{t}y$",
             hints=['med-res', 'x-positive'], solutions=sols)


# 25 (a)
sols = []
def sol(c):
    return lambda t: (c - np.cos(t) ) / t ** 2
for c in range(-3, 4):
    if c == 1:
        sols.append( (sol(c ** 3), "purple") )
    else:
        sols.append( (sol(c ** 3), "red") )

yp = lambda t, y: np.sin(t) / t**2 - 2 * y / t
dirfield(yp, fname="$\\frac{\\sin(t)}{t^2} - \\frac{2y}{t}$",
             hints=['med-res', 'x-negative'], solutions=sols)


# 26 (a)
sols = []
def sol(c):
    return lambda t: (np.exp(t) + c) / np.sin(t)
for c in range(-3, 4):
    if c == -1:
        sols.append( (sol(c), "purple") )
    else:
        sols.append( (sol(c), "red") )

yp = lambda t, y: np.exp(t) / np.sin(t) - y / np.tan(t)
dirfield(yp, fname="$\\csc(t)e^t - cot(t)y$", xmin=0, xmax=np.pi,
             ymin=-10, ymax=10, xstep=.1, ystep=.6, r=.1, solutions=sols)


# 27
sol = lambda t: 4 * (2 * np.sin(t) + np.cos(t)) / 5 - 9 * np.exp(-t/2) / 5
yp = lambda t, y: 2 * np.cos(t) - y/2

import scipy.optimize
from scipy.optimize import fmin
tmax = fmin(lambda x: - sol(x), 0)
local_max = (tmax[0], sol(tmax[0]))

dirfield(yp, fname="$2\\cos(t) - \\frac{y}{2}$", hints=['med-res'],
             solutions=[(sol, "red")], points=[local_max])


# 28
y0 = -1.64288
sol = lambda t: -3*(2*t - 7) / 8  +  (y0 - 21/8) * np.exp(-2*t/3)
yp = lambda t, y: 1 - t/2 - 2 * y / 3
tangent = (2, 0)
dirfield(yp, fname="$1 - \\frac{t}{2} - \\frac{2y}{3}$", hints=['med-res'],
             solutions=[(sol, "red")], points=[tangent])


# 29
sol = lambda t: 12 + 8*(np.cos(2*t) + 8*np.sin(2*t))/65 - 788*np.exp(-t/4)/65
yp = lambda t, y: 3 + 2*np.cos(2*t) - t/4
dirfield(yp, fname="$3 + 2\\cos(2t) - \\frac{1}{4}t$",
             hints=["med-res", "broad"], solutions=[(sol, "red")], hlines=[12])






















