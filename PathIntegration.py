"""Written by Joseph Hayes for UC Berkeley CogSci 131 Assignment 3, Spring 2020"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cmx
import math


# 1a. [5pts, HELP] Suppose that an ant wandered randomly by taking steps (x,y), one per
# second, where at each ant step, x and y each come from a normal distribution with a mean
# of 0 and a standard deviation of 1.0mm (assume this for all questions below). Plot
# a trace of the ant’s path over the course of an hour.

def getColorList(colors):
    cmap = plt.cm.jet
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]
    # create the new map
    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

    # define the bins and normalize
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
        # print(a)
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

    # limit = np.amax(dataPoints) * scale
    # print(limit)
    # plt.ylim(min(-1 * limit, limit) - 1, max(-1 * limit, limit) + 1)
    # plt.xlim(min(-1 * limit, limit) - 1, max(-1 * limit, limit) + 1)

    # limit = max(maxX, maxY)
    # print(limit)
    minX *= scale
    minY *= scale
    plt.ylim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)
    plt.xlim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)


    x, y = dataPoints.T
    # dx, dy = vectors.T
    # plt.plot(x, y)
    plt.text(0, 0, 'nest')
    plt.text(x1, y1, 'end')
    # plt.scatter(x, y, cmap=cmap)
    # plt.scatter(x, y, c=y)
    # plt.scatter(x, y, s=5, c=y) s is the radius of the scatter point, c=y creates a gradient
    plt.grid()
    plt.show()

    return dataPoints

antRandomPath()

#end
