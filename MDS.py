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
def stress(psychArray, coordArray):
    """Returns the stress value of the current graph"""
    stressSum = 0

    for j in range(len(coordArray)):
        for i in range(len(coordArray)):
            if i != j:
                target = coordArray[i]
                dest = coordArray[j]
                stressSum += (psychArray[i, j] - np.linalg.norm(target - dest)) ** 2

    return stressSum #need to test this vs stress() functionm

"""Problem 3
    Write down a function that takes a vector/matrix of positions and computes the gradient
    (e.g. applies the above numerical method of df/dp to each coordinate location)."""

def gradient(point, psychArray, coordArray, h=0.001): #be sure to take small steps in the direction of the gradient (e.g. 0.01*gradient)
    #There is not a difference in the function; the difference is in the input. You
    #input the entire matrix to the stress function when computing the gradient, but
    #a single value has .001 added to or subtracted from it.
    """Returns the gradient of a vector positions"""
    plusArrayX = np.copy(coordArray)
    minusArrayX = np.copy(coordArray) #success?
    plusArrayY = np.copy(coordArray)
    minusArrayY = np.copy(coordArray) #success?
    minusArrayX[point][0] -= h
    plusArrayX[point][0] += h
    minusArrayY[point][1] -= h
    plusArrayY[point][1] += h

    dx = (stress(psychArray, plusArrayX) - stress(psychArray, minusArrayX)) / (2*h)
    dy = (stress(psychArray, plusArrayY) - stress(psychArray, minusArrayY)) / (2*h)

    # print(plusArray)

    # print(minusArray)
    # print("plus: ", stress(psychArray, plusArray))
    # print("minus: ", stress(psychArray, minusArray))
    # return (stress(psychArray, plusArray) - stress(psychArray, minusArray)) / (2*h)
    return dx, dy

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
nameList2 = [i + '2' for i in nameList]
# print(nameList)
psyArray = convertArray(importArray, simToDist)
posArray_orig = getRandPositions(21, 2)
posArray_mod = np.copy(posArray_orig) #to save original array

x1, y1 = zip(*posArray_orig)
# print("stress value before : ", stress(psyArray, posArray))
# print("pos before: ", posArray)
# part = stress(psyArray, posArray, nameList.index('football'))
gradX, gradY = 0,0
stressVal = 2000
iterations = 0
while stressVal >= 100:
    for x in range(0, len(posArray_mod)):
        gradX, gradY = gradient(x, psyArray, posArray_mod, .001)
        posArray_mod[x][0] += (gradX * -.001) #correct method for moving? applies change to both coords equally...
        posArray_mod[x][1] += (gradY * -.001)
        stressVal = stress(psyArray, posArray_mod) #update stress
        iterations += 1
        if iterations % 100 == 0:
            print(iterations)
print(stressVal)
#after change in point position
# print("stress value after : ", stress(psyArray, posArray))
print("gradientX: ", gradX, "gradientY: ",gradY)
"""After figuring out the single iteration, getting min stress value, need to try N trials with random positions to ensure global minima is reached"""
x2, y2 = zip(*posArray_mod)
colors1 = np.random.RandomState(0).rand(21)
# colors2 = np.random.RandomState(0).rand(21)
# print("pos after:", posArray)
posArray_final = np.concatenate((posArray_orig, posArray_mod))
print(posArray_final)
nameList_final = nameList + nameList2
# print(nameList_final)
makeLabels(nameList_final, posArray_final, 5)
makeLabels(nameList2, posArray_mod, 5)
# plt.scatter(x1,y1, c='black')
plt.scatter(x2,y2, c=colors1)
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
