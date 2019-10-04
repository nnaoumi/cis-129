# M10 Assignment
# Author: Nicholas Naoumi

class AutomobileLoan:
    loanNumber = 0
    vehicleMake = 0
    vehicleModel = 0
    loanBalance = 0

    def loan_number(self):
        self.loanNumber = input('Enter loan number: ')

    def vehicle_make(self):
        self.vehicleMake = input('Enter the vehicle\'s make: ')
    
    def vehicle_model(self):
        self.vehicleModel = input('Enter the vehicle\'s model: ')
    
    def loan_balance(self):
        self.loanBalance = input('Enter the loan balance: ')
    
    def display_loan_info(self):
        print('\n')
        print('Loan Information is listed below: ')
        print('\n')
        print('Loan Number:', self.loanNumber)
        print('Vehicle Make:',self.vehicleMake)
        print('Vehicle Model:',self.vehicleModel)
        print( 'Loan Balance: ${} '.format(self.loanBalance) )


x = AutomobileLoan()
x.loan_number()
x.vehicle_make()
x.vehicle_model()
x.loan_balance()
x.display_loan_info()