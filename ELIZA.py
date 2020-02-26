import re
import random
import Rules

class ELIZA:
    """This chatbot will talk about sports cars"""

    def __init__(self):
        # self.name = self.takeName()
        self.ruleDict = {} #dictionary with rule name as key and string as value
        self.text = 'Hello, my name is ELIZA. Ask me anything about sports cars!'

    def takeName(self):
        """Takes in the user's name from the terminal"""
        return input(self.text)

    def getInput(self, answer):
        return input(self.text)

    def randomRule(self, ruleList):
        """Takes in a list of rules and returns one at random"""
        number = random.randint(0, len(ruleList) - 1 )

        return ruleList[number]

    def rules(self):
        return None

    def matchRule(self, answer): #Ensure that at least 5 rules have one variable and at least 5 have two variables.
        list = []

        for key, rule in self.ruleDict.items():
            matches, answer = rule(self, answer) #this is currently broken
            if matches:
                list += [answer]
                #we need to store the

        if len(list) > 1:
            return self.randomRule(list) #FINISH, should probably not modify self.text from the rule, do here instead
        # else:
        #     return self.text #need to figure out how to handle the rule and their answers

    def generateRules(self):
        """Generates a dictionary of rules"""
        for i in range(1, 17):
            self.ruleDict[i] = eval('Rules.rule' + str(i))
            print(self.ruleDict[i])
        # print(self.ruleDict)

    def main(self):
        self.generateRules()
        userInput = self.getInput(self.text)

        while userInput != 'q':

            elizaOutput = self.matchRule(userInput) #matchRule should return the statement
            userInput = self.getInput(elizaOutput) #asks next question


if __name__ == "__main__":
    ELIZA().main()

"""Use a dictionary/list of sports car manufacturers, models, year range, top speeds, colors, HP/torque, engine sizes

Ferrari, Porsche, General Motors: Camaro, Corvette, Firebird

May be a good idea to use the car as the focus of the discussion instead of manufacturers"""

# class Example(object):
#     def main(self):
#         print ("Hello World!")
#
# if __name__ == '__main__':
#     Example().main()

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
