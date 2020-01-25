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

"""returns the harmonic series some up to n"""
def harmonicSum(n):
    total = 0
    for i in range(1,n+1):
        total = t + 1 / (i + 1)

    return total
