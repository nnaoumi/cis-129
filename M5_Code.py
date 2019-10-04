# M5 Assignment Code - Homestead Furniture Store
# Author: Nicholas Naoumi

print('Homestead Furniture Store \n Monthly Payment Calculator \n')

acctNum = input('Please enter an account number: ')

while acctNum != 'quit' :
    custName = input('Enter the name of the customer: ')
    itemPrice = int(input('Enter the purchase price of the item: '))
    month = 1

    print('\n')
    print('Customer Name: ', custName)
    print('Account Number: ' , acctNum)

    while month < 13 :
        print('Payment {} Amount: $'.format(month), itemPrice / 12)
        month = month + 1

    acctNum = input('\n Please enter another account number, for type quit to exit this program: ')
    print('\n')