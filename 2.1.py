import numpy as np
from dirfield import dirfield


# WARNING: Be careful when iteratively creating lists of functions using lambda!
# Specifically, don't allow a lambda containing a bound variable, the lambda
# captures the variable, not the value of the variable.
# https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result

# 1 (a)
#sols = []
#def sol(c):
#    return lambda t: t/3 - 1/9 + np.exp(-2*t) + c * np.exp(-3*t)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: t + np.exp(-2 * t) - 3*y
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 2 (a)
#sols = []
#def sol(c):
#    return lambda t: 2 * np.exp(2 * t) * (t ** 3) / 3 + c * np.exp(2 * t)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: (t**2) * np.exp(2 * t) + 2 * y
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 3 (a)
#sols = []
#def sol(c):
#    return lambda t: t**2 * np.exp(-t) + 1 + c * np.exp(-t)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: t * np.exp(-t) - y + 1
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 4 (a)
#sols = []
#def sol(c):
#    return lambda t: (3/2)*np.sin(2*t) + 3*np.cos(2*t)/(2*t) + 3*c/t
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: 3 * np.cos(2 * t) - (1/t) * y
#dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 5 (a)
#sols = []
#def sol(c):
#    return lambda t: -3 * np.exp(t) + c * np.exp(2 * t)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: 3 * np.exp(t) + 2 * y
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 6 (a)
#sols = []
#def sol(c):
#    return lambda t: np.sin(t)/t**2 - np.cos(t)/t + c/t**2
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: np.sin(t) / t - 2 * y / t
#dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 7 (a)
#sols = []
#def sol(c):
#    return lambda t: (t ** 2 + c) * np.exp(- t ** 2)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: 2*t*np.exp(- t**2) - 2*t*y
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 8 (a)
#sols = []
#def sol(c):
#    return lambda t: (np.arctan(t) + c) / (1 + t**2) ** 2
#for c in range(-3, 4):
#    sols.append( (sol(c ** 3), "red") )     # Use c ** 3 to obtain a more 
#                                                   # appropriate range

#yp = lambda t, y: (1 + t**2) ** (-3) - 4*t*y / (1 + t**2)
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 9 (a)
#sols = []
#def sol(c):
#    return lambda t: 3*t - 6 + 3*np.exp(-t/2)*c/2
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: (3/2) * t - y/2
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 10 (a)
#sols = []
#def sol(c):
#    return lambda t: -t * np.exp(-t) + t * c
#for c in range(-3, 4):
#    if c == 0:
#        sols.append( (sol(c), "purple") )
#    else:
#        sols.append( (sol(.3 * c), "red") )

#yp = lambda t, y: t * np.exp(-t) + y / t
#dirfield(yp, hints=['hi-res', 'x-positive'], solutions=sols)

# 11 (a)
#sols = []
#def sol(c):
#    return lambda t: np.sin(2*t) - 2 * np.cos(2*t) + c * np.exp(-t)
#for c in range(-3, 4):
#    sols.append( (sol(c), "red") )

#yp = lambda t, y: 5 * np.sin(2 * t) - y
#dirfield(yp, hints=['hi-res'], solutions=sols)

# 12 (b)
#sols = []
#def sol(c):
#    return lambda t: 3 * (t**2 - 4*t + 8) + 3 * c * np.exp(-t / 2) / 2
#for c in range(-3, 4):
#    sols.append( (sol(10 * c), "red") )

#yp = lambda t, y: (3/2) * t**2 - y/2 
#dirfield(yp, hints=['hi-res', 'broad'], solutions=sols)



# 21 (b)
sols = []
#def sol(c):
#    return lambda t: 3 * (t**2 - 4*t + 8) + 3 * c * np.exp(-t / 2) / 2
#for c in range(-3, 4):
#    sols.append( (sol(10 * c), "red") )

yp = lambda t, y: 2*np.cos(t) + y/2
dirfield(yp, hints=['hi-res'], solutions=sols)



























