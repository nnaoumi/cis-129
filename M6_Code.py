# M6 Assignment - Arrays
# Author: Nicholas Naoumi

commonPWD = ['123456','123456789','qwerty','password','111111','12345678','abc123','1234567','password1','12345']

userPWD = input('Please enter a password: ')

while userPWD in commonPWD :
    print('Error: You chose a common password \n')
    userPWD = input('Please enter another password: ')

print('\n Your password has been accepted')