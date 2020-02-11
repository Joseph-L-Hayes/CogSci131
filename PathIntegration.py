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

def antRandomPath(randomFunction=np.random.normal, mean=0.0, stdev=1.0, step=1, time=3600, scale=1, color='red', plot=True, nest=[0,0]):
    # nest = [0, 0]
    dataPoints = np.array([nest])
    # vectors = np.array([nest])
    timeAxis = list(range(1, time + 1, step))
    x1, y1 = nest
    maxX, maxY = x1, y1
    minX, minY = x1, y1
    # colors = getColorList(time)

    for a in timeAxis:
        # color = colors[a - 1]
        dx = randomFunction(mean, stdev)
        dy = randomFunction(mean, stdev)

        if plot == True:
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

    if plot == True:
        minX *= scale
        minY *= scale
        plt.ylim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)
        plt.xlim(min(minY, minX) - 1, max(abs(maxY), abs(maxX)) + 1)

        x, y = dataPoints.T
        plt.text(nest[0], nest[1], 'nest')
        plt.text(x1, y1, 'end')
        plt.title('Graph of a random wandering ant, one step/second, for one hour')
        plt.xlabel('Horizontal distance from the next in mm')
        plt.ylabel('Vertical distance from the next in mm')
        plt.scatter(nest[0], nest[1], color='black')
        plt.scatter(x1, y1, color='black')
        plt.grid()
        plt.show()
        # plt.savefig('assignment3_1a.pdf')

    return (x1, y1)

antRandomPath(plot=False)
#end problem 1a

# Problem 1b: Let’s think about why ants need to perform path integration. Suppose that instead
# of path integration, when an ant found food, it just continued to wander with
# random steps until it got back to the nest. Using a simulation, estimate the probability
# that an ant who finds food after 1 hour will make its way back to within 5mm of the nest
# over the course of the next hour (note that if it comes within 5mm of a nest, it stops).
# How many simulations do you need to run? Do the results show that this is a good strategy?
# Why or why not?

#ant looks for food for 3600 s, randomly wanders for another 3600 s looking for the nest
#so integrate a start location in above function, no plot
#run a loop using antRandomPath, take returned tuple as new start and run antRandomPath again
#but with a check for distance from nest.

#take a sufficient number of samples and remember to normalize (?)
#can do 1=success, 0=failure. Take a percentage of successes over total

#end
