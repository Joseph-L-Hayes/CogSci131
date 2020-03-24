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
    global images, numIters, perceptron_list, fig, weights, axis

    if numIters <= 20:
        numIters += 1
    else:
        plt.xlabel('Training iterations: ' + str(numIters))
        numIters += 1
        for index in range(len(images)):
            images[index].set_array(perceptron_list[index].aniTrain())
            percent_change = int(np.sum(perceptron_list[index].weights != weights) / weights.size * 100)
            axis[index].set_ylabel('Weight Change: ' + str(percent_change) + '%')
        cbar.update_normal(images[5])
        cbar.ax.set_xlabel('Weight Range\nBatches: ' + str(numIters), rotation=0, ha='center', fontsize=15)

    return images,

trainingImages, unseenImages = loadImages(fileNames, unseen=False)
weights = np.load('animationWeights.npy')
perceptron_list = [Perceptron(np.copy(weights), 784, trainingImages, 0, i) for i in range(1, 10)]
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='JS'), bitrate=1800)

numIters = 0
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

cmap='inferno_r'
interpol = ir.interpol_methods[15] #13 looks good for upscaled

row, col = 3, 3
axis, images = [], []
for i in range(row):
    for j in range(col):
        images += [axs[i,j].imshow(np.copy(weights).reshape(28, 28), animated=True, interpolation=interpol, cmap=cmap)]
        axis += [axs[i,j]]
        axs[i,j].set_xticks([])
        axs[i,j].set_yticks([])
        axs[i,j].axes.get_xaxis().set_visible(False)
        axs[i,j].set_title('Digits ' + str(0) + ' and ' + str((i * row) + j + 1), fontsize=10)

cbar = fig.colorbar(images[0], ax=axs.ravel().tolist(), shrink=0.50, orientation='horizontal', aspect=50, pad=0.05)
cbar.ax.set_xlabel('Weight Range\nBatches: ' + str(numIters), rotation=0, ha='center', fontsize=15)
fig.suptitle('Perceptron Training', fontsize=20, y=.94)
ani = animation.FuncAnimation(fig, updatefig, frames=1000, interval=10, blit=False)
# ani.save('0-9_multi_weight_LOFI_cbar.mp4', writer=writer)
plt.show()
