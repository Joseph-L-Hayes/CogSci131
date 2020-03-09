import random
import numpy as np
import matplotlib as plt


def generateRegions(numRegions, low, high):
    #numpy.random.uniform(low=0.0, high=1.0, size=None)
    regions = [sorted((np.random.uniform(low, high), np.random.uniform(low, high))) for n in range(numRegions)]
    return regions

def contains(region, point):
    """Takes a region tuple and returns if point is in the region"""
    return (region[0] <= point) and (region[1] >= point)
