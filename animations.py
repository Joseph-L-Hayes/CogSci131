import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import image_resources as ir
#
# fig = plt.figure()
#
#
# def f(x, y):
#     return np.sin(x) + np.cos(y)
#
# # x = np.linspace(0, 2 * np.pi, 120)
# # y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# data = np.random.normal(0, 1, 784)
# im = plt.imshow(data.reshape(28, 28), animated=True, cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')]), interpolation=ir.interpol_methods[4])
#
#
# def updatefig(data, im):
#     data[np.random.choice(data)] += 1
#     data[random.randint(0, 783)] -= 1
#     data[random.randint(0, 783)] += 1
#     data[random.randint(0, 783)] += 1
#     im.set_array(data.reshape(28, 28))
#     return im,
#
# ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
# plt.show()

fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

im = plt.imshow(f(x, y), animated=True)


def updatefig(*args):
    global x, y
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_array(f(x, y))
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()


class Perceptron(object):

    def __init__(self, dimensions, data, digit0, digit1):
        self.weights = np.random.normal(0, 1, size=dimensions)
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

    def aniTrain(self, image):

        label = self.random_label()
        data = self.data_set[label]
        sub_data = random.choice(data)
        y = self.predict(self.weights, sub_data, self.bias)
        print('here')

        if label == 0 and y == 1:
            self.bias -= sub_data
            self.weights -= sub_data - self.bias
        elif label == 1 and y == 0:
            self.bias += sub_data
            self.weights += sub_data + self.bias

        image.set_array(self.weights.reshape(28, 28))

        return image


    def train(self, threshold, precision, blocks, plot=False):
        """Data_set is a dictionary of lists containing (784,) arrays"""
        accuracy = .5
        all_blocks = blocks
        correct = 0
        accuracy_trace = []
        xAxis = []
        acc_delta = 1
        getcontext().prec = precision
        fig = plt.figure()
        im = plt.imshow(self.weights.reshape(28, 28), animated=True, cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')]), interpolation=ir.interpol_methods[0])

        # self.aniTrain(blocks)

        # while (all_blocks // 25) <= 500:
        #
        #     xAxis += [all_blocks // 25]
        #     acc_delta = accuracy
        #
        #     for i in range(blocks):
        #         label = self.random_label()
        #         data = self.data_set[label]
        #         sub_data = random.choice(data)
        #         y = self.predict(self.weights, sub_data, self.bias)
        #
        #         if label == 0 and y == 1:
        #             self.bias -= sub_data
        #             self.weights -= sub_data - self.bias
        #         elif label == 1 and y == 0:
        #             self.bias += sub_data
        #             self.weights += sub_data + self.bias
        #         elif (label == 0 and y == 0) or (label == 1 and y == 1):
        #             correct += 1

                #try live plot here, use self.get_weights().reshape

            # ani.updatefig(self.weights, im)
        ani.animation.FuncAnimation(fig, self.aniTrain(blocks, im), interval=50, blit=True)
        plt.show()

            # accuracy = correct / all_blocks
            # acc_delta = abs(round(Decimal(accuracy), precision) - round(Decimal(acc_delta), precision))
            # all_blocks += blocks
            # accuracy_trace.append(accuracy)

        # self.overall_accuracy = accuracy

        if plot:
            self.plot_accuracy(xAxis, accuracy_trace)


def aniTrain2(data, image):

    label = self.random_label()
    data = self.data_set[label]
    sub_data = random.choice(data)
    y = self.predict(self.weights, sub_data, self.bias)
    print('here')

    if label == 0 and y == 1:
        self.bias -= sub_data
        self.weights -= sub_data - self.bias
    elif label == 1 and y == 0:
        self.bias += sub_data
        self.weights += sub_data + self.bias

    image.set_array(self.weights.reshape(28, 28))

    return image


fig = plt.figure()
im = plt.imshow(zeroOnePercept.weights.reshape(28, 28), animated=True, cmap=plt.get_cmap(ir.color_maps[ir.color_maps.index('inferno')]), interpolation=ir.interpol_methods[0])
animation.FuncAnimation(fig, aniTrain, interval=50, blit=True)
plt.show()
