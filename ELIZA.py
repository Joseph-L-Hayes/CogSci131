import re
import random

class ELIZA:

    def __init__(self):
        self.name = ELIZA.takeQuestion()

    def takeQuestion():
        """Takes in initial question from terminal"""
        return input('Hello, my name is ELIZA. What is your name?')

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 1 )

        return ruleList[number]





#project 4
for i in range(50):
    print(ELIZA().randomRule(list))




#end
