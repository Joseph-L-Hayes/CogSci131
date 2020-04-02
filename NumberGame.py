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
for i in hypos.items():
    print(i)

"""Problem 1:
    Write a function that takes an argument x and a hypothesis (however you represent it)
    and computes a size principle likelihood (e.g. where the likelihood of each number in
    the set is equal). Write down what likelihood each hypothesis assigns to each data
    point in it. What does each hypothesis assign to data points not in it?"""

def likelihood(x, hypothesesDict):
    for h in hypothesesDict.items():
        print('Size principle likelihood for ' + str(h[0]), ' = ', 1 / len(h[1]) )




likelihood(2, hypos)





#end
