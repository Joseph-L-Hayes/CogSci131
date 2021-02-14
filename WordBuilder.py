import string
from english_words import english_words_set
import random

vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
easyLetters = {'d': 2, 'g': 2, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1} #1 and 2 points
medLetters = {'b': 3, 'c': 3, 'f': 4, 'h': 4, 'k': 5, 'm': 3, 'p': 3, 'v': 4, 'w': 4, 'y': 4} #3-5 points
hardLetters = {'j': 8, 'q': 10, 'x': 8, 'z': 10} #6+ points

def buildWords(wordsList): #this is for building a list of words for the game
    """Returns a list of words containing only the required letter and optional letters"""
    acceptedWords = []
    required_letter = getRequiredLetter(easyLetters, medLetters)
    optional_letters = getLetters(required_letter, 2, 2, 2, 0)

    for word in wordsList:
        if required_letter in word and len(word) >= 4:
            mytable = word.maketrans(optional_letters, ' ' * len(optional_letters))
            result = word.translate(mytable).replace(' ', '')
            if len(result) == 0:
                acceptedWords += [word]
    print(len(acceptedWords))

    if len(acceptedWords) <= 10:
        buildWords(wordsList)

    else:
        return [required_letter, optional_letters, acceptedWords]

def compareStrings(list1, list2):
    """Returns True if list1 is a subset of list2, Else False"""
    return all(x in list2 for x in list1)


def getRequiredLetter(easyDict, medDict):
    """Returns one required letter from easy or medium letter lists"""
    return random.choice(list(easyDict.items()) + list(medDict.items()))[0]

def getLetters(required, numVowel, numEasy, numMed, numHard):
    """Returns 7 letters for the game made up of a random letters made up of quantity of
        passed in args.
        Example: getLetters(2, 2, 2, 1) returns 2 vowels, 2 easy, 2 med, and 1 hard. """

    letters = required
    letter = ''
    count = 0

    while count < numVowel:
        letter = random.choice(list(vowels.items()))[0]
        if letter not in letters:
            # print(letter)
            letters += letter
            count += 1

    count = 0

    while count < numEasy:
        letter = random.choice(list(easyLetters.items()))[0]
        if letter not in letters:
            # print(letter)
            letters += letter
            count += 1
    count = 0

    while count < numMed:
        letter = random.choice(list(medLetters.items()))[0]
        if letter not in letters:
            # print(letter)
            letters += letter
            count += 1

    count = 0

    while count < numHard: #may need a probability based method for getting hard
        letter = random.choice(list(hardLetters.items()))[0]
        if letter not in letters:
            # print(letter)
            letters += letter
            count += 1

    return ''.join(letters)

def main():
    return buildWords(english_words_set)

if __name__ == '__main__':
    main()
