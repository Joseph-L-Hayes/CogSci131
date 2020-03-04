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

def simToDist(x):
    """Converts a similarity to a psychological distance"""
    return 1 - x

"""Problem 2
    Write a function that takes a vector/matrix of positions for each item and computes
    the stress."""
def stress(psychArray, coordArray):
    """Returns the stress value of the current graph"""
    stressSum = 0

    for i in range(len(coordArray)):
        for j in range(len(coordArray)):
            if i != j:
                target = coordArray[i]
                dest = coordArray[j]
                stressSum += (psychArray[i, j] - np.linalg.norm(target - dest)) ** 2

    return stressSum

"""End Problem 2"""

"""Problem 3
    Write down a function that takes a vector/matrix of positions and computes the gradient
    (e.g. applies the above numerical method of df/dp to each coordinate location)."""

def gradient(point, psychArray, coordArray, h=0.001):
    """Returns the gradient with respect to x and y in point"""
    plusArrayX = np.copy(coordArray)
    minusArrayX = np.copy(coordArray)
    plusArrayY = np.copy(coordArray)
    minusArrayY = np.copy(coordArray)
    minusArrayX[point][0] -= h
    plusArrayX[point][0] += h
    minusArrayY[point][1] -= h
    plusArrayY[point][1] += h

    dx = (stress(psychArray, plusArrayX) - stress(psychArray, minusArrayX)) / (2*h)
    dy = (stress(psychArray, plusArrayY) - stress(psychArray, minusArrayY)) / (2*h)

    return dx, dy
"""End Problem 3"""

"""Problem 4 IDEA: MOVE EACH ITEM, compute stress, then move other items, set stress threshold for stopping?
    Explanation: """
def traceGradient(psycho_array, learn_rate=.01, gradient_threshold=0.5, n=1000, dimensions=2):
    """Takes a psychological distance array, returns a position array with min(stress) after n iterations and it's stress value"""

    grad_x, grad_y = 10000, 10000
    grad_total = 10000
    min_stress = float('inf')
    stress_value = float('inf')
    best_positions = None

    for i in range(n + 1):
        x, y = 0, 1
        position_array = getRandPositions(psycho_array.shape[0], dimensions)
        while (grad_x > gradient_threshold) and (grad_y > gradient_threshold):
            for point in range(0, len(position_array)):
                grad_x, grad_y = gradient(point, psycho_array, position_array, h=.001)
                position_array[point][x] += (-grad_x * learn_rate)
                position_array[point][y] += (-grad_y * learn_rate)

        grad_x, grad_y = 10000, 10000

        stress_value = stress(psycho_array, position_array)

        if stress_value < min_stress:
            min_stress = stress_value
            best_positions = position_array

    return best_positions, min_stress

def importCSV(csvFile, dataType, header=1):
    """Returns a numpy array without headers from a CSV file"""
    array = np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)
    return array

def convertArray(simArray, func):
    """Takes a similarity array and converts it to a psychological distance array using
        the supplied function func"""

    return np.apply_along_axis(func, 1, simArray)

def getRandPositions(rows, columns):
    """Returns a rows by columns matrix with random values"""
    return np.random.randn(rows, columns)

def getNames(csvFile, dataType, header=1):
    """Returns the header names form a CSV file"""
    array = np.genfromtxt(csvFile,delimiter=",", names=True)
    return list(array.dtype.names)

def makeLabels(nameList, positionArray, font_size=5):
    fig, labels = plt.subplots()

    for j in range(len(positionArray)):
        labels.annotate(nameList[j], positionArray[j], size=font_size, ha='left')


sportsData = 'similarities.csv'
# circleData = 'circle.csv' #to test known shape

importArray = importCSV(sportsData, float)
nameList = getNames(sportsData, float)

psyArray = convertArray(importArray, simToDist)
arraySize = psyArray.shape[0]
dim = 2

posArray = getRandPositions(arraySize, dim)
posArray_mod, minStress = traceGradient(psyArray, learn_rate=.01, n=1000, dimensions=dim)

print("minStress: ", minStress)

x2, y2 = zip(*posArray_mod)
colors1 = np.random.RandomState(0).rand(arraySize)
makeLabels(nameList, posArray_mod, 5)
plt.scatter(x2,y2, c=colors1)
# plt.savefig('sports_n1000.pdf')
# plt.show()
"""End Problem 4"""


"""Problem 5"""





#end
