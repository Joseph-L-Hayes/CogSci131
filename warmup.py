import numpy as np
import matplotlib.pyplot as plt
import math
#
# #problem 1
#
# def xPowSin(x):
#     return np.sin(pow(2,x))
#
#
# x = np.linspace(-1, 10, 10000)
# y = xPowSin(x)
#
# plt.plot(x, y)
# plt.ylim(-1.25, 1.25)
# plt.show()
#
# #problem 2
# x = np.linspace(0, 100, 10000)
# g = xPowSin(x) / (xPowSin(x + 0.1))
#
# plt.ylim(-100, 100)
# plt.xlim(0, 200)
#
# plt.plot(g, 'red')
# plt.show()
# #could be smoother? Needs better scaling
#
# #problem 3a
# """returns the harmonic of k"""
# def harmonic(k):
#     return 1 / (k + 1)
#
# """returns the harmonic series sum up to n"""
# def harmonicSum(n):
#     total = 0
#     for i in n:
#         total = total + harmonic(i)
#
#     return total
# #finished
#
# #problem 3b
# x = np.linspace(1, 100, 1000)
# y = harmonic(x)
# plt.plot(x, y)
# plt.show()
#
# #finished, check scaling

"""plots a histogram of func with sample type of numSamples"""
def histoPlot(func, sampleType, mean=0, stdev=1, numSamples=None, scale=None):
    x = sampleType(mean, stdev, numSamples)

    if numSamples != None and scale != None:
        plt.hist(func(x), numSamples // scale)

    plt.show()

#problem 4
histoPlot(np.sin, np.random.normal, 0, 1, 10000, 100)
#finished

#problem 5
histoPlot(np.exp, np.random.uniform, 0, 1.5, 10000, 100)
#check graph shape!

#problem 6a
def getDiff(array): #may need to rewrite
    for i in range(len(array) - 1):
        array[i] = abs(array[i + 1] - array[i])

    array = np.delete(array, 999) #

    return array


def adjHistoPlot(n=1000):
    sample = np.random.normal(0, 1, n)
    sample = np.sort(sample)

    diffArray = getDiff(sample)

    plt.hist(diffArray, n)
    plt.title('Differences Between Normally Distributed Samples')
    plt.xlabel('differences between samples after sorting')
    plt.ylabel('frequency')
    plt.xlim(0, .05)
    plt.show()

    return diffArray

diffArr = adjHistoPlot(1000)
#most samples have a difference of less than .01 between them

#problem 6b Plot the position in the sorted array (first, second, etc.) vs the difference computed in 6a.
x = np.arange(999)
plt.plot(x, diffArr, color='red')
plt.title("Differences between indices of sorted array")
plt.xlabel('index')
plt.ylabel('difference: arr[i + 1] - arr[i]')
plt.show()

#end
