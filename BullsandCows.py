#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:47:59 2017

@author: raphael
"""
import random

def generateNmbr():
   number = random.sample(range(10), 4) 
   return number


def hints(guess, number):
    hints = ""
    for i in range(len(guess)):
        
        if int(guess[i]) == number[i]:
            hints += "B"
        elif number[i] in guess:
            hints += "C"
    return hints
    

def playGame(number):
    print("_____________________________")
    print("Let's play Bulls & Cows!")
    print("I'm thinking of a four digit number.")
    pre_guesses = []
    pre_hints = []
    number = number
    i = 10
    while True:
        print("You have %d guesses left" %i)
        guess1 = input("Please guess a four digit number: ")
        
        pre_guesses.append(guess1)
        
        guess = list(map(int, guess1))
        hint = hints(guess, number)
        
       
        pre_hints.append(hint)
        
        if hint == "BBBB":
            print("Congratulations! You guessed my number!")
            break
        else:
            print(hint)
            print("Here are your previous guesses: ")
            for n in range(len(pre_guesses)):
                print(str(pre_guesses[n]) + " " + str(pre_hints[n]))
            print("_______________________________")
        
        i -= 1
        if i == 0:
            number_str = "".join(str(e) for e in number)
            print("You lost. My number was: %s " %number_str)
            break
       

    
   
        
    


number = generateNmbr()
playGame(number)