import string
from english_words import english_words_set
import random

reqLetter = 'p'
optLetters = 'amlevd' + reqLetter
wordList = ['palladium', 'palindrome', 'papa', 'hive', 'soda', 'enterprise', 'paddle', 'paddled', 'buck']

def buildWords(reqLetter, optLetters, words): #this is for building a list of words for the game
    """Returns a list of words containing only the required letter and optional letters"""
    acceptedWords = []
    for word in words:
        if reqLetter in word and len(word) >= 4:
            mytable = word.maketrans(optLetters, ' ' * len(optLetters))
            result = word.translate(mytable).replace(' ', '')
            if len(result) == 0:
                acceptedWords += [word]

    return acceptedWords

# myWords = buildWords(reqLetter, optLetters, english_words_set) #works!

vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
easyLetters = {'d': 2, 'g': 2, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1} #1 and 2 points
medLetters = {'b': 3, 'c': 3, 'f': 4, 'h': 4, 'k': 5, 'm': 3, 'p': 3, 'v': 4, 'w': 4, 'y': 4} #3-5 points
hardLetters = {'j': 8, 'q': 10, 'x': 8, 'z': 10} #6+ points
consonants = [easyLetters, medLetters, hardLetters]

def getRequiredLetter(easyDict, medDict):
    """Returns one required letter from easy or medium letter lists"""
    return random.choice(list(easyDict.items()) + list(medDict.items()))[0]

def getLetters(numVowel, numEasy, numMed, numHard):
    """Returns 6 letters for the game made up of a random letters made up of quantity of
        passed in args.
        Example: getLetters(2, 2, 2, 1) returns 2 vowels, 2 easy, 2 med, and 1 hard. """
    letters = ''
    for v in range(numVowel):
        letter += random.choice(list(vowels.items()))[0]
        if letter not in letters:
            letters += letter

    for e in range(numEasy):
        letter += random.choice(list(easyLetters.items()))[0]

    for m in range(numMed):
        letter += random.choice(list(medLetters.items()))[0]

    for h in range(numHard): #may need a probability based method for getting hard
        letter += random.choice(list(hardLetters.items()))[0]

    return letters

required = getRequiredLetter(easyLetters, medLetters)
letters = getLetters(2, 2, 2, 1)
print(required)
print(letters)

wordList = buildWords(required, letters, english_words_set)
print(wordList)

# dict = { 'A' : 1, 'B' : 2, 'C' : 3}
#
# random_element = random.choice(list(dict.items()))
# # Output = (key, value)
# print(random_element[0])
