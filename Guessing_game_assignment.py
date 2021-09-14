# Guessing_game_assignment
name = 'emmanuel mkpurunchi f'
title = 'guessing game assignment'
print(f'Name: {name.upper()}. \n Title: {title.upper()}.\n')
from math import *
import random


def guessing_game():

    secret_number = random.randrange(0, 101)
    # print(secret_number)
    my_input = int(input('enter a number: '))  # choose a number between 0 and 100
    if my_input > secret_number:
        print('high')
    elif my_input < secret_number:
        print('low')
    else:
        print('you just got it !')

guessing_game()

"""
in the above program, a function guessing_game() is defined and must be finally called to execute the program.
while randrange() from random module specifies the range of the number to be chosen.
if the user guss is below the secret number, that means its low, if 
the user guess is above, he/she got high. and if his/her guess matches the secret_number, then the user is right.
the single line comment above hides the secret_number from the user. 
"""

