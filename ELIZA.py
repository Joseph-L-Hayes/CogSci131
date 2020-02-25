# import re
# import random
#
# def ruleOne(self, answer): #leave here for testing, can't call inside the class for some reason...
#     one = re.search(r'I love (.+)', answer)
#     if one:
#         return True, 'ELIZA: Why do you love ' + one[1] + '?' #this format works
#
# def ruleTwo(self, answer): #answer when a car company was founded
#     two = re.search(r'when was (.+)', answer)
#
#     if two:
#         # self.text = two[1] + ' was founded in 1925 by Enzo Ferrari'
#         return True, two[1] + ' was founded in 1925 by Enzo Ferrari'
#
# def ruleSixteen(self, answer):
#     """This rule returns a random answer when ELIZA doesn't understand the question"""
#     return None
#
#
# class ELIZA:
#     """This chatbot will talk about sports cars"""
#
#     def __init__(self):
#         # self.name = self.takeName()
#         self.ruleDict = {} #dictionary with rule name as key and string as value
#         self.text = 'Hello, my name is ELIZA. Ask me anything about sports cars!'
#
#     def takeName(self):
#         """Takes in the user's name from the terminal"""
#         return input(self.text)
#
#     def getInput(self, answer):
#         return input(self.text)
#
#     def randomRule(self, ruleList):
#         """Takes in a list of rules and returns one at random"""
#         number = random.randint(0, len(ruleList) - 1 )
#
#         return ruleList[number]
#
#     def rules(self):
#         return None
#
#     def matchRule(self, answer): #Ensure that at least 5 rules have one variable and at least 5 have two variables.
#         list = []
#
#         for key, rule in self.ruleDict.items():
#             matches, answer = rule(self, answer) #this is currently broken
#             if matches:
#                 list += [answer]
#                 #we need to store the
#
#         if len(list) > 1:
#             return self.randomRule(list) #FINISH, should probably not modify self.text from the rule, do here instead
#         # else:
#         #     return self.text #need to figure out how to handle the rule and their answers
#
#     def generateRules(self): #integers as keys and function names as values
#         self.ruleDict[1] = ruleOne
#         self.ruleDict[2] = ruleTwo
#         # print(self.ruleDict)
#
#
#     def main(self):
#         self.generateRules()
#         answer = self.getInput(self.text)
#         question = self.matchRule(answer)
#         self.getInput(question)
#
#
# if __name__ == "__main__":
#     ELIZA().main()

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
