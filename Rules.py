import re
import random
import string

def rule1(self, input): #leave here for testing, can't call inside the class for some reason...
    """Enter function"""
    one = re.search(r'i love (.+)', input) #for all input, make lowercase, answer in upper
    if one:
        return True, 'Why do you love ' + one[1] + '?'
    else:
        return False, None

def rule2(self, input): #input when a car company was founded
    """Enter function"""
    two = re.search(r'when was (.+)', input)
    if two:
        return True, two[1] + ' was founded in 1925 by Enzo Ferrari'
    else:
        return False, None

def rule3(self,input): #two variable
    """Rule 3 handles questions about the top speed of a car"""

    three = re.search(r'the (.+) (.+) of a (.+)', input)

    if three and (three[3] in carDict): #combine 1 and 2 for testing only
        topSpeed = three[1] + ' ' + three[2]
        car = three[3]
        madeBy = carDict[car]['made']
        answer = carDict.get(three[3])[topSpeed]

        return True, 'The ' + topSpeed + ' of a ' + madeBy + ' ' + car.capitalize() + ' is ' + answer
    else:
        return False, None #could return response message here

def rule4(self,input): #ask if you would go that fast?
    """Enter function"""
    four = re.search(r'i aborr (.+)', input)
    if four:
        return True, 'Why do you 4 ' + four[1] + '?'
    else:
        return False, None

def rule5(self,input):
    """Enter function"""
    five = re.search(r'i aborr (.+)', input)
    if five:
        return True, 'Why do you 5 ' + five[1] + '?'
    else:
        return False, None

def rule6(self,input):
    """Enter function"""
    six = re.search(r'i aborr (.+)', input)
    if six:
        return True, 'Why do you 6 ' + six[1] + '?'
    else:
        return False, None

def rule7(self,input):
    """Enter function"""
    seven = re.search(r'i aborr (.+)', input)
    if seven:
        return True, 'Why do you 7 ' + seven[1] + '?'
    else:
        return False, None

def rule8(self,input):
    """Enter function"""
    eight = re.search(r'i aborr (.+)', input)
    if eight:
        return True, 'Why do you 8 ' + eight[1] + '?'
    else:
        return False, None

def rule9(self,input):
    """Enter function"""
    nine = re.search(r'i aborr (.+)', input)
    if nine:
        return True, 'Why do you 9 ' + nine[1] + '?'
    else:
        return False, None

def rule10(self,input):
    """Enter function"""
    ten = re.search(r'i aborr (.+)', input)
    if ten:
        return True, 'Why do you 10 ' + ten[1] + '?'
    else:
        return False, None

def rule11(self,input):
    """Enter function"""
    eleven = re.search(r'i aborr (.+)', input)
    if eleven:
        return True, 'Why do you 11 ' + eleven[1] + '?'
    else:
        return False, None

def rule12(self,input):
    """Enter function"""
    twelve = re.search(r'i aborr (.+)', input)
    if twelve:
        return True, 'Why do you 12 ' + twelve[1] + '?'
    else:
        return False, None

def rule13(self,input):
    """Enter function"""
    thirteen = re.search(r'i aborr (.+)', input)
    if thirteen:
        return True, 'Why do you 13 ' + thirteen[1] + '?'
    else:
        return False, None

def rule14(self,input):
    """Enter function"""
    fourteen = re.search(r'i aborr (.+)', input)
    if fourteen:
        return True, 'Why do you 14 ' + fourteen[1] + '?'
    else:
        return False, None

def rule15(self,input):
    """Enter function"""
    fifteen = re.search(r'i aborr (.+)', input)
    if fifteen:
        return True, 'Why do you 15 ' + fifteen[1] + '?'
    else:
        return False, None

def rule16(self, input):
    """This rule returns a random input when ELIZA doesn't understand the question"""
    input = input.split() #place holder, works for now
    # return False, "I don't know what " + input[random.randint(0, len(input) - 1)] + " are!" #formatting works, need regex
    return False, "Let's just talk about sports cars, okay?"
    # number = random.randint(0, len(ruleList) - 1 )

corvette = {'made': 'Chevrolet', 'engine': 'V8', 'top speed': '200mph', 'fast': 'yes'}
enzo = {'made': 'Ferrari', 'engine': 'V12','top speed': '221mph', 'fast': 'yes'}
nineEleven = {'made': 'Porsche', 'engine': 'Boxer 6','top speed': '191mph', 'fast': 'yes'}

carDict = {'corvette': corvette, 'enzo': enzo, '911': nineEleven}



#end
