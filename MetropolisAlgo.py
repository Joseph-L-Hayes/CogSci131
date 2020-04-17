import numpy as np
from math import log, sqrt
import scipy.stats
import pandas as pd
import random
import matplotlib.pyplot as plt

def log_likelihood(n1, n2, a, W): #P(D|W)
    # this function takes a numpy array for n1, n2, and the accuracy (0/1), whether they answered correctly
    # as well as W (the hypothesis)
    # and returns the *log* likelihood of the responses, log P(accuracy | n1, n2, W)

    assert(len(n1) == len(n2) == len(a))

    p = 1.0-scipy.stats.norm.cdf(0, loc=np.abs(n1-n2), scale=W*np.sqrt(n1**2 + n2**2)) # the probability of answering correctly
    return np.sum(np.where(a, np.log(p), np.log(1.0-p)))

df = pd.read_csv('Assignment9-data.csv')
n1 = df['n1'].values #behavioral stimuli
n2 = df['n2'].values #behavioral stimuli
a = df['correct'].values

"""Problem 1:
    We will implement functions that compute the logarithm of the prior and the logarithm
    posterior, as opposed to the unlogged versions. Explain why in 1-2 sentences.

    ANSWER: INCOMPLETE"""
    #see lecture video for 4/9 PROPORTIONALITY?


"""Problem 2:
    Explain in a 1-2 sentences why the form of the acceptance ratio P(W'|D)/P(W|D) is
    convenient for us – that is, why it saves us from doing an integral.

    ANSWER: INCOMPLETE"""

"""Problem 3:
    Write functions to compute something proportional to the log prior and log posterior in
    this model. You will prevent later frustration by ensuring that your prior correctly handles
    cases when W<0 (what should it return?).

    ANSWER: I'm not entirely sure what the thought process is behind what should be returned
            when W < 0. I used 1 in order to make the prior have no effect on the Posterior
            This doesn't seem to be an issue though as np.exp(-W) won't ever be negative causing
            an error in np.log.
    """

def logPrior(W):
    if W < 0:
        return 1

    return np.log(np.exp(-W))

def logPosterior(n1, n2, a, W):
    """Returns P(W|D)"""
    # print(logPrior(W) + log_likelihood(n1, n2, a, W))
    return logPrior(W) + log_likelihood(n1, n2, a, W)

"""Problem 4:
    Implement the Metropolis algorithm, starting from a random W, and plot:

    (a) the posterior score of W over the first 300 samples;
    (b) the value of W over the first 300 samples, and
    (c) a histogram of the samples of W over the first 10,000 samples after 1000 samples of “burn in.”"""

def metropolis(n, burnIn=False): #needs testing

    W = random.uniform(0, 1)
    primeW, next, ratio = 0, 0, 0
    abAxis = list(range(1, n + 1))
    wVals = [] #start with W?
    posVals = []
    intervalProb = 0
    modifier = 0

    if burnIn:
        abAxis = list(range(1, n - 1000 + 1))
        modifier = 1000

        for i in range(1000):
            primeW = W + random.gauss(0, 0.1)
            pW = logPosterior(n1, n2, a, W)
            pPrime = logPosterior(n1, n2, a, primeW)
            ratio = np.exp(pPrime - pW)

            if pW < pPrime:
                W = primeW
            else:
                if random.random() <= ratio:
                    W = primeW

    for i in range(n - modifier):
        primeW = W + random.gauss(0, 0.1)
        pW = logPosterior(n1, n2, a, W)
        pPrime = logPosterior(n1, n2, a, primeW)
        # print(pW, pPrime)
        # ratio = pPrime / pW
        ratio = np.exp(pPrime - pW)

        if pW < pPrime:
            W = primeW
            posVals += [pPrime]
        else:
            if random.random() <= ratio:
                W = primeW
                posVals += [pPrime]
            else:
                posVals += [pW]
        # posVals += [pW] #check location
        wVals += [W] #check location

        if W >= .60 and W <= .65:
            intervalProb += 1

    # print(intervalProb / n)

    return abAxis, wVals, posVals

xAxis, wData, posteriorData = metropolis(10000, burnIn =True)
# xAxis, wData, posteriorData = metropolis(300)
# plt.hist(wData, 100, color='green')
# plt.title(" Samples of W after 1000 sample 'burn in' ")
# plt.xlabel('Bins')
# plt.ylabel('Number of Samples')
# plt.savefig('a9_p4c.pdf')

# plt.plot(xAxis, wData)
# plt.plot(xAxis[1:], wData[1:], color='blue')
# plt.title('Value of W')
# plt.ylabel('Value')
# plt.xlabel('Samples')
# plt.savefig('a9_p4b.pdf')
# plt.show()
#for histogram
# alldata = [priordata, posteriordata]
# plt.hist(alldata, number of bins)
# plt.show()


"""Problem 5:
    Use your sampler to determine the probability that W is in the interval [0.60, 0.65].
    What is that probability?

    ANSWER:
        ~ 0.66 """


"""Problem 6:
    Run your sampler on the prior (assuming no data) and plot histograms of the prior samples
    and the posterior samples (from Q4c) in the same graph. What relationship between these
    distributions does your plot show, and what does it mean?"""


"""Problem 7 (Extra Credit):
    Do you get “better” estimates with this algorithm if you run one chain for 1000 steps or
    100 chains for 10 steps each and just concatenate their samples? To answer this, you should
    come up with both:
    (a) a simulation that tries both of these options (you'll want to run more than one time!)
    and
    (b) a measure of how “good” a run was (i.e. how accurate its samples were).
    Write a sentence or two justifying your measure of goodness, create a visualization of the
    two options, and explain in a sentence how the visualization answers the question."""
#end
