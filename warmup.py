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
#
# """plots a histogram of func with sample type of numSamples"""
# def histoPlot(func, sampleType, mean=0, stdev=1, numSamples=None, scale=None):
#     x = sampleType(mean, stdev, numSamples)
#
#     if numSamples != None and scale != None:
#         plt.hist(func(x), numSamples // scale)
#
#     plt.show()
#
# #problem 4
# histoPlot(np.sin, np.random.normal, 0, 1, 10000, 10)
# #finished
#
# #problem 5
# histoPlot(np.exp, np.random.uniform, 0, 1.5 + .01, 10000, 100)
# #check graph shape!

#problem 6a
def getDiff(array): #may need to rewrite
    for i in range(len(array) - 1):
        array[i] = abs(array[i + 1] - array[i])

    array = np.delete(array, 999) #

    return array


def adjHistoPlot(n=1000):
    sample = np.random.normal(0, 1, n)
    sample1 = np.sort(sample)
    sample2 = np.ndarray.copy(sample1)

    bins = n

    diffArray = getDiff(sample1)

    plt.hist(diffArray, bins)
    plt.title('getDiff')
    plt.xlabel('n')
    plt.ylabel('y')
    plt.xlim(0, .05)
    test = np.diff(sample2)
    print('np.diff: ', test)
    print('myDiff: ', diffArray)
    plt.show()

    plt.hist(test, bins, color='red') #testing only
    plt.title('np.diff')
    plt.xlim(0, .05)
    plt.show()

adjHistoPlot(1000)




# def getBins(array):
#     n = len(array)
#     # print(n)
#     intRange = np.amax(array) - np.amin(array)
#     ints = np.sqrt(n)
#     # print(ints)
#     # print(intRange/ints)
#     bins = np.arange(np.amin(array), np.amax(array), intRange / ints).tolist()
#     print(bins)
#     print(len(bins))
#
#     return bins

# def is_sorted(a):
#     for i in range(a.size-1):
#          if a[i+1] < a[i] :
#                return False
#     return True

#readjust all histoplots using
    # n = number of observations = 100
    # Range = maximum value – minimum value = 91 – 1 = 90
    # # of intervals =  √n = √100 = 10
    # Width of intervals =  Range / (# of intervals) = 90/10 = 9



#end
