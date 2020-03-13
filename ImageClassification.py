import os
import numpy as np

# Functions that might be useful (please read the documentation)
# x.flatten() (take a N-dimensional numpy array and make it one-dimensional)
# numpy.random.choice -- choose from the list of images
# numpy.dot -- compute the dot product
# numpy.random.normal -- set up random initial weights

DIM = (28,28) #these are the dimensions of the image

def load_image_files(n, path="images/"):
    # helper file to help load the images
    # returns a list of numpy vectors
    images = []
    for f in os.listdir(os.path.join(path,str(n))): # read files in the path
        p = os.path.join(path,str(n),f)
        if os.path.isfile(p):
            i = np.loadtxt(p)
            assert i.shape == DIM # just check the dimensions here
            # i is loaded as a matrix, but we are going to flatten it into a single vector
            images.append(i.flatten())
    return images


# Load up these image files
#a list of numpy vectors
A = load_image_files(0) #each element in the list is a flattened array with shape (784,), is it all the text for number 0?
B = load_image_files(1) #also (784,)

N = len(A[0]) # the total size
assert N == DIM[0]*DIM[1] # just check our sizes to be sure

# set up some random initial weights
weights = np.random.normal(0,1,size=N) #shape (784,)

## Your code here:
"""Problem 1: Write an implementation of the perceptron learning algorithm that first
    loads images for the digit “0” and then for the digit “1”. Start with random weights
    from a normal distribution. Compute the average accuracy on blocks of 25 items and plot
    this accuracy until you think it won’t get better."""

def perceptron(data_set, weights, trials): #seems like updating the weights to improve accuracy only
    #I'm guessing we process 25 blocks at a time and for '0' we should get some
    #level of accuracy as num1/25 or the positive over total because we know this
    #data is from a 0 training set.
    products = list(range(trials))
    weightsN = np.random.normal(0,1,size=len(data_set[0]))

    # for i in range(trials): #start by computing current classification
    #     products += [prediction(np.dot(weights, data_set[i]))]
        # print(products[i])

        #where does sum come in???
        #turn this into a while loop and put update inside until convergence?

    while get_accuracy(products, 1) < .90:

        for i in range(trials):
            pred = prediction(np.dot(weightsN, data_set[i]))
            products[i] = [pred] #just for accuracy right now, may need to change
            # print(pred)
            # if pred != 1: #for right now we are only training on one number so want all 1?
            update_weights(data_set[i], weightsN, pred) #returns nothing duh
        print(get_accuracy(products, 1)) #SOMETHING WRONG HERE



    total = sum(products)

    return total, weights

def get_accuracy(lst, y):

    return lst.count(y) / len(lst)

def prediction(x):

    if x >= 0:
        return 1
    else:
        return 0

def update_weights(x, weights, prediction):

    if prediction:
        weights += x
    else:
        weights -= x

# numTrials = 25
#
# totals, weights = perceptron(A, weights, numTrials)


class Perceptron(Object):

    def __init__(self, dimensions):
        self.weights = np.random.normal(0,1,size=dimensions)

    def get_weights(self):
        return self.weights

    def dotProd(self, x):

        return np.dot(self.weights, x)

    def predict(self, x):
        dot = self.dotProd(x)

        if dot >= 0:
            return 1
        else: return 0

    def accuracy(self):
        return None

    def update(self, x):
        return None

    def train(self, threshold):
        return None













#end
