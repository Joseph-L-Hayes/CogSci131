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
    """Takes a region tuple and returns if point is in the region"""
    return (region[0] <= point) and (region[1] >= point)

"""Problem 2"""
def conditionalProb(regionList, x, y):
    """Takes a list of regions as intervals and returns P(y | x)"""
    # for r in regionList:

    return None
