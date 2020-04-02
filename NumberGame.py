import matplotlib.pyplot as plt

def genHypos(min, max):
    hypoDict = dict()

    hypoDict['H1'] = list(range(min + 1, max + 1, 2))
    hypoDict['H2'] = list(range(min, max + 1, 2))
    hypoDict['H3'] = [x**2 for x in range(min, max + 1) if x**2 <= 100] #is this correct or go above 100?
    hypoDict['H4'] = [x for x in range(min + 1, max + 1) if all(x % i != 0 for i in range(min + 1, x))]
    hypoDict['H5'] = [x * 5 for x in range(min, max + 1) if x*5 <= 100] #is this correct or go above 100?
    hypoDict['H6'] = [x * 10 for x in range(min, max + 1) if x*10 <= 100]
    hypoDict['H7'] = list(range(min, max + 1))

    return hypoDict

hypos = genHypos(1, 100)
# for i in hypos.items():
#     print(i)

"""Problem 1:
    Write a function that takes an argument x and a hypothesis (however you represent it)
    and computes a size principle likelihood (e.g. where the likelihood of each number in
    the set is equal). Write down what likelihood each hypothesis assigns to each data
    point in it. What does each hypothesis assign to data points not in it?

    ANSWER: INCOMPLETE
        Likelihoods for data points in each hypothesis:
            P(D | H1) = 0.02
            P(D | H2) = 0.02
            P(D | H3) = 0.1
            P(D | H4) = 0.04
            P(D | H5) = 0.05
            P(D | H6) = 0.1
            P(D | H7) = 0.01
            P(D ∉ Hx) = 0 (for data points not in the hypothesis)
        """

def likelihood(x, hypothesesDict, hypothesis=None): #check for correct interpretation
    """Returns the P(x | Hn) where Hn is a hypothesis from hypothesesDict"""
    # for h in hypothesesDict.items(): #prints P(D | Hx)
    #     print('P(D | ' + str(h[0]) + ') =', 1 / len(h[1]) )
    if hypothesis and x in hypothesesDict[hypothesis]:
        return 1 / len(hypothesesDict[hypothesis])
    else:
        return 0


print(likelihood(3, hypos, 'H4'))


"""Problem 2:
    Make a plot showing the posterior predictive probability (marginalizing over hypotheses)
    that each number 1...100 is “in” the concept, for each of the following data sets:

    (a) No data
    (b) 50
    (c) 53
    (d) 50, 53
    (e) 16
    (f) 10, 20
    (g) 2, 4, 8
    (h) 2, 4, 8, 10

    Assume that there are equal priors on each hypothesis and the size principle likelihood
    from Q1. Be sure that you structure your code to process the data (a)-(h) as a list and
    do not “hard code” in these datasets (i.e. the likelihood function and posterior function
    should accept any list of data). Write a sentence for each plot about whether the model
    does or does not capture your intuitions about the “right” answer.

    ANSWER: INCOMPLETE """
    #what posterior function? we didn't make one... ugh
    #equal priors? So P(H) = 1/7 ?



"""Problem 3:
    Re-make the plots from Q2 but now incorporate range-based hypotheses. To do this, assume
    that H1-H7 each have a prior of 1/8, and the remaining 1/8th probability is distributed
    equally among all intervals in the range 1-100. Here we will define as “interval” as something
    containing two distinct points (e.g. [50-51] or [3-88] but not [31]); there are a lot of
    these range-based hypotheses-- how many are there? Write a sentence for each plot about
    whether the including the range-based hypotheses makes them better match your own intuitions
    about how to generalize and why.

    ANSWER: INCOMPLETE """
#end
