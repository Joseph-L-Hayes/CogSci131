import re
import random

class ELIZA:
    """This chatbot will talk about sports the user participates in"""

    def __init__(self):
        self.name = self.takeName()

    def takeName(self):
        """Takes in the user's name from the terminal"""
        return input('Hello, my name is ELIZA. What is your name?')

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 1 )

        return ruleList[number]

    def rules(self):
        return None

    def main(self):
        print("take 2")
        self.takeName()

if __name__ == "__main__":
    ELIZA().main()



ELIZA()

#project 4





#end
