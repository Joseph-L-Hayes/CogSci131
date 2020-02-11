"""Written by Joseph Hayes for UC Berkeley CogSci 131 Assignment 3, Spring 2020"""

import numpy as np
import matplotlib.pyplot as plt
import math


# 1a. [5pts, HELP] Suppose that an ant wandered randomly by taking steps (x,y), one per
# second, where at each ant step, x and y each come from a normal distribution with a mean
# of 0 and a standard deviation of 1.0mm (assume this for all questions below). Plot
# a trace of the ant’s path over the course of an hour.

def antRandomPath(randomFunction=np.random.normal, mean=0.0, stdev=1.0, step=1, time=3600, scale=1):
    nest = [0, 0]
    dataPoints = np.array([nest])
    # vectors = np.array([nest])
    xAxis = list(range(1, time + 1, step))
    x1, y1 = nest
    x2, y2 = 0, 0
    # cmap = plt.cm.jet
    # cmaplist = [cmap(i) for i in range(cmap.N)]
    # cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

    for a in xAxis:
        dx = randomFunction(mean, stdev)
        dy = randomFunction(mean, stdev)
        plt.arrow(x=x1 * scale, y=y1 * scale, dx=dx * scale, dy=dy * scale, length_includes_head=True, head_width=.1, color='red')
        x1 += dx
        y1 += dy
        # x1, y1 = x2, y2
        # vectors = np.append(vectors, [[dx, dy]], axis=0)
        dataPoints = np.append(dataPoints, [[x1, y1]], axis=0)

        """ADD A TRACER FOR THE LARGEST X AN Y VALUES FOR SCALING"""

    limit = np.amax(dataPoints) * scale
    print(limit)
    plt.ylim(min(-1 * limit, limit) - 1, max(-1 * limit, limit) + 1)
    plt.xlim(min(-1 * limit, limit) - 1, max(-1 * limit, limit) + 1)

    # plt.ylim(min(-1 * y1, y1) - 1, max(-1 * y1, y1) + 1)
    # plt.xlim(min(-1 * x1, x1) - 1, max(-1 * x1, x1) + 1)

    x, y = dataPoints.T
    # dx, dy = vectors.T
    # plt.plot(x, y)
    plt.text(0, 0, 'nest')
    plt.text(x1, y1, 'end')
    # plt.scatter(x, y, cmap=cmap)
    # plt.scatter(x, y, c=y, cmap=cmap)
    # plt.scatter(x, y, s=5, c=y) s is the radius of the scatter point, c=y creates a gradient
    # plt.grid()
    plt.show()

    return dataPoints

antRandomPath()

#end
