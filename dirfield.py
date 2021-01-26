import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import *

# https://stackoverflow.com/questions/12439588/how-to-maximize-a-plt-show-window-using-python/14537262
def maximize():
    plot_backend = plt.get_backend()
    mng = plt.get_current_fig_manager()
    if plot_backend == 'TkAgg':
        mng.resize(*mng.window.maxsize())
    elif plot_backend == 'wxAgg':
        mng.frame.Maximize(True)
    elif plot_backend == 'Qt4Agg':
        mng.window.showMaximized()


# solutions is a list of ordered pairs of the form (f, color), where f is the
# function to be plotted and color is the color of the solution.
def plot_solutions(solutions, xmin, xmax):
    x = np.linspace(xmin, xmax, num=400)
    for f, color in solutions:
        plt.plot(x, f(x), color)

# dirfield is an alteration of a solution posted on a matplotlib forum.
# http://matplotlib.1069221.n5.nabble.com/Need-help-with-direction-field-plot-td24886.html

# f must have parameters x, y, as in f(x, y). (f should really be called fprime 
# or yp but for now it is not worth it to me to change this.)
# fname is a string describing f, such as "-3exp(t) + 2y".
# solutions is a list of ordered pairs of the form (f, color), where f is the
# function to be plotted and color is the color of the solution.
# hlines are a list of y values for placement of horizontal red lines.
# hints may be one of 'hi-res', 'Q1'. 
def dirfield(f, fname="", hlines=[], hints=[], solutions=[],
             xmin=-10, xmax=10, ymin=-10,
             ymax=10, xstep=1, ystep=1, r=1,
             yvar='y', tvar='t'):
    if 'med-res' in hints:
        xstep = .4
        ystep = .4
        r = .4
    if 'hi-res' in hints:
        xstep = .2
        ystep = .2
        r = .2
    if 'Q1' in hints:
        xmin = -1
        xmax = 19
        ymin = -1
        ymax = 19
    if 'x-positive' in hints:
        xmin = -1
        xmax = 19
    if 'y-positive' in hints:
        ymin = -1
        ymax = 19
    if 'broad' in hints:
        xmin *= 5
        xmax *= 5
        ymin *= 5
        ymax *= 5
        xstep *= 5
        ystep *= 5
        r *= 5
    if 'narrow' in hints:
        xmin *= .25
        xmax *= .25
        ymin *= .25
        ymax *= .25
        xstep *= .25
        ystep *= .25
        r *= .25
    
    # coordinate initialization :
    x      = np.arange(xmin, xmax, xstep)
    if 'x-positive' in hints:
        x  = np.arange(0, xmax, xstep)
    y      = np.arange(ymin, ymax, ystep)
    x, y = np.meshgrid(x, y)
    
    # obtain aspect ration of slope field :
    xlength = xmax - xmin
    xcut = xlength % xstep if (xlength % xstep != 0) else xstep
    xlength -= xcut
    ylength = ymax - ymin
    ycut = ylength % ystep if (ylength % ystep != 0) else ystep
    ylength -= ycut
    ratio = ylength / xlength
    
    # differential function :
    yp = f(x, y)
    v  = np.sqrt((r**2) / (1 + 1/yp**2))   # length of arrow in y-dir
    u  = v/yp                              # length of arrow in x-dir
    nan = np.isnan(u)
    u[nan] = r
    
    # correct slope in relation to graph boundaries :
    slope = v / u
    slope /= ratio
    angle = np.arctan(slope)
    v = np.sin(angle)
    u = np.cos(angle)
    
    # plotting :
    fig = plt.figure()                                      # initialize figure
    gray = '#5f5f5f'                                        # color for axes
    plt.axhline(lw=2, c=gray)                                   # x-axis
    plt.axvline(lw=2, c=gray)                                   # y-axis
    plt.quiver(x, y, u, v, headwidth=0.0, 
                       headlength=0.0, 
                       headaxislength=0.0,
                       pivot='middle')                      # plot the dir. field
    for line in hlines:
        plt.axhline(y=line, c='r')                          # equilibrium isocline
    
    plt.ylim([ymin, ymax])                                      # plotting y-axis limits
    plt.xlim([xmin, xmax])                                      # plotting x-axis limits
    if fname:
        plt.title("Direction field for $\\frac{d%s}{d%s}$ = " % (yvar, tvar) + fname)  # title
    plt.xlabel("$%s$" % tvar)                                          # x-axis label
    plt.ylabel("$%s$" % yvar)                                          # y-axis label
    plot_solutions(solutions, xmin, xmax)
    maximize()
    plt.show()































