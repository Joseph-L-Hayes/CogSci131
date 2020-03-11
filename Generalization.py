import random
import numpy as np
import matplotlib.pyplot as plt

"""Problem 0, Generate regions between [-10, 10]"""
def generateRegions(numRegions, low, high):
    regions = [sorted((np.random.uniform(low, high), np.random.uniform(low, high))) for n in range(numRegions)]
    return regions

regionList = generateRegions(10000, -10, 10)

"""Problem 1"""
def contains(region, point):
    """Takes a region as a 2 element list or tuple and returns if point is in the region"""
    return (region[0] <= point) and (region[1] >= point)

def size(region):
    return region[1] - region[0]

"""Problem 2:  What is the probability of getting x=1 for regions containing x=0?
    ANSWER: ~0.10613579023117636 """

def conditionalProb(regions, x, y):
    """Takes a list of regions as intervals and returns P(y | x ∈ r)"""

    xRegions = 0
    totalProb = 0
    intervalProb = []

    for r in regions:
        if contains(r, x):
            xRegions += 1

            if contains(r, y):
                intervalProb += [1 / size(r)]

    if intervalProb and xRegions:
        condProb = 1 / xRegions
        intervalProb = [condProb * p for p in intervalProb]
        totalProb = sum(intervalProb)

        return totalProb
    else:
        return 0

# regionList = generateRegions(10000, -10, 10)
# print(conditionalProb(regionList, 0, 1))

"""Problem 3: Plot the probability of getting x for x ranging from 0 to 10, for regions
    containing x=0. What does this function look like? Write a sentence explaining why
    intuitively.

    ANSWER: INCOMPLETE """

def plotProb(z, interval, regions, saveName=None, scale='linear', color='blue'):
    probList = []
    xAxis = []

    for i in range(interval + 1):
        xAxis += [i]
        probList += [conditionalProb(regions, z, i)]

    x, y = xAxis, probList

    plt.plot(x, y, c=color)
    plt.yscale(scale)
    plt.title('P(x | x=' + str(z) + ' ∈ r)')
    plt.xlabel('X Range')
    plt.ylabel('Probability')

    if saveName:
        plt.savefig(saveName + '.pdf')

    # plt.show()

# regionList = generateRegions(10000, -10, 10)
# plotProb(0, 10, regionList, 'a6_p3')
# plotProb(0, 10, regionList, scale='log')

"""Problem 4: One way to check if the curve has an exponential decrease is to plot a
    logarithmic y axis and look for a straight line. Why does this check if the curve
    is exponential?
    ANSWER: ???"""

"""Problem 5: Plot Q3 with a logarithmic y axis for x ranging from -5 to 5, and x
    ranging from -10 to 10. What do these two plots show? How do you interpret them?
    Explain in a few sentences."""
regionTen = generateRegions(10000, -10, 10)
regionFive = generateRegions(10000, -5, 5)
plotProb(0, 10, regionTen, scale='log', color='red')
plotProb(0, 10, regionFive, scale='log')

plt.show()
"""Problem 6: In previous questions, we've been assuming that people implement the law
    perfectly and we have been trying to approximate their behavior using 10,000 regions.
    However, people themselves have limited resources. What if people themselves only used
    a few consequential regions in order to compute generalizations? Re-plot Question 2
    using only 10, 100, and 1000 consequential regions. What patterns do you see?"""

"""Problem 7: Describe a way you could test how many consequential regions people actually
    made use of in this kind of generalization. Could you tell the difference between 10 and
    10,000? Could you tell the difference between 10,000 and 20,000, why or why not?"""






#end
