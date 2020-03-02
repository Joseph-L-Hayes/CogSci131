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
def stress(psychArray, pos_i, coordArray): #may need to take just the point from question 5, faster
    """Returns the stress of a single single point relative to other points"""

    stressSum = 0
    for j in range(len(coordArray)): #i != j
        if pos_i != j:
            target = coordArray[pos_i]
            dest = coordArray[j]
            stressSum += (psychArray[pos_i, j] - np.linalg.norm(target - dest)) ** 2

    return stressSum #need to test this vs stress() functionm

"""Problem 3
    Write down a function that takes a vector/matrix of positions and computes the gradient
    (e.g. applies the above numerical method of df/dp to each coordinate location)."""

def gradient(point, h=0.001):
    """Returns the gradient of a vector positions"""
    #may need to use the point only, array from parent function

    return (stress(point + h) - stress(point - h)) / (2*h)

def importCSV(csvFile, dataType, header=1):
    """Returns a numpy array without headers from a CSV file"""
    array = np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)
    return array

def convertArray(simArray, func):
    """Takes a similarity array and converts it to a psychological distance array using
        the supplied function func"""

    return np.apply_along_axis(func, 1, simArray) #doesn't like array w/headers, figure out later

def getRandPositions(rows, columns):
    """Returns a rows by columns matrix with random values"""
    return np.random.randn(rows, columns) #why not random.normal?

def getNames(csvFile, dataType, header=1):
    """Returns the header names form a CSV file"""
    array = np.genfromtxt(csvFile,delimiter=",", names=True)
    return list(array.dtype.names)

def makeLabels(nameList, positionArray, font_size=5):
    fig, labels = plt.subplots()

    for j in range(len(positionArray)):
        labels.annotate(nameList[j], positionArray[j], size=font_size, ha='left') #annotations work!


"""Problem 4 IDEA: MOVE EACH ITEM, compute stress, then move other items, set stress threshold for stopping?"""


#may need a main function to drive the code
i = 0
importArray = importCSV('similarities.csv', float)
nameList = getNames('similarities.csv', float) #doing this twice for now, convertArray doesn't like the headers
# print(nameList)
psyArray = convertArray(importArray, simToDist)
posArray = getRandPositions(21, 2)

makeLabels(nameList, posArray, 5)

part = stress(psyArray, nameList.index('football'), posArray)
print(nameList[i], "stress: ", part)


x, y = zip(*posArray)
colors = np.random.RandomState(0).rand(21)

plt.scatter(x,y, c=colors)
plt.show()

#end

# print(posArray)
# test = np.array([[0, 0],
# [0, 0]])
# print(test[0])
# print(test[1])
# print(importArray[0, 0])
#
# print(stress(psyArray[0, 0], test[0], test[1]))

# stressSum = 0 #we want to minimize the stress for the item, how to automate this?
# i = 0
# fig, labels = plt.subplots()

# for j in range(len(posArray)):
#     labels.annotate(nameList[j], posArray[i], posArray[j], size=5, ha='left') #annotations work!
