import os
import numpy as np
import random

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
# A = load_image_files(0)
# B = load_image_files(1)

A = np.load('Zero.npy') #each element in the list is a flattened array with shape (784,), is it all the text for number 0?
B = np.load('One.npy') #also (784,)

N = len(A[0]) # the total size
# assert N == DIM[0]*DIM[1] # just check our sizes to be sure

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


class Perceptron(object):

    def __init__(self, dimensions, image0, image1):
        self.weights = np.random.normal(0,1,size=dimensions)
        self.data_set = self.buildData(image0, image1)

    def buildData(self, *args):
        """Takes in a list of data sets and returns a dictionary with keys as labels for the data sets.
            The key labels are generated based on index in args, so they must be input in the correct order.
            For example: data set for 0 images must be first arg in args, 1 images must be next"""
        data = dict()
        for k in range(len(args)):
            # print(k)
            data[k] = args[k]
        return data

    def get_weights(self): #may not be necessary
        return self.weights

    def dotProd(self, w, x):

        return np.dot(w, x) #changed to indexed weights w[i]

    def predict(self, w, x):
        dot = self.dotProd(w, x) #change to w[i]

        if dot >= 0:
            return 1

        else: return 0

    def accuracy(self):
        return None

    def update(self, x): #this should take intended label and a data label along with prediction
        self.weights += x #need to change to weights[i], passed in
        #logic for how to update weights here

    def get_label(self):
        """Returns a random dataset label"""
        labels = list(self.data_set.keys())
        #seems to be working, needs testing
        return random.choice(labels)

    def train(self, threshold):
        """Data_set is a dictionary of lists containing (784,) arrays"""
        runs = 25
        accuracy = 0

        while accuracy < threshold:
            trained = True
            correct = 0

            for i in range(runs): #25 is the number of images being tested
                runs += 1
                label = self.get_label()
                data = self.data_set[label]
                sub_data = random.choice(data)
                #they "simplify" things by assigning a digit to 0 or 1. So 1 and 1 is correct, w+=x, 0 and 1 is incorrect, w-=x
                #if there is no change, then count toward accuracy
                y = self.predict(self.weights, sub_data)

                if label == 0 and y == 1:
                    self.weights -= sub_data
                    trained = False
                elif label == 1 and y == 0:
                    self.weights += sub_data
                    trained = False
                else:
                    correct += 1
                #the above doesn't error out... now to see what's going on inside; weights definitely getting changed

                #next step is to graph the accuracy of the changes?
            accuracy = correct / runs
            print("accuracy? ", accuracy)


zeroPercept = Perceptron(N, A, B)
zeroPercept.train(.5)








#end
#scrap:
            # label = self.get_label()
            # data = self.data_set[label] #this should give data for 0 or 1, then random into that
            #if the data is label 1 and we get 0 as output, that means it was incorrect
            #if data is label 0 and we get 1 as output, weights incorrect
            # sub_data = random.choice(data) #this should be one of the (784,) arrays
            # print("intended :", intended)
            # print("label: ", label)
            # print("sub_data: ", sub_data.shape)
