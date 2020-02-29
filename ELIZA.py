import re
import random
import string
import Rules

class ELIZA:
    """This chatbot will talk about sports cars"""

    def __init__(self):
        self.ruleDict = {}
        self.text = 'ELIZA: Hello, my name is ELIZA. Ask me anything about sports cars!'

    def getInput(self, userInput):
        """Enter function"""
        return input(userInput)

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 2 ) #-2 to avoid rule 15 for multiple

        return ruleList[number]

    def matchRule(self, input):
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

#end
