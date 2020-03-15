import os
import numpy as np
import random
import matplotlib.pyplot as plt
from decimal import *

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


# N = len(A[0]) # the total size
# assert N == DIM[0]*DIM[1] # just check our sizes to be sure

## Your code here:
def saveImages(files, show=False):
    for j in range(len(files)):
        np.save(files[j], load_image_files(j))
        if show:
            print(files[j] + '.npy saved')

def uploadImages(files, show=False):
    """Returns a dictionary of image files """
    imageDict = dict()

    for f in range(len(files)):
        imageDict[f] = np.load(files[f] + '.npy')
        if show:
            print(files[f] + '.npy loaded')
    return imageDict

fileNames = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
images = uploadImages(fileNames)
N = len(images[0][0])
assert N == DIM[0]*DIM[1] # just check our sizes to be sure

"""Problem 1: Write an implementation of the perceptron learning algorithm that first
    loads images for the digit “0” and then for the digit “1”. Start with random weights
    from a normal distribution. Compute the average accuracy on blocks of 25 items and plot
    this accuracy until you think it won’t get better."""

class Perceptron(object):

    def __init__(self, dimensions, data, digit0, digit1):
        self.weights = np.random.normal(0, 1, size=dimensions)
        self.data_set = {0: data[digit0], 1: data[digit1]}
        self.digits = [digit0, digit1]

    # def buildData(self, *args):
    #     """Takes in a list of data sets and returns a dictionary with keys as labels for the data sets.
    #         The key labels are generated based on index in args, so they must be input in the correct order.
    #         For example: data set for 0 images must be first arg in args, 1 images must be next"""
    #     data = dict()
    #     for k in range(len(args)):
    #         data[k] = args[k]
    #     return data

    def get_weights(self):
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
        return random.choice(labels)

    def plot_accuracy(self, x, y, save=False, name=None, color='red'):

        plt.xlabel('Blocks of 25')
        plt.ylabel('Accuracy')
        plt.title('P1: Training Accuracy for Digits {0} and {1}'.format(self.digits[0], self.digits[1]))
        plt.legend(loc=0, title='Converged to {0} Accuracy in {1} Blocks'.format(round(y[-1], 5), x[-1]))
        plt.plot(x, y, c=color, label='')

        if save:
            plt.savefig(name + '.pdf')

        plt.show()
        plt.close()

    def train(self, threshold, precision, blocks):
        """Data_set is a dictionary of lists containing (784,) arrays"""
        accuracy = .5
        all_blocks = blocks
        correct = 0
        accuracy_trace = []
        xAxis = []
        acc_delta = 1
        getcontext().prec = precision

        while accuracy < threshold or acc_delta:
        #From Piazza: Train your perceptron algorithm on ALL images in your dataset
            xAxis += [all_blocks // 25]
            acc_delta = accuracy

            for i in range(blocks):
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

            accuracy = correct / all_blocks
            # print("Accuracy: ", accuracy)
            # print("Total Blocks: ", all_blocks)

            acc_delta = abs(round(Decimal(accuracy), precision) - round(Decimal(acc_delta), precision))
            # acc_delta = abs(round(accuracy, precision) - round(acc_delta, precision))
            all_blocks += blocks
            accuracy_trace.append(accuracy)

        print("Final Accuracy: ", accuracy, acc_delta)
        self.plot_accuracy(xAxis, accuracy_trace)


zeroOnePercept = Perceptron(N, images, 0, 1)
zeroOnePercept.train(.9998, 5, 25)

# oneTwoPercept = Perceptron(N, images, 1, 2)
# oneTwoPercept.train(.9998, 5, 25)

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
