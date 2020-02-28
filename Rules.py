import re
import random
import string

def rule1(self, input):
    """Rule 1 applies to """
    one = re.search(r'of (.+) does \b(?:a|an|the)\b (.+) ([a-z]+)', input)
    if one and (one[2] in carDict) and (carDict[one[2]][one[1]]):
        car = one[2]
        part = carDict[car][one[1]]
        return True, 'The ' + car + ' has a ' + part + ' ' + one[1] + '.'
        # return True, 'The %s has a %s transmission', car, trans
    else:
        return False, None

def rule2(self, input): #input when a car company was founded
    """Rule 2 applies to questions about the horsepower of a car"""
    two = re.search(r'how much (.+) does \b(?:a|an|the)\b (.+) have?', input) #needs to be more general
    if two and (two[2] in carDict):
        car = two[2].capitalize()
        return True, 'A ' + car + ' has ' + carDict[two[2]]['power']
    else:
        return False, None

def rule3(self,input): #two variable
    """Rule 3 answers questions about the top speed of a car"""

    three = re.search(r'the (.+) (.+) of \b(?:a|an|the)\b (.+)', input) #would like to have optional word in place of just a: 'a', 'an', 'the'

    if three and (three[3] in carDict): #combine 1 and 2 for testing only
        topSpeed = three[1] + ' ' + three[2]
        car = three[3]
        madeBy = carDict[car]['make']
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

def rule15(self,input): #need to make sure other functions haven't applied yet: use a class and global variable?
    """Rule 15 applies if a car other than one ELIZA knows is asked about"""
    fifteen = re.search(r'a (.+)', input)
    partOne, partTwo = randomCar()
    if fifteen and carDict.get(input, True):
        return True, "I don't think " + fifteen[1].capitalize() + " is a sports car." + " Want to hear about the " + partOne + " " + partTwo + "?"
    else:
        return False, None

def rule16(self, input):
    """This rule returns a random input when ELIZA doesn't understand the question"""
    partOne, partTwo = randomCar()

    return False, "Let's just talk about sports cars, okay? " + "Want to hear about the " + partOne + " " + partTwo + "?"

def randomCar():
    """Returns a random car from carDict"""
    modelList = list(carDict.keys())
    randomCar = modelList[random.randint(0, len(carDict) - 1)]
    partOne = carDict[randomCar]['make']
    partTwo = carDict[randomCar]['name']

    return partOne, partTwo

corvette = {'name': 'Corvette', 'transmission': '7spd manual','price': '$123,000','power': '755 hp','make': 'Chevrolet', 'engine': 'V8', 'top speed': '200mph', '60': '3.0 seconds'}
huracan = {'name': 'Huracan', 'transmission': '7spd automatic', 'price': '$261,000', 'power': '630 hp', 'make': 'Lamborghini', 'engine': 'V10','top speed': '199mph', '60': '3.4 seconds'}
nineEleven = {'name': '911', 'transmission': '7spd automatic', 'price': '$123,000', 'power': '540 hp', 'make': 'Porsche', 'engine': 'Turbo Boxer 6','top speed': '191mph', '60': '2.8 seconds'}
roadster = {'name': 'Roadster', 'transmission': '1spd automatic', 'price': '$200,000', 'power': '10000 Nm', 'make': 'Tesla', 'engine': 'Electric','top speed': '250mph', '60': '1.9 seconds'}
eightTwelveSuper = {'name': '812 Superfast', 'transmission': '7spd automatic','price': '$335,000', 'power': '788 hp', 'make': 'Ferrari', 'engine': 'V12','top speed': '211mph', '60': '2.9 seconds'}

carDict = {'corvette': corvette, 'huracan': huracan, '911': nineEleven, 'roadster': roadster, '812 superfast': eightTwelveSuper}

# number = random.randint(0, len(ruleList) - 1 )
# return False, "I don't know what " + input[random.randint(0, len(input) - 1)] + " are!" #formatting works, need regex


#end
