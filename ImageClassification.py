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
assert N == DIM[0]*DIM[1] # just check our sizes to be sure

# set up some random initial weights
# weights = np.random.normal(0,1,size=N) #shape (784,)

## Your code here:
"""Problem 1: Write an implementation of the perceptron learning algorithm that first
    loads images for the digit “0” and then for the digit “1”. Start with random weights
    from a normal distribution. Compute the average accuracy on blocks of 25 items and plot
    this accuracy until you think it won’t get better."""

class Perceptron(object):

    def __init__(self, dimensions, image0, image1):
        self.weights = np.random.normal(0, 1, size=dimensions)
        self.data_set = self.buildData(image0, image1)
        self.accuracy_trace = []

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

    def random_label(self):
        """Returns a random dataset label"""
        labels = list(self.data_set.keys())
        #seems to be working, needs testing
        return random.choice(labels)

    def train(self, threshold, runs):
        """Data_set is a dictionary of lists containing (784,) arrays"""
        accuracy = 0

        while accuracy < threshold: #change accuracy to error or diff in accuracy
            correct = 0

            for i in range(runs):
                label = self.random_label()
                data = self.data_set[label] #image set 0 or 1
                sub_data = random.choice(data) #a (784,) array from image set 0 or 1
                y = self.predict(self.weights, sub_data)

                if label == 0 and y == 1:
                    self.weights -= sub_data
                elif label == 1 and y == 0:
                    self.weights += sub_data
                else:
                    correct += 1
                #next step is to graph the accuracy of the changes?
            accuracy = correct / runs
            self.accuracy_trace.append(accuracy)
        print(self.accuracy_trace)

zeroPercept = Perceptron(N, A, B)
zeroPercept.train(1, 25)


"""Problem 2: """


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
