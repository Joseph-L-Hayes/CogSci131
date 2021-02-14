import string
from english_words import english_words_set
import random
import WordBuilder as wb

class SpellingBee(object):
    def __init__(self):
        self.requiredLetter, self.letters, self.wordList = wb.main()
        self.acceptedList = []

    def showLetters(self):
        return self.letters

    def showRequired(self):
        return self.requiredLetter

    def user_input(self):
        print('Required Letter:', self.requiredLetter)
        print('Optional Letters:', self.letters)
        return input('(Type 1 to Quit) Enter a word: ' )

    def check_word(self, word):
        # print('You are here!')
        if word == '1':
            return 1
        if len(word) < 4:
            print('One')
            return 'Word must be 4 or more characters'
        elif self.requiredLetter not in word:
            print('Two')
            return 'The must contain ' + self.requiredLetter
        elif word in self.acceptedList:
            print('Three')
            return 'Word already found'
        elif word in self.wordList:
            print('Four')
            # print('Word accepted!')
            self.acceptedList += [word]
            return 'Word accepted!'
        else:
            return 'What happened?'


def runBee():

    testRun = SpellingBee()
    input = None

    while input != '1':
        input = testRun.user_input()
        run = testRun.check_word(input)
        print(run)
    print(testRun.acceptedList)
        # print(testRun.wordList)

runBee()
