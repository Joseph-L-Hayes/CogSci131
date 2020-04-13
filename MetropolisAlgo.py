import numpy as np
from math import log, sqrt
import scipy.stats
import pandas as pd

def log_likelihood(n1, n2, a, W): #P(W|D)
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

def weberPrior(W): #P(W)
    """Returns the prior, P(W), for the Weber ratio: P(W) = e^-W where W is a ratio"""

    return np.exp(-W)

# print(weberPrior(-10))

"""Problem 1:
    We will implement functions that compute the logarithm of the prior and the logarithm
    posterior, as opposed to the unlogged versions. Explain why in 1-2 sentences.

    ANSWER: INCOMPLETE"""
    #see lecture video for 4/9


"""Problem 2:
    Explain in a 1-2 sentences why the form of the acceptance ratio P(W'|D)/P(W|D) is
    convenient for us – that is, why it saves us from doing an integral.

    ANSWER: INCOMPLETE"""


"""Problem 3:
    Write functions to compute something proportional to the log prior and log posterior in
    this model. You will prevent later frustration by ensuring that your prior correctly handles
    cases when W<0 (what should it return?)."""


"""Problem 4:
    Implement the Metropolis algorithm, starting from a random W, and plot:
    (a) the posterior score of W over the first 300 samples;
    (b) the value of W over the first 300 samples, and
    (c) a histogram of the samples of W over the first 10,000 samples after 1000 samples of “burn in.”"""


"""Problem 5:
    Use your sampler to determine the probability that W is in the interval [0.60, 0.65].
    What is that probability?"""


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
