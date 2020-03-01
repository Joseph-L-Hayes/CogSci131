import numpy as np
import random


def importCSV(csvFile, dataType, header=1): #how to reference the sports without headers?
    """Returns a numpy array without headers from a CSV file"""
    return np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)

def simToDist(x):
    return 1 - x

def convertArray(simArray, func):
    """Takes a similarity array and converts it to a distance array using the supplied
        function func"""

    return np.apply_along_axis(func, 1, simArray)

def stress(vector):
    """Returns the stress of vector positions"""
    return None

def gradient(vector):
    """Returns the gradient of vector positions"""
    return None

array = importCSV('similarities.csv', float)
array = convertArray(array, simToDist)
print(array))

#end
