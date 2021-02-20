import WordBuilder as wb
import string_utils

class SpellingBee(object):
    def __init__(self):
        self.requiredLetter, self.letters, self.wordList = wb.main()
        #need to generate the letters here, use func to choose next required letters
        #from the available letters, then generate a new word list.
        self.acceptedList = []

    def showLetters(self):
        return self.letters

    def showRequired(self):
        return self.requiredLetter

    def shuffleLetters(self):
        self.letters = string_utils.shuffle(self.letters)

    def user_input(self):
        print()
        print('Required Letter:', self.showRequired())
        print('All Letters:', self.showLetters())
        print()
        return input('(Type 1 to Quit, 2 to view your word list, 3 to shuffle letters) Enter a word: ' )

    def check_word(self, word):

        if word == '1':
            return 1

        elif word == '2':
            print(self.acceptedList)
            return 0

        elif word == '3':
            self.shuffleLetters()
            return 0

        elif len(word) < 4:
            print('Word must be 4 or more characters')
            return 0

        elif self.requiredLetter not in word:
            print('The must contain ' + self.requiredLetter)
            return 0

        elif word in self.acceptedList:
            print('Word already found')
            return 0

        elif word in self.wordList:
            self.acceptedList += [word]
            print('Word accepted!')

            if len(self.acceptedList) == len(self.wordList):
                print('Game over, all words found')
                return 1
            else:
                return 0

        else:
            print('Word is not in the word list')
            return 0


def runBee():

    testRun = SpellingBee()
    run = 0
    input = None

    while run == 0:
        input = testRun.user_input()
        run = testRun.check_word(input)
    print(testRun.acceptedList)
    # print(testRun.wordList)

runBee()
