#Problem Set 2
#Name: Trevor Tomlin
#Collaborators: N/A
#Time: 2:00

import random
import string
import re

WORDLIST_FILENAME = "words.txt"

def load_words():
    print ("Loading words from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print (" ",len(wordlist), "words loaded.")
    print ("-"*25)
    return (wordlist)

def choose_word(wordlist):
    return random.choice(wordlist)

def check_letter(guess, word, correctList):
    for i,c in enumerate(word):
        if c == guess:
            correctList[i] = c

    return (correctList)

def hangman(word,guesses):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is {} letters long".format(len(word)))
    print ("-"*25)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    find = [" _ "] * len(word)
    correctList = [" _ "] * len(word)
    origList = []
    while guesses > 0 and correctList != list(word):
        print ("You have {} guesses left".format(guesses))
        print ("Available letters:")
        print (",".join(letters))
        guess = str(input("Guess a letter:"))
        guess = guess.lower()
        while not (guess in letters):
            print ("Incorrect answer, try again")
            guess = str(input("Guess a letter:"))
            guess = guess.lower()
        origList = list(correctList)
        find = check_letter(guess, word, correctList)

        if correctList == origList:
            print("Oops! That letter is not in my word")
            print ("-"*25)
            guesses = guesses - 1
            print (" ".join(find))
            letters.remove(guess)
        else:
            print("Good Guess")
            print ("-"*25)
            print (" ".join(find))
            letters.remove(guess)

    if guesses == 0:
        print ("You lose!")
        print ("The word was:", word)
    else:
        print ("Congradulations, you won!")

def main():
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = int(input("Enter the difficulty:"))
    guesses = 0
    while guesses == 0:
        if difficulty == 1:
            guesses = 15
        elif difficulty == 2:
            guesses = 10
        elif difficulty == 3:
            guesses = 5
        else:
            print ("Print that number is not valid")
    wordlist = load_words()
    word = choose_word(wordlist)
    #print (word)
    hangman(word, guesses)

if __name__ == '__main__':
    main()
