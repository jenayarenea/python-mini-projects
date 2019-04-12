#CTI 110
#M6HW1 Test Averages
#Jenaya Curry
#16 November 2017
#This program takes 5 test scores and calculates the average and displays a
#letter grade.

#Ask the user for 5 test scores.
def scoreInput():
     scoreOne = float(input('Enter score 1: '))

     scoreTwo = float(input('Enter score 2: '))
     
     scoreThree = float(input('Enter score 3: '))
     
     scoreFour = float(input('Enter score 4: '))
     
     scoreFive = float(input('Enter score 5: '))
    

     return scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive
          
     
def calcAverage(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive):
    scoreAverage = (scoreOne + scoreTwo + scoreThree + scoreFour + scoreFive)/5

    return scoreAverage
  
def determineGrade(scoreAverage):
        # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60


    if scoreAverage >= A_score:
      return 'Your grade is: A. Excellent!'
    elif scoreAverage >= B_score:
      return 'Your grade is: B. Good!' 
    elif scoreAverage >= C_score:
      return 'Your grade is: C. Keep Going!'
    elif scoreAverage >= D_score:
      return 'Your grade is: D. You can do better. Grow up.'
    else:
      return 'Your grade is: F. Get Your Life Together. Seriously.'
def display(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive):
     print('Score\tLetter Grade')
     print( "Your average is", calcAverage( scoreOne, scoreTwo, scoreThree, scoreFour,\
     scoreFive ) )
     print( str(scoreOne) + '\t' + determineGrade(scoreOne))
     print( str(scoreTwo) + '\t' + determineGrade(scoreTwo))
     print( str(scoreThree)+ '\t' + determineGrade(scoreThree))
     print( str(scoreFour)+ '\t' + determineGrade(scoreFour))
     print(str(scoreFive)+ '\t' + determineGrade(scoreFive))

def main():
     scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive, = scoreInput()
     display(scoreOne,scoreTwo,scoreThree,scoreFour,scoreFive)
     
#call the main function
main()


