import re
import random

def rule1(self, input): #leave here for testing, can't call inside the class for some reason...
    """Enter function"""
    one = re.search(r'I love (.+)', input)
    if one:
        return True, 'ELIZA: Why do you love ' + one[1] + '?'
    else:
        return False, None

def rule2(self, input): #input when a car company was founded
    """Enter function"""
    two = re.search(r'when was (.+)', input)

    if two:
        # self.text = two[1] + ' was founded in 1925 by Enzo Ferrari'
        return True, two[1] + ' was founded in 1925 by Enzo Ferrari'
    else:
        return False, None

def rule3(self,input):
    """Enter function"""
    three = re.search(r'I hate (.+)',input)
    if three:
        return True, 'ELIZA: Why do you hate ' + three[1] + '?'
    else:
        return False, None

def rule4(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 4 ' + one[1] + '?'
    else:
        return False, None

def rule5(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 5 ' + one[1] + '?'
    else:
        return False, None

def rule6(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 6 ' + one[1] + '?'
    else:
        return False, None

def rule7(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 7 ' + one[1] + '?'
    else:
        return False, None

def rule8(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 8 ' + one[1] + '?'
    else:
        return False, None

def rule9(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 9 ' + one[1] + '?'
    else:
        return False, None

def rule10(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 10 ' + one[1] + '?'
    else:
        return False, None

def rule11(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 11 ' + one[1] + '?'
    else:
        return False, None

def rule12(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 12 ' + one[1] + '?'
    else:
        return False, None

def rule13(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 13 ' + one[1] + '?'
    else:
        return False, None

def rule14(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 14 ' + one[1] + '?'
    else:
        return False, None

def rule15(self,input):
    """Enter function"""
    one = re.search(r'I aborr (.+)', input)
    if one:
        return True, 'ELIZA: Why do you 15 ' + one[1] + '?'
    else:
        return False, None

def rule16(self, input):
    """This rule returns a random input when ELIZA doesn't understand the question"""
    return "I don't know what " + input " is!"
