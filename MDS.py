import numpy as np
import random


def importCSV(csvFile, dataType, header=1):
    return np.genfromtxt(csvFile, dtype=dataType ,delimiter=",", skip_header=1)


def stress(vector):
    """Returns the stress of vector positions"""
    return None

def gradient(vector):
    """Returns the gradient of vector positions"""
    return None



sportArray = importCSV("similarities.csv", float)
print(sportArray)


#end
