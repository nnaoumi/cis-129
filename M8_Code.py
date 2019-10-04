# M8 Assignment - Professor Zak
# Author - Nicholas Naoumi

# Declarations
quizScores = []
quizElement = 0
quizNum = 1
totalScore = 0

studentName = input('Please enter a student name: ')

# Loop for entering scores of the 10 quizzes
while quizNum < 11 :
    quizScores.append( int( input('Enter Quiz {} Score: '.format(quizNum) ) ) )
    
    while quizScores[quizElement] > 100 :
        quizScores[quizElement] = int( input('Please enter a score from 0 to 100 for Quiz {}: '.format(quizNum) ) )

    quizElement = quizElement + 1
    quizNum = quizNum + 1

quizScores.sort()

# Loop for adding up the six highest test scores
for i in quizScores[4:] :
    totalScore = totalScore + i

print('\n')
print('{}\'s total points for their six highest quiz scores is: '.format(studentName), totalScore)
print('\n')


print("""Note to professor:

If you would like to check my math,
listed below are the array elements for the 10 quiz scores
sorted in ascending order.  

""")

print(quizScores)