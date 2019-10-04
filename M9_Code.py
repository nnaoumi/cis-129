# M9 Assignment
# Author: Nicholas Naoumi

# Modules
def birthDate() :
    birthYear = input('Please enter the year you were born in YYYY format: ')
    birthMonth = input('Please enter the month you were born in MM format: ')
    
    return int(birthYear), int(birthMonth)

def ageCalculation(bornYear, bornMonth) :
    from datetime import datetime
    
    currentDate = datetime.today()
    currentYear = currentDate.year
    currentMonth = currentDate.month

    ageInYears = currentYear - bornYear
    ageInMonths = currentMonth - bornMonth

    # This conditional is written to remove the negative sign if the difference in months results in a negative number.
    if ageInMonths < 0 :
        ageInMonths = ageInMonths * -1

    return ageInYears, ageInMonths


# Main Program
birthYear, birthMonth = birthDate()
ageInYears, ageInMonths = ageCalculation(birthYear, birthMonth)

print( 'You are {} years and {} months old!'.format(ageInYears,ageInMonths) )