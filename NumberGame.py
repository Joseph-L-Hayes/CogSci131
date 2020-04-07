import matplotlib.pyplot as plt

def genHypos(min, max):
    hypoDict = dict()

    hypoDict['H1'] = list(range(min + 1, max + 1, 2)) #even numbers
    hypoDict['H2'] = list(range(min, max + 1, 2)) #odd numbers
    hypoDict['H3'] = [x**2 for x in range(min, max + 1) if x**2 <= 100] #square numbers
    hypoDict['H4'] = [x for x in range(min + 1, max + 1) if all(x % i != 0 for i in range(min + 1, x))] #prime numbers
    hypoDict['H5'] = [x * 5 for x in range(min, max + 1) if x*5 <= 100] #multiples of 5
    hypoDict['H6'] = [x * 10 for x in range(min, max + 1) if x*10 <= 100] #multiples of 10
    hypoDict['H7'] = list(range(min, max + 1)) #all numbers

    return hypoDict

HYPOTHESIS_DICT = genHypos(1, 100)
# for i in hypos.items():
#     print(i)

"""Problem 1:
    Write a function that takes an argument x and a hypothesis (however you represent it)
    and computes a size principle likelihood (e.g. where the likelihood of each number in
    the set is equal). Write down what likelihood each hypothesis assigns to each data
    point in it. What does each hypothesis assign to data points not in it?

    ANSWER: INCOMPLETE
        Likelihoods for data points in each hypothesis:
            P(D ∈ H1 | H1) = 0.02 = 1/50
            P(D ∈ H2 | H2) = 0.02 = 1/50
            P(D ∈ H3 | H3) = 0.1 = 1/10
            P(D ∈ H4 | H4) = 0.04 = 1/25
            P(D ∈ H5 | H5) = 0.05 = 1/20
            P(D ∈ H6 | H6) = 0.1 = 1/10
            P(D ∈ H7 | H7) = 0.01 = 1/100
            P(D ∉ Hn | Hn) = 0 (for data points not in the hypothesis)
        """

def likelihood(dataSet, hypothesis): #check for correct interpretation
    """Returns the P(dataSet | Hx) where Hx is a hypothesis"""
    # for h in hypothesesDict.items(): #prints P(D | Hx)
    #     print('P(D | ' + str(h[0]) + ') =', 1 / len(h[1]) )
    total = 1
    if dataSet:
        for d in dataSet:
            if d in HYPOTHESIS_DICT[hypothesis]: #problem here!
                total *= 1 / len(HYPOTHESIS_DICT[hypothesis]) #total should go back to 0 if there is a d NOT in the hypo
            else:
                total = 0
        if total == 1:
            return 0
        else:
            return total
    else:
        return 1.0 #from piazza: the size principle likelihood of no data is 1.0


# print(likelihood([90, 80], 'H6'))


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

def bayesRule(dataList):
    """Returns a dictionary of hypotheses as keys and P(h|dataList) as values """
    prior_prob = 1 / len(HYPOTHESIS_DICT) #P(h)
    hypo_given_data = dict()
    norm = 0

    for key in HYPOTHESIS_DICT:
        hypo_given_data[key] = likelihood(dataList, key) * prior_prob
        norm += hypo_given_data[key]

    for key in hypo_given_data:
        hypo_given_data[key] /= norm
    print('probs:', hypo_given_data)

    return hypo_given_data

# print(bayesRule([80, 90]))
# a = bayesRule([80, 90])
# print('sum:', sum([a[key] for key in a]))

def pos_pred_prob(dataList, start, finish):

    hypo_given_data = bayesRule(dataList)
    xList = list(range(start, finish + 1))
    prob_list = []

    for x in xList:
        total = 0
        for key in HYPOTHESIS_DICT: #sum over hypos
            if x in HYPOTHESIS_DICT[key]:
                total += hypo_given_data[key] * 1

        prob_list += [total]

    return xList, prob_list

xAxis, yAxis = pos_pred_prob([], 1, 100)

plt.bar(xAxis, yAxis)
plt.show()


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
