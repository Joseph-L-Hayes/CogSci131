import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import image_resources as ir

def loadImages(files, show=False, unseen=False):
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

    return trainingDict, unseenDict

fileNames = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

trainingImages, unseenImages = loadImages(fileNames, unseen=False)


class Perceptron(object):

    def __init__(self, weights, dimensions, data, digit0, digit1):
        self.weights = weights
        self.data_set = {0: data[digit0], 1: data[digit1]}
        self.digits = [digit0, digit1]
        self.bias = np.zeros(dimensions)
        self.overall_accuracy = 0

    def get_weights(self):
        #changed this to a copy when live plotting; may cause issues with other functions already written
        return self.weights

    def dotProd(self, w, x):

        return np.dot(w, x)

    def predict(self, w, x, b):
        dot = self.dotProd(w, x)

        if dot >= 0:
            return 1

        else: return 0

    def classify(self, w, x):
        dot = self.dotProd(w, x)

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

    def aniTrain(self):

        label = self.random_label()
        data = self.data_set[label]
        sub_data = random.choice(data)
        y = self.predict(self.weights, sub_data, self.bias)
        oldData = np.copy(self.weights)

        if label == 0 and y == 1:
            self.bias -= sub_data
            self.weights -= sub_data - self.bias
        elif label == 1 and y == 0:
            self.bias += sub_data
            self.weights += sub_data + self.bias

        if np.sum(oldData == self.weights) == 0:
            return

        return self.weights.reshape(28, 28)

# np.save('animationWeights.npy', np.random.normal(0, 1, size=784))
digit0, digit1 = 1, 0
trainingImages, unseenImages = loadImages(fileNames, unseen=False)
percept = Perceptron(np.load('animationWeights.npy'), 784, trainingImages, digit0, digit1)


def updatefig(*args):
    global im, numIters, digit0, digit1

    im.set_array(percept.aniTrain())
    numIters += 1
    plt.xlabel('Training iterations: ' + str(numIters))

    return im,
numIters = 0
fig = plt.figure(figsize=(5, 5))
im = plt.imshow(percept.aniTrain(), animated=True, interpolation=ir.interpol_methods[9], cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')])) #, cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')])
# im.axes.get_xaxis().set_visible(False)
im.axes.get_yaxis().set_visible(False)
#put aniTrain as function in imshow, first arg
# fig.colorbar(im, orientation='horizontal', fraction=.0415)
plt.title('Perceptron Training Digits ' + str(digit0) + ' and ' + str(digit1), fontsize=10)
ani = animation.FuncAnimation(fig, updatefig, frames=1000, interval=10, blit=False)
plt.show()
