import random
import numpy as np
import matplotlib as plt

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
    return region[1] - region[0]

"""Problem 2"""
def conditionalProb(regionList, x, y):
    """Takes a list of regions as intervals and returns P(y | x)"""
    xRegions = [] #count of regions containing x
    yRegions = 0
    totalProb = 0

    for r in regionList:
        if contains(r, x):
            xRegions += [r]

            if contains(r, y):
                # totalProb += (condProb * (1 / size(xR)))
                totalProb += 1 / size(r)

    condProb = len(xRegions) / len(regionList)

    # for xR in xRegions:
    #
    #     if contains(xR, y):
    #         # totalProb += (condProb * (1 / size(xR)))
    #         totalProb += 1 / size(xR)


    # return totalProb / len(xRegions) #need to confirm the normalization method
    return (totalProb * condProb) / len(regionList)











#end
