import re
import random


def ruleOne(self, answer): #leave here for testing, can't call inside the class for some reason...
    one = re.search(r'I love (.+)', answer)
    if one:
        self.text = 'Why do you love ' + one[1] +'?' #this format works
        return True

def ruleTwo(self, answer):
    return None


class ELIZA:
    """This chatbot will talk about sports the user participates in"""

    def __init__(self):
        # self.name = self.takeName()
        self.ruleDict = {} #dictionary with rule name as key and string as value
        self.text = 'Hello, my name is ELIZA. What is your name?'

    def takeName(self):
        """Takes in the user's name from the terminal"""
        return input(self.text)

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 1 )

        return ruleList[number]

    def rules(self):
        return None

    def getInput(self, answer):
        return input(self.text)

    def matchRule(self, answer): #Ensure that at least 5 rules have one variable and at least 5 have two variables.
        # list = []

        for key, rule in self.ruleDict.items():
            if rule(self, answer):
                list += [rule]
                #not finished!

        if len(list) > 1:
            return self.randomRule(list) #FINISH
        else:
            return self.text #need to figure out how to handle the rule and their answers

    def generateRules(self):
        self.ruleDict[1] = ruleOne
        self.ruleDict[2] = ruleTwo
        print(self.ruleDict)


    def main(self):
        self.generateRules()
        answer = self.getInput(self.text)
        question = self.matchRule(answer)
        self.getInput(question)


if __name__ == "__main__":
    ELIZA().main()


# class Example(object):
#     def main(self):
#         print ("Hello World!")
#
# if __name__ == '__main__':
#     Example().main()

#project 4





#end
