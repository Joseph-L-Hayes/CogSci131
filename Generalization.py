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

"""Problem 2 What is the probability of getting x=1 for regions containing x=0?
    Answer: 0.05782114104160832 CONFIRM, CHECK FOR ERRORS"""
def conditionalProb(regionList, x, y):
    """Takes a list of regions as intervals and returns P(y | x)"""
    xRegions = [] #count of regions containing x
    yRegions = 0
    totalProb = 0
    result = 0
    intervalProb = []
    norm = 0

    for r in regionList:
        if contains(r, x):
            xRegions += [r]

            if contains(r, y):
                # totalProb += (condProb * (1 / size(xR)))
                intervalProb += [1 / size(r)]
                # print(intervalProb)
                norm += size(r)

    condProb = len(xRegions) / len(regionList)
    if norm: #change later
        # intervalProb = intervalProb / norm
        intervalProb = [condProb * p for p in intervalProb]
        totalProb = sum(intervalProb)
        result = totalProb / len(regionList)
        # print(intervalProb)
        # print("normed: ", intervalProb, condProb)
        # print("norm", norm)

    #still need to figure out the normalization issue

    # for xR in xRegions:
    #
    #     if contains(xR, y):
    #         # totalProb += (condProb * (1 / size(xR)))
    #         totalProb += 1 / size(xR)


    # return totalProb / len(xRegions) #need to confirm the normalization method
    # return (totalProb * condProb)
    return result #seems to give a better answer; over all r given x
    # return totalProb / len(regionList) #over all r


"""Problem 3"""
def plotProb(z, interval, regions):
    probList = []
    xAxis = []

    for i in range(interval + 1):
        xAxis += [i]
        probList += [conditionalProb(regions, z, i)]
        print(conditionalProb(regions, z, i))

    x, y = xAxis, probList

    plt.plot(x, y)
    # plt.yscale("log")
    plt.show()

plotProb(0, 10, regionList)









#end
