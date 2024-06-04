#!/usr/bin/env python

import random

def main():
    """Start a color game"""
    print("Guess the colour!")

    rainbow = ["red","orange","yellow","green","blue","indigo","violet"]

    x=random.choice(rainbow)
    #print( )
    guess=None

    while x!=guess:
        guess = str(input("What colour an I thinking of ?"))

        if x ==guess:
            print("You guessed {}. Congratulation you got it right!".format(guess))
            break
        else :
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
    
main()
