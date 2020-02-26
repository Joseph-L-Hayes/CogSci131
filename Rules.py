import re
import random

def rule1(self, answer): #leave here for testing, can't call inside the class for some reason...
    one = re.search(r'I love (.+)', answer)
    if one:
        return True, 'ELIZA: Why do you love ' + one[1] + '?' #this format works

def rule2(self, answer): #answer when a car company was founded
    """Enter function"""
    two = re.search(r'when was (.+)', answer)

    if two:
        # self.text = two[1] + ' was founded in 1925 by Enzo Ferrari'
        return True, two[1] + ' was founded in 1925 by Enzo Ferrari'

def rule3(self, input):
    """Enter function"""
    return None

def rule4(self, input):
    """Enter function"""
    return None

def rule5(self, input):
    """Enter function"""
    return None

def rule6(self, input):
    """Enter function"""
    return None

def rule7(self, input):
    """Enter function"""
    return None

def rule8(self, input):
    """Enter function"""
    return None

def rule9(self, input):
    """Enter function"""
    return None

def rule10(self, input):
    """Enter function"""
    return None

def rule11(self, input):
    """Enter function"""
    return None

def rule12(self, input):
    """Enter function"""
    return None

def rule13(self, input):
    """Enter function"""
    return None

def rule14(self, input):
    """Enter function"""
    return None

def rule15(self, input):
    """Enter function"""
    return None

def rule16(self, answer):
    """This rule returns a random answer when ELIZA doesn't understand the question"""
    return None
