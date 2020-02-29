import re
import random
import string
import Rules

class ELIZA:
    """This chatbot will talk about sports cars"""

    def __init__(self):
        # self.name = self.takeName()
        self.ruleDict = {} #dictionary with rule name as key and string as value
        self.text = 'ELIZA: Hello, my name is ELIZA. Ask me anything about sports cars!'

    def getInput(self, userInput):
        """Enter function"""
        return input(userInput)

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 1 )

        return ruleList[number]

    def matchRule(self, input): #Ensure that at least 5 rules have one variable and at least 5 have two variables.
        """Enter function"""
        ruleList = []

        for key, rule in self.ruleDict.items():
            matches, answer = rule(self, input)
            if matches:
                ruleList += [answer]

        if len(ruleList) > 1:
            return self.randomRule(ruleList)
        elif len(ruleList) == 1:
            return ruleList[0]
        else:
            match, answer = self.ruleDict[14](self, input)
            return answer

    def generateRules(self):
        """Generates a dictionary of rules"""
        for i in range(1, 16):
            self.ruleDict[i] = eval('Rules.rule' + str(i))

    def main(self):
        self.generateRules()
        print(self.text)
        userInput = self.getInput("USER: ").lower().strip(string.punctuation)

        while userInput != 'q':

            elizaOutput = self.matchRule(userInput.lower())
            print('ELIZA: ' + elizaOutput)
            userInput = self.getInput('USER: ').lower().strip(string.punctuation)

if __name__ == "__main__":
    ELIZA().main()

"""Use a dictionary/list of sports car manufacturers, models, year range, top speeds, colors, HP/torque, engine sizes

Ferrari, Porsche, General Motors: Camaro, Corvette, Firebird

May be a good idea to use the car as the focus of the discussion instead of manufacturers"""

#project 4

#
# response = input("What is your name? ")
#
# while response != 'q':
#     # response = ruleOne(response) #pattern match
#     for doesntmatter, value in rules.items():
#         answer = value(response) # = ruleOne(string)
#         if answer != None:
#             response = answer
#             break
#
#     response = input(response)




#end
