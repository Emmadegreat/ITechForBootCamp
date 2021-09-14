name = 'emmanuel mkpurunchi f'
title = 'hangman game assignment '
print(f'Name: {name.upper()}. \n Title: {title.upper()}. \n')

import time
def hang_man():

    name = input('what is your name: ')
    print("hello ! " + name.upper() + ", let's play hangman game")

    time.sleep(1)  # the system will pause for 1 second after welcoming the user.
    print("start playing ...")
    time.sleep(0.2)  # time range it will pause before the game will start
    word = 'school'
    guesses = ''
    turns = 10

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print('you won')
            break

        guess = input('guess a character: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('you guessed wrong')
            print('you have only ', + turns, 'left ')

            if turns == 0:
                print('you lost')

hang_man()
