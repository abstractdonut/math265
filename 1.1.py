from dirfield import dirfield
import numpy as np

# Problems 1.1.1 - 1.1.6; 1.1.11 - 1.1.14; 1.1.25(d)-1.1.33 in Boyce & DiPrima

# 1
yp = lambda t, y: 3 - 2*y
dirfield(yp, fname="$3 - 2y$", hlines=[1.5], hints=['med-res', 'narrow'])
# as t increases, y converges to 1.5

# 2
yp = lambda t, y: 2*y - 3
dirfield(yp, fname="$2y - 3$", hlines=[1.5], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > 1.5 at t = 0
#   - y decreases without bound if y < 1.5 at t = 0
#   - y stays constant if y = 1.5 at t = 0     

# 3
yp = lambda t, y: 3 + 2 * y
dirfield(yp, fname="$3 + 2y$", hlines=[-1.5], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > -1.5 at t = 0
#   - y decreases without bound if y < -1.5 at t = 0
#   - y stays constant if y = -1.5 at t = 0  


# 4
yp = lambda t, y: -1 - 2 * y
dirfield(yp, fname="$-1 - 2y$", hlines=[-0.5], hints=['med-res', 'narrow'])
# as t increases, y converges to -0.5

# 5
yp = lambda t, y: 1 + 2 * y
dirfield(yp, fname="$1 + 2y$", hlines=[-0.5], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > -0.5 at t = 0
#   - y decreases without bound if y < -0.5 at t = 0
#   - y stays constant if y = -0.5 at t = 0  

# 6
yp = lambda t, y: y + 2
dirfield(yp, fname="$y + 2$", hlines=[-2], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > -2 at t = 0
#   - y decreases without bound if y < -2 at t = 0
#   - y stays constant if y = -2 at t = 0  


# 11
yp = lambda t, y: y * (4 - y)
dirfield(yp, fname="$y(4-y)$", hlines=[0, 4], hints=['med-res'])
# as t increases,
#   - y approaches 4 if y > 0 at t = 0
#   - y decreases with bound if y < 0 at t = 0
#   - y stays constant if y = 0 at t = 0  



# 12
yp = lambda t, y: -y * (5 - y)
dirfield(yp, fname="$-y(5 - y)$", hlines=[0, 5],
             xmin=-5, xmax=5, xstep=.25, ymin=-2, ymax=8, ystep=.15, r=.15)
# as t increases,
#   - y increases without bound if y > 5 at t = 0
#   - y stays constant if y = 5 at t = 0
#   - y approaches 0 if y < 5 at t = 0  



# 13
yp = lambda t, y: y**2
dirfield(yp, fname="$y^2$", hlines=[0], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > 0 at t = 0
#   - y stays constant if y = 0 at t = 0
#   - y approaches 0 if y < 0 at t = 0



# 14
yp = lambda t, y: y * (y - 2) ** 2
dirfield(yp, fname="$y(y-2)$", hlines=[0, 2], hints=['med-res', 'narrow'])
# as t increases,
#   - y increases without bound if y > 2 at t = 0
#   - y approaches 2 if 0 < y <= 2 at t = 0
#   - y stays constant if y = 0 at t = 0
#   - y decreases without bound if y < 0 at t = 0


# 25 (d)
yp = lambda t, y: 10 * 9.81 - 0.040857976 * y ** 2
dirfield(yp, fname="$981 - 0.040857976y^2$", hlines=[49],
             xmin=0, xmax=10, ymin=45, ymax=55, xstep=.2, ystep=.2, r=.2)

# 26
yp = lambda t, y: -2 + t - y
dirfield(yp, fname="$-2 + t - y$", hints=["med-res"])
# as t->inf, y->inf


# 27 (requires fullscreen)
yp = lambda t, y: t * np.exp(-2 * t) - 2 * y
dirfield(yp, fname="$e^{-2t} - 2y$", hints=['med-res', 'narrow'])
# as t->inf, y->0

# 28 (requires fullscreen)
yp = lambda t, y: np.exp(-t) + y
dirfield(yp, fname="$e^{-t}$", hints=['med-res'], xstep=.2, ystep=.2, r=.2)
# as t->inf,
#   - if y=0 when t=0, then y->0
#   - if y>0 when t=0, then y->inf
#   - if y<0 when t=0, then y->-inf

# 29
yp = lambda t, y: t + 2*y
dirfield(yp, fname="$t + 2y$", hints=['med-res', 'narrow'])
# as t->inf,
#   - if y > 0 when t=0, then y->inf
#   - if y <= 0 when t=0, then y->-inf


# 30
yp = lambda t, y: 3 * np.sin(t) + 1 + y
dirfield(yp, fname="$3\\sin(t) + 1 + y$", hints=['med-res'])
#             xmin=0, xmax=10, ymin=-5, ymax=5, xstep=.2, ystep=.2, r=.2)
# as t->inf,
#   - if y > -1 when t=0, then y->inf
#   - if y = -1 when t=0, then y has no limit
#   - if y < -1 when t=0, then y->-inf

# 31
yp = lambda t, y: 2 * t - 1 - y ** 2
dirfield(yp, fname="$2t - 1 - y^2$",
             xmin=-1, xmax=10, ymin=-7.5, ymax=7.5, xstep=.2, ystep=.2, r=.2)
# Let a be a critical y value for which the behavior of the DE changes at t=0.
#	- When y(0) > a, y→inf as t→inf
#	- When y(0) < a, y→-inf as t→inf

# 32
yp = lambda t, y: -(2*t + y) / (2 * y)
dirfield(yp, fname="$-\\frac{2t + y}{2y}$", hints=['med-res'])
# y -> 0 as t -> inf.


# 33
yp = lambda t, y: (1/6) * y ** 3 - y - (1/3) * t ** 2
dirfield(yp, fname="$\\frac{1}{6}y^3 - y - \\frac{1}{3}t^2$",
             xmin=-5, xmax=5, ymin=-3, ymax=7, xstep=.2, ystep=.2, r=.2)
# as t->inf
#   - if y>=sqrt(6) when t=0, then y->inf
#   - if y<sqrt(6) when t=0, then y->-inf


























