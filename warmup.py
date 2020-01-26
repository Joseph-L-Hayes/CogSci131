import numpy as np
import matplotlib.pyplot as plt
import math

#problem 1

def xPowSin(x):
    return np.sin(pow(2,x))


x = np.linspace(-1, 10, 10000)
y = xPowSin(x)

plt.plot(x, y)
plt.ylim(-1.25, 1.25)
plt.show()

#problem 2
x = np.linspace(0, 100, 10000)
g = xPowSin(x) / (xPowSin(x + 0.1))

plt.ylim(-100, 100)
plt.xlim(0, 200)

plt.plot(g, 'red')
plt.show()
#could be smoother? Needs better scaling

#problem 3a
"""returns the harmonic of k"""
def harmonic(k):
    return 1 / (k + 1)

"""returns the harmonic series sum up to n"""
def harmonicSum(n):
    total = 0
    for i in n:
        total = total + harmonic(i)

    return total
#finished

#problem 3b
x = np.linspace(1, 100, 1000)
y = harmonic(x)
plt.plot(x, y)
plt.show()

#finished, check scaling

"""plots a histogram of func with sample type of numSamples"""
def histoPlot(func, sampleType, mean=0, stdev=1, numSamples=None, scale=None):
    x = sampleType(mean, stdev, numSamples)
    print(x)
    if numSamples != None and scale != None:
        plt.hist(func(x), numSamples // scale)
    # else:
    #     plt.hist(func(x), 10000 // 100)
    plt.show()

#problem 4
histoPlot(np.sin, np.random.normal, 0, 1, 10000, 10)
#finished

#problem 5
histoPlot(np.exp, np.random.uniform, 0, 1.5 + .01, 10000, 100)
#check graph shape!

#problem 6






#end
