"""Written by Joseph Hayes for UC Berkeley CogSci 131, Spring 2020"""

import numpy as np
import matplotlib.pyplot as plt
import doctest
from decimal import *

def RescorlaWagner(initStr, t, salience=0.5, learnRate=0.1):
    """ Returns the association strength of a stimulant after t time steps
    >>> RescorlaWagner(0.2, 2, .5, .1)
    ([0.2, 0.24], array([1, 2]))

    >>> RescorlaWagner(.5, 10, .5, .1)
    ([0.5, 0.525, 0.5488, 0.5714, 0.5928, 0.6132, 0.6325, 0.6509, 0.6684, 0.685], array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]))

    """
    Vs = []
    trials = np.arange(1, t + 1)
    # trials = list(range(1, t + 1))

    for trial in trials:
        initStr = round(initStr, 4)
        Vs.append(initStr)
        initStr += salience * learnRate * (1 - initStr)

    return Vs, trials

# doctest.testmod()

#Problem 1a
Vs1, trials1 = RescorlaWagner(0.05, 20, 0.5, 0.1)
Vs2, trials2 = RescorlaWagner(0.5, 20, 0.5, 0.1)

plt.figure()
plt.plot(trials1, Vs1, label='initial str 0.05')
plt.plot(trials2, Vs2, label='initial str 0.50')

plt.xlabel("Trials")
plt.ylabel("Association Strength")
plt.title("Association Strength of Light to Food")
plt.legend(loc='lower right')
plt.xticks(np.arange(min(trials1), max(trials1) + 1))

plt.ylim(0, 1)
plt.grid()
plt.savefig("1a.pdf")
# plt.show()

#Problem 1b
def manyTrials(initStr, limit, t=1, salience=0.5, learnRate=0.1):

    if initStr >= limit:
        return t
    else:
        initStr += salience * learnRate * (1 - initStr)
        return manyTrials(initStr, limit, t + 1)

print(manyTrials(0.05, .8))
"""It will take 32 trials to reach Vlight = 0.8 if the initial association is 0.05"""

#end
