import numpy as np
import matplotlib as plt

def RescorlaWagner(associationStr, t, salience=0.5, learnRate=0.1):
    """ Returns the association strength of a stimulant after t time steps
    >>>RescorlaWagner(.2, 10, .5, .1)


    """
    Vs = [associationStr]
    trials = np.arange(1, t + 1)

    for trial in trials:
        associationStr += salience * learnRate * (1 - associationStr)
        Vs.append(associationStr)

    return Vs, trials, associationStr





#end
