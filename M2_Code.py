# Wireless Bill Calculation Program

import random

# List of Modules
def fullName():
    fullName = input('Please enter your full name: ')
    print('\n')
    print('Hello', fullName , ', your wireless bill details are below: ')
    print('\n')

def billingAddress():
    print('Billing Address: ')
    print('12345 Street Dr. ')
    print('Anytown, MI 48353 \n')

def wirelessNum():
    print('Wireless Number: 248-539-2693 \n')

def dataCharges():
    gigabytesUsed = random.randint(1,5)
    dataCharges = gigabytesUsed * 10
    return dataCharges

def callingCharges():
    minutesUsed = random.randint(50,100)
    callingCharges = minutesUsed * 0.10
    return callingCharges

def textCharges():
    textsUsed = random.randint(200,400)
    textCharges = textsUsed * 0.02
    return textCharges

def govtFees():
    x = 6
    return x

def insuranceFee():
    x = 11
    return x

def discounts():
    x = 5
    return x

def dueDate():
    print('Due Date: \n June 1, 2019 \n')

def remitAddress():
    print('Please send payment to: \n PO BOX 5355 \n Anytown, MI 48353 \n')


# Wireless Bill Calculation

accountNum = input('Please enter your account number to view your wireless bill: ')

if accountNum is accountNum :
    fullName()
    billingAddress()
    wirelessNum()
else :
    print('nothing...')

dataMessage = 'Data Fees:'
callingMessage = 'Phone Call Fees:'
textMessage = 'Text Messaging Fees:'
govtMessage = 'Government Fees:'
insuranceMessage = 'Insurance Fee:'
discountMessage = 'Wireless Discount:'

print( dataMessage, dataCharges() )
print( callingMessage, callingCharges() )
print( textMessage, textCharges() )
print( govtMessage, govtFees() )
print( insuranceMessage, insuranceFee() )
print( discountMessage, '-', discounts() )
print('\n')

print( 'Balance Due:', dataCharges() + callingCharges() + textCharges() + govtFees() + insuranceFee() - discounts() )
print('\n')

dueDate()
remitAddress()