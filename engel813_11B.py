# CSci 1133 HW 11
# Kayla Engelstad
# HW Problem 11B
# Lab Section 22

# GUESSING GAME CODE
# This program will allow a human and computer to play a guessing game. The first player to guess the randomly
# chosen integer in the range 0-99 will be the winner. HumanPlayer and ComputerPlayer will be derived from the
# abstract Player class. the play function will run the game, taking 2 'players' and the answer as arguments.

# imports

import random

# define classes

# base class
class Player(object):
    def __init__(self, guess=None):
        self.guess = guess

    def getGuess(self):
        raise NotImplemented


# subclasses
class HumanPlayer(Player):
    def __init__(self, guess=None):
        Player.__init__(self, guess)

    def getGuess(self):
        valid_guess = False

        while not valid_guess:
            guess = int(input("Enter a guess between 0 and 99: "))

            if (guess >= 0) and (guess <= 99):
                valid_guess = True
                return guess

            elif (guess < 0) or (guess > 99):
                string = ('Invalid value entered: ' + str(guess) + ' please try again.')
                print(string)


class ComputerPlayer(Player):
    def __init__(self, guess=None):
        Player.__init__(self, guess=None)

    def getGuess(self):
        guess = random.randint(0,99)
        return guess

class SmartComp(Player):
    def __init__(self, guess=None, numlist=[]):
        Player.__init__(self, guess)
        self.numlist = numlist

    def eliminateGuesses(self, lastGuess=0, result=None):
        guesses = self.numlist
        new_guesses = []

        if result == True:
            for i in range(len(guesses)):
                if guesses[i] < lastGuess:
                    new_guesses.append(guesses[i])

        elif result == False:
            for i in range(len(guesses)):
                if guesses[i] > lastGuess:
                    new_guesses.append(guesses[i])

        self.numlist = new_guesses

        return self.numlist

    def getGuess(self):
        guesses = self.numlist
        bnum = (len(guesses)) // 2
        guess = guesses[bnum]
        return guess

    def getNumList(self):
        return self.numlist
            

# functions

def checkGuess(g1, answer):
    print("You guessed: ", g1)

    if g1 == answer:
        found = True
        result = None
        print("You're right! You win!")

    elif g1 > answer:
        found = False
        result = True
        print("Your guess is too high.")

    elif g1 < answer:
        found = False
        result = False
        print("Your guess is too low.")

    return (found, result)
    

# play function
def play(p1, p2, answer):

    # loop and take turns unitl answer is found
    found = False
    val2 = None

    if 'SmartComp' not in (str(type(p1)) and str(type(p2))):

        while not found:

            val, result = checkGuess(p1.getGuess(), answer)

            if val == False:
                val2 = checkGuess(p2.getGuess(), answer)

            if (val == True) or (val2 == True):
                found = True

    elif ('SmartComp' in (str(type(p1)))) and ('SmartComp' in str(type(p2))):

        while not found:

            val, result = checkGuess(p1.getGuess(), answer)

            if val == False:
                p2.eliminateGuesses(p1.getGuess(), result)
                p1.eliminateGuesses(p1.getGuess(), result)
                val2, result = checkGuess(p2.getGuess(), answer)
                p1.eliminateGuesses(p2.getGuess(), result)
                p2.eliminateGuesses(p2.getGuess(), result)

            if (val == True) or (val2 == True):
                found = True

    elif ('SmartComp' in (str(type(p1)))) and ('SmartComp' not in (str(type(p2)))):

        while not found:

            val, result = checkGuess(p1.getGuess(), answer)

            if val == False:
                p1.eliminateGuesses(p1.getGuess(), result)
                val2, result = checkGuess(p2.getGuess(), answer)
                p1.eliminateGuesses(p2.getGuess(), result)

            if (val == True) or (val2 == True):
                found = True

    elif ('SmartComp' in (str(type(p2)))) and ('SmartComp' not in (str(type(p1)))):

        while not found:

            num1 = p1.getGuess()
            val, result = checkGuess(num1, answer)

            if val == False:
                #print(p2.getNumList())
                p2.eliminateGuesses(num1, result)
                #print(p2.getNumList())
                num2 = p2.getGuess()
                val2, result = checkGuess(num2, answer)
                #print(p2.getNumList())
                p2.eliminateGuesses(num2, result)
                #print(p2.getNumList())

            if (val == True) or (val2 == True):
                found = True


# --main

numlist = []
for i in range(0,100):
    numlist.append(i)

num = random.randint(0,99)

p1 = HumanPlayer()
p2 = ComputerPlayer()
p3 = SmartComp(numlist=numlist)
p4 = SmartComp(numlist=numlist)

play(p2, p3, num)
            

        


                
        
