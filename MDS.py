import numpy as np
import matplotlib.pyplot as plt
import random

"""Problem 1
    The dataset1 provides similarities, not distances. Write down three
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
    """Converts a similarity to a psychological distance"""
    return 1 - x

"""Problem 2
    Write a function that takes a vector/matrix of positions for each item and computes
    the stress."""
def stress(psyDist, pos_i, pos_j):
    """Returns the stress value of two """
    #stress = sum(i,j)(behavDist - euclidDist(posi, posj))**2

    return (psyDist - np.linalg.norm(pos_i - pos_j))**2

"""Problem 3
    Write down a function that takes a vector/matrix of positions and computes the gradient
    (e.g. applies the above numerical method of df/dp to each coordinate location)."""

def gradient(vector, h=0.001):
    """Returns the gradient of vector positions"""
    return None

def importCSV(csvFile, dataType, header=1):
    """Returns a numpy array without headers from a CSV file"""
    return np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)
    # return np.genfromtxt(csvFile,delimiter=",", names=True)

def convertArray(simArray, func):
    """Takes a similarity array and converts it to a psychological distance array using
        the supplied function func"""

    return np.apply_along_axis(func, 1, simArray) #doesn't like array w/headers, figure out later

def getRandPositions(rows, columns):
    """Returns a rows by columns matrix with random values"""
    return np.random.randn(rows, columns) #why not random.normal?

def importNames(csvFile, dataType, header=1):
    """Returns a numpy array without headers from a CSV file"""
    return np.genfromtxt(csvFile,delimiter=",", names=True)



#may need a main function to drive the code
importArray = importCSV('similarities.csv', float)
nameArray = importNames('similarities.csv', float) #doing this twice for now, convertArray doesn't like the headers
nameList = list(nameArray.dtype.names)
print(nameList)
psyArray = convertArray(importArray, simToDist)
# test = np.array([[ 0, 0],
# [0, 0]])

posArray = getRandPositions(21, 2)
# print(test[0])
# print(test[1])
# print(importArray[3, 6])
#
# print(stress(psyArray[3, 6], test[0], test[1]))

x, y = zip(*posArray)

# plt.scatter(x,y)
# plt.show()

#end
