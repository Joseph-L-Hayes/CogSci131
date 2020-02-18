import re
from PyDictionary import PyDictionary
import random
"""documentation for re:
    https://docs.python.org/3/library/re.html """


#lecture example
# s = 'My name is ELIZA the chatbot'
#
# m = re.search(r"My name is (.+) the (.+)", s) #makes this very simple compared to Java
#
# if m:
#     print(m.groups())

def response(s1, s2):
    m = re.search(r"My name is (.+) the (.+)", s1) #simple pattern matching
    z = re.search(r"My name is (.+)", s2)

    one = m.group(1) #string matches pattern, one is the first part of match
    two = m.group(2)
    three = z.group(1)
    # three = m.group(3) #will error if no group exists

    #go over randomizing the adjective for the response

    if m and z:
        print('Hello %s the %s, it is a pleasure to meet you!' % (one, two))
        print('Hello %s, it is a pleasure to meet you!' % three)
        # print('Group 1:', m.group(1))
        # print('Group 2:', m.group(2))

    if one:
        print(one)

    # if z:
    #     print(z.group(1))
    #groups are the (.+) portions of the string
    #this allows you to pick out parts of the string you may want to work with

def responseAll(*args):

    for x in args:
        y = re.search(r"My name is (.+) the (.+)", x)
        if (y):
            print(y.group())

def responseInput(*args):
    name = input("Hello, what is your name?")


    print('Hello %s, it is a pleasure to meet you.' % (name))

# def running(*args): #identify the noun and the verb, return a response
    # dictionary = PyDictionary()
    # verb, noun = '', ''
    # for w in args:
    #     number = random.randint(1, 101)
    #     pos = dictionary.meaning(w)
    #     # print(pos)
    #     if pos and 'Noun' in pos.keys():
    #         noun = w
    #         print(noun)
    #     if pos and 'Verb' in pos.keys():
    #         verb = w
    #         print(verb)


    # print('I can %s %s %s. ' % (verb, number, noun))

def running2(): #try using regex matching for response
    return None


# response('My name is ELIZA the chatbot', 'My name is Joe')
# running('How', 'many', 'miles', 'can', 'you', 'run?')
# running('miles')
#
# responseAll('My name is ELIZA the chatbot', 'My name is Joe')

# responseInput()



# def printString(*args):
#     y= ''
#
#     print('Arguments with formatting, each step: ')
#     for x in args:
#         y += '%s%s' % (x, ' ') #each %s will require one variable be assigned to it
#         # += can be used to build a string, perhaps recursively as in natural linguistics
#         print(y)
#
#     print()
#     print('Completed string with formatting: ')
#     print(y) #prints the completed string, which we have added spaces to
#
#     print()
#
#     print('Arguments without formatting: ')
#     for x in args:
#         print(x)
#
# printString('I', 'would', 'like', 'to', 'learn', 'more', 'about', 'python')

""" Only refer to things below here. """
def ruleOne(string):

    pets = ['dog', 'cat', 'fish']
    cars = ['Honda', 'Chevy']
    nouns = {}

    nouns.update(pet = pets)
    nouns.update(car = cars)

    for x, y in nouns.items():
        if string in nouns[x]:
            print('I have a %s too' % string)

def ruleTwo(string):
    return False

def ruleThree(string):
    return False


# for pet in pets:
#     print(pet)
def takeQuestion():
    rules = {1: ruleOne, 2:ruleTwo, 3:ruleThree}
    number = random.randint(1, 3)
    print(number)


    s = input('What kind of pet do you have?')
    rules[number](s)


takeQuestion()
# def test():


"""To uncomment the above after #, highlight the text and use command + /"""












#end
