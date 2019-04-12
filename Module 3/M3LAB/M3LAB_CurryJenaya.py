# CTI 110
#M3LAB
#Jenaya Curry
#28 September 2017
# This program takes a number grade and outputs a letter grade.


 
def mainElif():
    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    score = float(input('Enter grade: '))

    if score >= A_score:
      print('Your grade is: A. Excellent!')
    elif score >= B_score:
      print('Your grade is: B. Good!') 
    elif score >= C_score:
      print('Your grade is: C. Keep Going!')
    elif score >= D_score:
      print('Your grade is: D. You can do better. Grow up.')
    else:
      print('Your grade is: F. Get Your Life Together. Seriously.')
'''
def mainNested():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    score = float(input('Enter grade: '))

    if score >= A_score:
      print('Your grade is: A. Excellent!')
    else:
     if score >= B_score:
      print('Your grade is: B. Good!')
     else:
       if score >= C_score:
        print('Your grade is: C. Keep Going!')
       else:
         if score >= D_score:
           print('Your grade is: D. You can do better. Grow up.')
         else:
           print('Your grade is: F. Get Your Life Together. Seriously.')
'''
def mainRounded():
 #Takes in account grades that round up   
    A_score = 89.5
    B_score = 79.5
    C_score = 69.5
    D_score = 59.5

    score = float(input('Enter grade: '))

    if score >= A_score:
      print('Your grade is: A. Excellent!')
    elif score >= B_score:
      print('Your grade is: B. Good!') 
    elif score >= C_score:
      print('Your grade is: C. Keep Going!')
    elif score >= D_score:
      print('Your grade is: D. You can do better. Grow up.')
    else:
      print('Your grade is: F. Get Your Life Together. Seriously.')
# program start

print ('Welcome to the letter grading scale!')
roundYes = input ('Would you like to round your grades? Enter \'yes\' or \'no\'.\n\
For example, 89.6 will still be considered an \'A\'. ')

if roundYes =='yes':
    mainRounded()
    mainRounded()
    mainRounded()
    mainRounded()
    mainRounded()
 
else:
    mainElif()
    mainElif()
    mainElif()
    mainElif()
    mainElif()
'''
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
'''
