import numpy as np
import matplotlib as plt
import doctest
from decimal import *

def RescorlaWagner(associationStr, t, salience=0.5, learnRate=0.1):
    """ Returns the association strength of a stimulant after t time steps
    >>> RescorlaWagner(0.2, 1, .5, .1)
    ([0.2, 0.24], array([1]), 0.24)

    >>> RescorlaWagner(.5, 10, .5, .1)
    ([.5, ], array([1]), last)

    """
    Vs = [associationStr]
    trials = np.arange(1, t + 1)

    for trial in trials:
        associationStr += salience * learnRate * (1 - associationStr)
        associationStr = round(associationStr, 2)
        Vs.append(associationStr)

    return Vs, trials, associationStr


doctest.testmod()


#end
