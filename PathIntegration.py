"""Written by Joseph Hayes for UC Berkeley CogSci 131 Assignment 3, Spring 2020"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cmx
import math


# Problem 1a: Suppose that an ant wandered randomly by taking steps (x,y), one per
# second, where at each ant step, x and y each come from a normal distribution with a mean
# of 0 and a standard deviation of 1.0mm (assume this for all questions below). Plot
# a trace of the ant’s path over the course of an hour.

def getColorList(colors):
    """Color gradient function created with the help of:
    https://stackoverflow.com/questions/12487060/matplotlib-color-according-to-class-labels/12487355
    by user https://stackoverflow.com/users/2444213/salomonvh """
    cmap = plt.cm.jet
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

    bounds = np.linspace(0, colors, colors + 1)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    scalarMap = cmx.ScalarMappable(norm=norm,cmap=cmap)
    list = []
    for i in range(colors):
        list += [scalarMap.to_rgba(i)]

    return list



def antRandomPath(randomFunction=np.random.normal, mean=0.0, stdev=1.0, step=1, time=3600, scale=1, color='red'):
    nest = [0, 0]
    dataPoints = np.array([nest])
    # vectors = np.array([nest])
    xAxis = list(range(1, time + 1, step))
    x1, y1 = nest
    maxX, maxY = x1, y1
    minX, minY = x1, y1
    # colors = getColorList(time)

    for a in xAxis:
        # color = colors[a - 1]
        dx = randomFunction(mean, stdev)
        dy = randomFunction(mean, stdev)
        plt.arrow(x=x1 * scale, y=y1 * scale, dx=dx * scale, dy=dy * scale, length_includes_head=True, head_width=.1, color=color, rasterized=True)
        x1 += dx
        y1 += dy
        dataPoints = np.append(dataPoints, [[x1, y1]], axis=0)
        if x1 > maxX:
            maxX = x1
        if y1 > maxY:
            maxY = y1
        if y1 < minY:
            minY = y1
        if x1 < minX:
            minX = x1

    minX *= scale
    minY *= scale
    plt.ylim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)
    plt.xlim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)

    x, y = dataPoints.T
    plt.text(0, 0, 'nest')
    plt.text(x1, y1, 'end')
    plt.title('Graph of a random wandering ant, one step/second, for one hour')
    plt.xlabel('Horizontal distance from the next in mm')
    plt.ylabel('Vertical distance from the next in mm')
    plt.scatter(0, 0, color='black')
    plt.scatter(x1, y1, color='black')
    plt.grid()
    plt.show()
    plt.savefig('assignment3_1a.pdf')

antRandomPath()
#end problem 1a


#end
