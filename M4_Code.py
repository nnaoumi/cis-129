# M4 Making Decisions Assignment
# Author: Nicholas Naoumi

firstNum = int(input('Enter a number: '))
secondNum = int(input('Enter a second number: '))
thirdNum = int(input('Enter a third number: '))
print('\n')

if (firstNum + secondNum) == thirdNum :
    print('The sum of {} and {} is equal to {}.'.format(firstNum,secondNum,thirdNum))
elif (firstNum + thirdNum) == secondNum :
    print('The sum of {} and {} is equal to {}.'.format(firstNum,thirdNum,secondNum))
elif (secondNum + thirdNum) == firstNum :
    print('The sum of {} and {} is equal to {}.'.format(secondNum,thirdNum,firstNum))