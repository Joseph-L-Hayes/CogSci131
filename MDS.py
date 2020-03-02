import numpy as np
import random

"""Problem 1 The dataset1 provides similarities, not distances. Write down three
    ways you could convert a similarity to a distance ψij and choose one to use in the
    code. Briefly explain why you chose it over the others.
    1. Use the formula distance = (1 - similarity)
    2. Use the formula distance = 1 / similarity
    3.
    
    I will use distance = (1 - similarity) because it maintains the same scale as
    the similarity matrix and doesn't require normalizing. It is also easier for me
    to conceptualize in my head, if two categories have a similarity score of 1
    then their distance = 1 - 1 = 0 meaning they are in the same location. """

#dist = np.linalg.norm(a-b) #for distance between two points

def simToDist(x):
    """Converts a similarity measurement to a behavioral distance"""
    return 1 - x

def importCSV(csvFile, dataType, header=1): #how to reference the sports without headers?
    """Returns a numpy array without headers from a CSV file"""
    return np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)

def convertArray(simArray, func):
    """Takes a similarity array and converts it to a behavioral distance array using
        the supplied function func"""

    return np.apply_along_axis(func, 1, simArray)

def stress(vector):
    """Returns the stress of vector positions"""
    return None

def gradient(vector):
    """Returns the gradient of vector positions"""
    return None

array = importCSV('similarities.csv', float)
array = convertArray(array, simToDist)
print(array)

#end
