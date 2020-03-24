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

class Perceptron(object):

    def __init__(self, weights, dimensions, data, digit0, digit1):
        self.weights = weights
        self.data_set = {0: data[digit0], 1: data[digit1]}
        self.digits = [digit0, digit1]
        self.bias = np.zeros(dimensions)
        self.overall_accuracy = 0

    def dotProd(self, w, x):

        return np.dot(w, x)

    def predict(self, w, x, b):
        dot = self.dotProd(w, x)

        if dot >= 0:
            return 1

        else: return 0

    def random_label(self):
        """Returns a random dataset label"""
        labels = list(self.data_set.keys())
        return random.choice(labels)

    def aniTrain(self):

        label = self.random_label()
        data = self.data_set[label]
        sub_data = random.choice(data)
        y = self.predict(self.weights, sub_data, self.bias)

        if label == 0 and y == 1:
            self.bias -= sub_data
            self.weights -= sub_data - self.bias
        elif label == 1 and y == 0:
            self.bias += sub_data
            self.weights += sub_data + self.bias

        return self.weights.reshape(28, 28)

# np.save('animationWeights.npy', np.random.normal(0, 1, size=784))

def updatefig(*args):
    global im, im2, im3, numIters

    if numIters <= 10:
        numIters += 1
        return im,
    else:
        im.set_array(percept.aniTrain())
        plt.xlabel('Training iterations: ' + str(numIters))
        im.set_array(percept.aniTrain()), im2.set_array(percept2.aniTrain()), im3.set_array(percept3.aniTrain())
        # cbar.update_normal(im)
        cbar.ax.set_xlabel('Weight Range\nBatches: ' + str(numIters), rotation=0, ha='center', fontsize=15)
        numIters += 1

    return im,

trainingImages, unseenImages = loadImages(fileNames, unseen=False)
percept = Perceptron(np.load('animationWeights.npy'), 784, trainingImages, 0, 1)
percept2 = Perceptron(np.load('animationWeights.npy'), 784, trainingImages, 0, 2)
percept3 = Perceptron(np.load('animationWeights.npy'), 784, trainingImages, 0, 3)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='JS'), bitrate=1800)

numIters = 0
fig, axs = plt.subplots(1, 3, figsize=(13, 6))
cmap='inferno_r'
interpol = ir.interpol_methods[2]
# fig, = plt.figure(figsize=(5, 5))
im = axs[0].imshow(np.load('animationWeights.npy').reshape(28, 28), animated=True, interpolation=interpol, cmap=cmap)
im2 = axs[1].imshow(np.load('animationWeights.npy').reshape(28, 28), animated=True, interpolation=interpol, cmap=cmap)
im3 = axs[2].imshow(np.load('animationWeights.npy').reshape(28, 28), animated=True, interpolation=interpol, cmap=cmap)
im.axes.get_xaxis().set_visible(False)
im.axes.get_yaxis().set_visible(False)
im2.axes.get_xaxis().set_visible(False)
im2.axes.get_yaxis().set_visible(False)
im3.axes.get_xaxis().set_visible(False)
im3.axes.get_yaxis().set_visible(False)
axs[0].set_title('Digits 0 and 1', fontsize=15)
axs[1].set_title('Digits 0 and 2', fontsize=15)
axs[2].set_title('Digits 0 and 3', fontsize=15)

cbar = fig.colorbar(im, ax=axs.ravel().tolist(), shrink=0.98, orientation='horizonal', aspect=50)
fig.suptitle('Perceptron Training', fontsize=20, y=.96)
ani = animation.FuncAnimation(fig, updatefig, frames=1000, interval=10, blit=False)
# ani.save('0-3_multi_weight_LOFI.mp4', writer=writer)
plt.show()
