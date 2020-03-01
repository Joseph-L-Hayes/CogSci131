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
    array = np.array(21, dtype=float)
    for x in range(21):
        array[x] = np.apply_along_axis(func, x, simArray) #errors

    return array

def stress(vector):
    """Returns the stress of vector positions"""
    return None

def gradient(vector):
    """Returns the gradient of vector positions"""
    return None

array = importCSV('similarities.csv', float)
print(array)
print(array.shape)
convertArray(array, simToDist)
print(array)


#end
