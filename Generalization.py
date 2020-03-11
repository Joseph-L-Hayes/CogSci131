import random
import numpy as np
import matplotlib.pyplot as plt

"""Problem 0, Generate regions between [-10, 10]"""
def generateRegions(numRegions, low, high):
    #numpy.random.uniform(low=0.0, high=1.0, size=None)
    regions = [sorted((np.random.uniform(low, high), np.random.uniform(low, high))) for n in range(numRegions)]
    return regions

regionList = generateRegions(10000, -10, 10)

"""Problem 1"""
def contains(region, point):
    """Takes a region as a 2 element list or tuple and returns if point is in the region"""
    return (region[0] <= point) and (region[1] >= point)

def size(region):
    # print(region[1] - region[0])
    return region[1] - region[0]

"""Problem 2:  What is the probability of getting x=1 for regions containing x=0?
    ANSWER: ~0.10613579023117636 """

def conditionalProb(regions, x, y):
    """Takes a list of regions as intervals and returns P(y | x ∈ r)"""

    xRegions = 0
    totalProb = 0
    intervalProb = []

    for r in regions:
        if contains(r, x):
            xRegions += 1

            if contains(r, y):
                intervalProb += [1 / size(r)]

    if intervalProb and xRegions:
        condProb = 1 / xRegions
        intervalProb = [condProb * p for p in intervalProb]
        totalProb = sum(intervalProb)

        return totalProb
    else:
        return 0

# regionList = generateRegions(10000, -10, 10)
# print(conditionalProb(regionList, 0, 1))

"""Problem 3: Plot the probability of getting x for x ranging from 0 to 10, for regions
    containing x=0. What does this function look like? Write a sentence explaining why
    intuitively.

    ANSWER: INCOMPLETE """

def plotProb(z, interval, regions, saveName=None, scale='linear'):
    probList = []
    xAxis = []

    for i in range(interval + 1):
        xAxis += [i]
        probList += [conditionalProb(regions, z, i)]

    x, y = xAxis, probList

    plt.plot(x, y)
    plt.yscale(scale)
    plt.title('P(x | x=' + str(z) + ' ∈ r)')
    plt.xlabel('X Range')
    plt.ylabel('Probability')

    if saveName:
        plt.savefig(saveName + '.pdf')

    plt.show()

# regionList = generateRegions(10000, -10, 10)
# plotProb(0, 10, regionList, 'a6_p3')

"""Problem 4: """








#end
