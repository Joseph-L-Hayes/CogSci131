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
plt.savefig("assignment2_1a.pdf")
# plt.show()
#end problem 1a

#Problem 1b
def manyTrials(initStr, limit, t=1, salience=0.5, learnRate=0.1):

    if initStr >= limit:
        return t
    else:
        initStr += salience * learnRate * (1 - initStr)
        return manyTrials(initStr, limit, t + 1)

manyTrials(0.05, .8)
"""It will take 32 trials to reach Vlight = 0.8 if the initial association is 0.05"""
#end problem 1b

#Problem 1c uppose that it takes a 13 trials for a buzzer’s association with food to exceed 0.8
# starting from an initial association of 0.0. What is the salience? Show your work/code (it is acceptable
# to solve numerically).

#many trials = 13, assoc = .8, assume learnRate = .1 (?)

#iV(t) += salience * learnRate * (1 - V(t+1))

# .8 = salience * .1 * (1 - V(t+1))

#.8 / (1 - V(t+1)) = salience * .1

#.8 / (.1 - .1V(t+1)) = salience

#SKIP FOR NOW

#Problem 2
def RescorlaWagnerBlock(initStrBlock, initStrTarget=0, t=20, targetSalience=0.5, learnRate=0.1):
    Vs =[]
    trials = np.arange(1, t + 1)
    assocStr = initStrTarget

    for trial in trials:
        # assocStr = round(assocStr, 4)
        Vs.append(assocStr)
        assocStr += targetSalience * learnRate * (1 - (assocStr + initStrBlock))

    return Vs, trials


Vs1, trials = RescorlaWagnerBlock(0.8, 0, 20, 0.2, 0.1) #double check blocking behavior in function

plt.figure()
plt.plot(trials, Vs1, label='Bell', color='red')

plt.xlabel("Trials")
plt.ylabel("Association Strength")
plt.title("Association Strength of a Bell to Food after Light Association")
plt.legend(loc='lower right')
plt.xticks(np.arange(min(trials), max(trials) + 1))

plt.ylim(0, max(Vs1) + (max(Vs1) / 3))
plt.grid()
plt.savefig("assignment2_2.pdf")
plt.show()

#end Problem 2
#end
