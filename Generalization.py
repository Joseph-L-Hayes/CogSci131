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
    """Takes a list of regions as intervals and returns P(y ∈ r | x ∈ r)"""

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
        intervalProb = [abs(condProb * p) for p in intervalProb]
        totalProb = sum(intervalProb)

        return totalProb
    else:
        return 0

# regionList = generateRegions(10000, -10, 10)
# print(conditionalProb(regionList, 0, 1))

"""Problem 3: Plot the probability of getting x for x ranging from 0 to 10, for regions
    containing x=0. What does this function look like? Write a sentence explaining why
    intuitively.

    ANSWER: The maximum probability is the chance of choosing x=0 given x=0 ∈ r at about
    0.14 and then the graph decays  """

def plotProb(z, start, end, regions, saveName=None, scale='linear', color='blue', leg=None, legTitle='Enter Title'):
    probList = []
    xAxis = []

    for i in range(start, end + 1):
        xAxis += [i]
        probList += [conditionalProb(regions, z, i)]

    x, y = xAxis, probList

    plt.plot(x, y, c=color, label=leg)
    plt.yscale(scale)
    plt.title('P(x ∈ r | x=' + str(z) + ' ∈ r)')
    plt.xlabel('X Range')
    plt.ylabel('Probability')

    if leg:
        plt.legend(loc=0, title=legTitle)

    if saveName:
        plt.savefig(saveName + '.pdf')

    plt.show()

# region20k = generateRegions(20000, -10, 10)
# plotProb(0, 0, 10, region20k, saveName='a6_p3_20k', legTitle='20000 Regions')

"""Problem 4: One way to check if the curve has an exponential decrease is to plot a
    logarithmic y axis and look for a straight line. Why does this check if the curve
    is exponential?

    ANSWER: Plotting y values on a log scale gives all intervals of y the same 'tick'
    distance. So an interval of 1 to 10 has the same y distance as 10 to 100; log scale
    gives all y values a constant ratio between ticks. Assuming the x and y axis have
    the same tick distances and number of intervals, an exponential decrease should
    appear as a straight line. """
# plotProb(0, 0, 10, regionList, saveName='a6_p4', scale='log')

"""Problem 5: Plot Q3 with a logarithmic y axis for x ranging from -5 to 5, and x
    ranging from -10 to 10. What do these two plots show? How do you interpret them?
    Explain in a few sentences.
    ANSWER...??? """
# regionList = generateRegions(10000, -10, 10)
# plotProb(0, -10, 10, regionList, saveName='a6p5_-10to10', scale='log', color='red', leg='[-10, 10]')
# plotProb(0, -5, 5, regionList, saveName='a6p5_-5to5', scale='log', leg='[-5, 5]')

"""Problem 6: In previous questions, we've been assuming that people implement the law
    perfectly and we have been trying to approximate their behavior using 10,000 regions.
    However, people themselves have limited resources. What if people themselves only used
    a few consequential regions in order to compute generalizations? Re-plot Question 3
    using only 10, 100, and 1000 consequential regions. What patterns do you see?

    ANSWER: The curves are not as smooth going from 10 to 1000 as when there were 10000
    regions and the probabilities from 0 to 10 should all be the same but they aren't; some
    x higher/lower for a given distance from 0.

    With fewer regions to choose from, people are more likely to generalize to a region
    that doesn't fit the subject; they will have less accuracy. We are using a uniform
    distribution meaning that all numbers should be equally as likely in the random sample.
    Generating more regions increases the likelihood that we will see the true probability
    distribution; ie generalize to the correct category.
    """

# region10 = generateRegions(10, -10, 10)
# region100 = generateRegions(100, -10, 10)
# region1000 = generateRegions(1000, -10, 10)
# plotProb(0, 0, 10, region10, color='red', leg='10 Regions', legTitle='Number of Regions')
# plotProb(0, 0, 10, region100, color='green', leg='100 Regions', legTitle='Number of Regions')
# plotProb(0, 0, 10, region1000, saveName='a6p6',color='blue',leg='1000 Regions', legTitle='Number of Regions')
# plt.show()

"""Problem 7: Describe a way you could test how many consequential regions people actually
    made use of in this kind of generalization. Could you tell the difference between 10 and
    10,000? Could you tell the difference between 10,000 and 20,000, why or why not?

    ANSWER: backtrack the math to pull out the 1/regionsWithX=0 probs"""






#end
