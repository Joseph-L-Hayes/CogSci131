import operator as op

class Foo(object):
    def __init__(self, func):
        #the init function goes into every class and tells the program how to create the object
        #here the only difference between objects would be the function func which I've used as a math
        #function. Entering a non math function or one that takes more or less than 2 arguments would
        #result in an error
        self.func = func

    def mathy(self, num1, num2):
        return self.func(num1, num2)

one = Foo(op.mul)
two = Foo(op.add)
#a note on 'self': to use the mathy function, use name.mathy(num1, num2) where 'name' is the name of the object.
#python will automatically put name in place of self when calling the function.
print('one.mathy(2, 3) =', one.mathy(2, 3))
#prints 6
print('two.mathy(2, 3) =',two.mathy(2, 3))
#prints 5
print(one.func)
#prints <built-in function mul>
print(two.func)
#prints <built-in function add>
print(one) #prints the name of the class object and its location in memory
# prints <__main__.Foo object at 0x101a39dd0>
print(two) #prints the name of the class object and its location in memory
# prints <__main__.Foo object at 0x101a39e50>

#0x101a39e50 is a memory location, see that 'two' location is different than 'one'

"""This demonstrates that the mathy functions are unique to each Foo object. Foo
    is often used for examples because it is essentially a nonsense word or has
    no other meaning"""


class Car(object):

    def __init__(self, carColor, numDoors, transmission):
        #this class object has more to it than the Foo class above.
        self.color = carColor
        self.doors = numDoors
        self.trans = transmission

    def color(self):
        #this is called a 'get' function. For security reasons it is a bad idea to
        #allow someone to access self.color or any other variable because someone could
        #set it to another value. By creating a 'get' function, the user can have access
        #to the color or any other class variable without being able to change it.
        #this isn't really important right now but is good to understand down the road
        #if you ever build a larger program.
        return self.color

    def doors(self):
        return self.doors

    def transmission(self):
        return self.trans

    def __str__(self):
        #the __str__ function, when added to any class will print what you want that object to look like when you print it
        #this is in contrast to the Foo class above which prints some technical computer stuff about the object
        #using __str__ allows you to display something about the object that a human can read if they ever print the object
        return 'This is a ' + self.color + ' car with ' + str(self.doors) + ' doors and a(n) ' + self.trans + ' transmission.'


car1 = Car('red', 4, 'automatic') #here 'self' would refer to car1; it is a unique object
print(car1) #prints the string representation of the the car1 object
car2 = Car('blue', 2, 'manual')
print(car2) #prints the string representation of the the car1 object
car3 = Car('green', 4, 'manual')
print(car3) #prints the string representation of the the car1 object


""" The beauty of Object Oriented Programming (OOP for short) is that you use less code
    to do repetitive tasks and it allows you to create unique objects for pretty much anything
    you want and keeps the variables for each object insulated from the other objects. As we've
    seen while doing cogsci131 assignments, mixing up variables causes a lot of problems and it's
    just difficult to keep track of it all in your head in larger projects!

    Below is my perceptron class from the last assignment as an example of a more complex class
    than the above classes. Also, classes can be used or 'inherited' by each other! But we'll leave that for later :) """


# class Perceptron(object):
#
#     def __init__(self, dimensions, data, digit0, digit1):
#         self.weights = np.random.normal(0, 1, size=dimensions)
#         self.data_set = {0: data[digit0], 1: data[digit1]}
#         self.digits = [digit0, digit1]
#         self.bias = np.zeros(dimensions)
#         self.overall_accuracy = 0
#
#     def get_weights(self):
#         #changed this to a copy when live plotting; may cause issues with other functions already written
#         return self.weights
#
#     def dotProd(self, w, x):
#
#         return np.dot(w, x)
#
#     def predict(self, w, x, b):
#         dot = self.dotProd(w, x)
#
#         if dot >= 0:
#             return 1
#
#         else: return 0
#
#     def classify(self, w, x):
#         dot = self.dotProd(w, x)
#
#         if dot >= 0:
#             return 1
#         else: return 0
#
#     def random_label(self):
#         """Returns a random dataset label"""
#         labels = list(self.data_set.keys())
#         return random.choice(labels)
#
#     def plot_accuracy(self, x, y, save=False, name=None, color='red'):
#
#         plt.xlabel('Blocks of 25')
#         plt.ylabel('Accuracy')
#         plt.title('P1: Training Accuracy for Digits {0} and {1}'.format(self.digits[0], self.digits[1]))
#         plt.legend(loc=0, title='Converged to {0} Accuracy in {1} Blocks'.format(round(y[-1], 5), x[-1]))
#         plt.plot(x, y, c=color, label='')
#
#         if save:
#             plt.savefig(name + '.pdf')
#
#         plt.show()
#         plt.close()
#
#     def train(self, threshold, precision, blocks, plot=False):
#         """Data_set is a dictionary of lists containing (784,) arrays"""
#         accuracy = .5
#         all_blocks = blocks
#         correct = 0
#         accuracy_trace = []
#         xAxis = []
#         acc_delta = 1
#         getcontext().prec = precision
#
#         while (all_blocks // 25) <= 500:
#
#             xAxis += [all_blocks // 25]
#             acc_delta = accuracy
#
#             for i in range(blocks):
#                 label = self.random_label()
#                 data = self.data_set[label]
#                 sub_data = random.choice(data)
#                 y = self.predict(self.weights, sub_data, self.bias)
#
#                 if label == 0 and y == 1:
#                     self.bias -= sub_data
#                     self.weights -= sub_data - self.bias
#                 elif label == 1 and y == 0:
#                     self.bias += sub_data
#                     self.weights += sub_data + self.bias
#                 elif (label == 0 and y == 0) or (label == 1 and y == 1):
#                     correct += 1
#
#
#             accuracy = correct / all_blocks
#             acc_delta = abs(round(Decimal(accuracy), precision) - round(Decimal(acc_delta), precision))
#             all_blocks += blocks
#             accuracy_trace.append(accuracy)
#
#         self.overall_accuracy = accuracy
#
#         if plot:
#             self.plot_accuracy(xAxis, accuracy_trace)
#
#
# zeroOnePercept = Perceptron(N, trainingImages, 0, 1)
# zeroOnePercept.train(.97, 5, 25, plot=False)



#end
