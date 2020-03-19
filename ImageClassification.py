import os
import numpy as np
import random
import matplotlib.pyplot as plt
import image_resources as ir
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

## Your code here:
def saveImages(files, show=False):
    """Saves digit image matrices for faster access during training"""

    for j in range(len(files)):
        np.save(files[j], load_image_files(j))
        if show:
            print(files[j] + '.npy saved')

def loadImages(files, show=False, unseen=False): #if unseen, save 1000 into another dict and return separately
    """Returns a dictionary of image files with digits as keys"""
    trainingDict = dict()
    unseenDict = dict()

    for f in range(len(files)):
        trainingDict[f] = np.load(files[f] + '.npy')
        if show:
            print(files[f] + '.npy loaded')

    if unseen:
        print('Creating a dictionary of test images, 500 for each digit...')
        for x in range(len(trainingDict)):
            unseenDict[x] = np.empty((500, 784))

            for i in range(500):
                randomIndex = random.randint(0, len(trainingDict[x]) - 1)
                unseenDict[x][i] = trainingDict[x][randomIndex]
                trainingDict[x] = np.delete(trainingDict[x], randomIndex, 0)
            print('...')
    print('Test dictionary complete')


    return trainingDict, unseenDict

fileNames = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

trainingImages, unseenImages = loadImages(fileNames, unseen=True)
N = len(trainingImages[0][0])
assert N == DIM[0]*DIM[1] # just check our sizes to be sure

"""Problem 1: Write an implementation of the perceptron learning algorithm that first
    loads images for the digit “0” and then for the digit “1”. Start with random weights
    from a normal distribution. Compute the average accuracy on blocks of 25 items and plot
    this accuracy until you think it won’t get better.

    ANSWER: The answer to how many images it takes to train my model varies depending
        on the random weights I start with but it usually takes around 400 blocks to
        achieve achieve .99 accuracy. This is about 10,000 images between the 0 and 1
        training sets. I attempted to get .9999 accuracy but it takes 10x longer
        and doesn't seem to produce significantly better results. """

class Perceptron(object):

    def __init__(self, dimensions, data, digit0, digit1):
        self.weights = np.random.normal(0, 1, size=dimensions)
        self.data_set = {0: data[digit0], 1: data[digit1]}
        self.digits = [digit0, digit1]
        self.bias = np.zeros(dimensions)
        self.overall_accuracy = 0

    def get_weights(self):
        return self.weights

    def dotProd(self, w, x):

        return np.dot(w, x)

    def predict(self, w, x):
        dot = self.dotProd(w, x) #added self.bias, needs testing

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

    def train(self, threshold, precision, blocks, plot=False):
        """Data_set is a dictionary of lists containing (784,) arrays"""
        accuracy = .5
        all_blocks = blocks
        correct = 0
        accuracy_trace = []
        xAxis = []
        acc_delta = 1
        getcontext().prec = precision

        # while accuracy <= threshold or acc_delta > 0:
        while (all_blocks // 25) <= 500: #400 blocks from problem 1 convergence

            xAxis += [all_blocks // 25]
            acc_delta = accuracy

            for i in range(blocks):
                label = self.random_label()
                data = self.data_set[label] #image set 0 or 1
                sub_data = random.choice(data) #a (784,) array from image set 0 or 1
                y = self.predict(self.weights, sub_data)

                if label == 0 and y == 1:
                    self.bias -= sub_data
                    self.weights -= sub_data - self.bias
                elif label == 1 and y == 0:
                    self.bias += sub_data
                    self.weights += sub_data + self.bias
                else:
                    correct += 1

            accuracy = correct / all_blocks
            acc_delta = abs(round(Decimal(accuracy), precision) - round(Decimal(acc_delta), precision))
            all_blocks += blocks
            accuracy_trace.append(accuracy)

        self.overall_accuracy = accuracy

        if plot:
            self.plot_accuracy(xAxis, accuracy_trace)

# zeroOnePercept = Perceptron(N, trainingImages, 4, 9)
# beforeWeight = np.copy(zeroOnePercept.get_weights())
# zeroOnePercept.train(.97, 5, 25, plot=True)
# print(zeroOnePercept.overall_accuracy) #will give the last accuracy number aka overall_accuracy
# zeroOneWeight = np.copy(zeroOnePercept.get_weights())
#
# np.save('pre_zero_one', beforeWeight)
# np.save('zero_one', zeroOneWeight)

"""Problem 2: Does your solution in Q1 converge on 100% accuracy or not? What does this
    mean in terms of the linear separability of “0” and “1” on this feature space?

    ANSWER: INCOMPLETE"""

"""Problem 3: """
def weightMatrix(weights, dims, save=False, fileName='TITLE',method=None, bounds=[0, 1]):
    # weights= weights[10]
    weights = weights.reshape(dims, dims)
    fig, im = plt.subplots(figsize=(10, 10))
    wm = plt.imshow(weights, interpolation=ir.interpol_methods[method], cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')]), vmin=bounds[0], vmax=bounds[1])

    wm.axes.get_xaxis().set_visible(False)
    wm.axes.get_yaxis().set_visible(False)
    plt.title('Heat Map of Trained Weight Matrix For Digits 0 and 1', fontsize=15)
    fig.colorbar(wm, orientation='horizontal', fraction=.0415)
    if save:
        plt.savefig(fileName + '.pdf')

    plt.show()

# boundList = [-1, 1]
# weightMatrix(np.load('zero_one.npy'), 28, method=4, bounds=boundList)

"""Problem 4: """
#for training on digits I haven't seen for 4 and 5, maybe store the indices
#seen during training, then skipping those for this question?
#may have to rewrite code instead of using random choice

"""Problem 5: Next show a matrix of the classification accuracy of each pair of digits
    after enough training. Make this a plot (with colors for accuracy rather than numbers).
    Does it match your intuitions about which pairs should be easy vs. hard? Why or why not?

    Essentially, repeat question 1 for training weights. Then train on an unseen
    data set for each pair, make matrix of accuracy on unseen data"""

def allDigitsAcc(trainDict, unseenDict, N):
    digitArray = np.zeros(100)
    digitArray = digitArray.reshape(10, 10)
    xlabels = np.arange(0, 10)
    ylabels = np.arange(0, 10)

    for k in range(len(trainDict.items())):
        for j in range(len(trainDict.items())):
            correct = 0
            percept = Perceptron(N, trainDict, k, j)
            percept.train(.97, 5, 25)
            # digitArray[k, j] = percept.overall_accuracy #training accuracy
            #just call percept.predict(w, x)
            for i in range(1000):
                index = np.random.choice([k, j])#need to pick k or j randomly i.e. k=0, j=1, test the result
                # print(index)

                result = percept.predict(percept.get_weights(), unseenDict[index][i % 500])
                # print(result)
                if index == k and result == 0:
                    correct += 1

                elif index == j and result == 1:
                    correct += 1

            digitArray[k, j] = correct / 1000
            print(digitArray[k, j])


    return digitArray, xlabels, ylabels


grid, xAx, yAx = allDigitsAcc(trainingImages, unseenImages, N)
# np.save('accMatrix', grid)
# np.save('accMatrix_X', xAx)
# np.save('accMatrix_Y', yAx)

# grid = np.load('accMatrix.npy')
# xAx = np.load('accMatrix_X.npy')
# yAx = np.load('accMatrix_Y.npy')

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

fig, ax = plt.subplots() #figsize=(10,10)
matrix = plt.imshow(grid, cmap='coolwarm', extent=[0, 9, 9, 0])
fig.colorbar(matrix, orientation='horizontal', fraction=.05) #, ticks=[.50, .60, .70, .80, .90, 1]
ax.set_xticks(xAx)
ax.set_yticks(yAx)

# plt.savefig('a7p5accuracy.pdf')

plt.show()


#end
