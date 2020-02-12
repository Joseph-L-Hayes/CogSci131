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
class Assignment3():

    def distance(x1, y1, x2, y2):
        """Returns the Pythagorean distance between two points"""

        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

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


    def antRandomPath(randomFunction=np.random.normal, mean=0.0, stdev=1.0, step=1, time=3600, scale=1, color='red', plot=True, foodLoc=None, nest=[0,0], track=False):
        # nest = [0, 0]
        dataPoints = np.array([nest])
        # vectors = np.array([nest])
        timeAxis = list(range(1, time + 1, step))
        x1, y1 = nest
        shortestDist = 0

        if foodLoc is not None:
            x1, y1 = foodLoc
            shortestDist = Assignment3.distance(foodLoc[0], foodLoc[1], nest[0], nest[1])

        maxX, maxY = x1, y1
        minX, minY = x1, y1
        # colors = getColorList(time)
        if foodLoc is not None:
            plt.text(foodLoc[0], foodLoc[1], 'food')
            plt.scatter(foodLoc[0], foodLoc[1], color='black')
            color = 'blue'
            # nestDistance = Assignment3.distance(x1, y1, nest[0], nest[1])
            # if nestDistance <= 5.0:
            #     return 1

        for a in timeAxis:
            # color = colors[a - 1]
            dx = randomFunction(mean, stdev)
            dy = randomFunction(mean, stdev)

            if plot == True:
                plt.arrow(x=x1 * scale, y=y1 * scale, dx=dx * scale, dy=dy * scale, length_includes_head=True, head_width=.1, color=color, rasterized=True)

            nestDistance = Assignment3.distance(x1, y1, nest[0], nest[1])
            x1 += dx
            y1 += dy

            if track is True and foodLoc is not None:
                if nestDistance <= 5.0:
                    return 1

            if track is False and foodLoc is not None:
                shortestDist = min(shortestDist, nestDistance)

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

        if track == True:
            return 0
        if track == False and foodLoc is not None:
            print(shortestDist)
            return shortestDist
        else:
            return (x1, y1)

# Assignment3.antRandomPath(plot=False)
# print("dist: ", Assignment3.distance(-59.06819725288309, 5.947437155778581, 0, 0))
#end problem 1a

# Problem 1b: Let’s think about why ants need to perform path integration. Suppose that instead
# of path integration, when an ant found food, it just continued to wander with
# random steps until it got back to the nest. Using a simulation, estimate the probability
# that an ant who finds food after 1 hour will make its way back to within 5mm of the nest
# over the course of the next hour (note that if it comes within 5mm of a nest, it stops).
# How many simulations do you need to run? Do the results show that this is a good strategy?
# Why or why not?

# successes = 0
# numTrials = 10000
#
# for i in range(numTrials):
#     foodLocation = Assignment3.antRandomPath(plot=False)
#     successes += Assignment3.antRandomPath(plot=False, track=True, foodLoc=[foodLocation[0], foodLocation[1]])
#
# print('P(finds nest, 1 hour)=', successes / numTrials * 100, '%', '# samples:', numTrials)
"""Answer for 1b:
        P(finds nest, 1 hour)= 14.96 % # samples: 10000. After running 10,000 samples,
        the ant only gets within 5.0mm of the nest 14.96% of the time. This is
        very poor strategy, it is extremely inefficient"""
#end Problem 1b

# Problem 1c: If the ant searches for an hour, finds food, and then searches for the nest
# by continuing to walk at random, on average, what is the closest distance it will come to
# the nest over the course of the next hour? (Do not assume it stops if it comes within 5mm)
# Find this average distance with a simulation.


# Imagine the ant walks for an hour, and then continues to travel randomly for the next hour.
# You should keep track of the closest the ant comes to the nest over the course of the second hour.
# Now do this 500, 1000 etc times (some number of trials), and compute the average over all trials.
# So you are finding the closest distance to the nest, on average.

numTrials = 10
shortestDist = []

for i in range(numTrials):
    foodLocation = Assignment3.antRandomPath(plot=False)
    shortestDist += [Assignment3.antRandomPath(plot=False, track=False, foodLoc=[foodLocation[0], foodLocation[1]])]
# print(min(shortestDist))
print(sum(shortestDist) / numTrials)
#end
