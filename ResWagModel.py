"""Written by Joseph Hayes for UC Berkeley CogSci 131, Spring 2020"""

import numpy as np
import matplotlib.pyplot as plt
import doctest
from decimal import *

def RescorlaWagner(associationStr, t, salience=0.5, learnRate=0.1):
    """ Returns the association strength of a stimulant after t time steps
    >>> RescorlaWagner(0.2, 1, .5, .1)
    ([0.2, 0.24], array([1]))

    >>> RescorlaWagner(.5, 10, .5, .1)
    ([0.5, 0.525, 0.5488, 0.5714, 0.5928, 0.6132, 0.6325, 0.6509, 0.6684, 0.685, 0.7008], array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    """
    Vs = [associationStr]
    trials = np.arange(1, t + 1)

    for trial in trials:
        associationStr += salience * learnRate * (1 - associationStr)
        associationStr = round(associationStr, 4)
        Vs.append(associationStr)

    return Vs, trials


#Problem 1a
Vs1, trials = RescorlaWagner(.05, 20, .5, .1)
Vs2 = RescorlaWagner(.5, 20, .5, .1)

# plt.figure()
plt.plot(Vs1, trials)
plt.plot(Vs2, trials)

plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()



#end
