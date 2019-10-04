# Number Guessing Program

import random

prompt = 'I am thinking of a number. Please guess a number from 1 to 100: \n'
x = random.randint(1,100)
y = int(input(prompt))

while x is not y :
    if y > x :
        print('You guessed too high, please try again. \n')
        y = int(input(prompt))
    elif y < x :
        print('You guessed too low, please try again. \n')
        y = int(input(prompt))

print('You guessed', x, 'good job!')