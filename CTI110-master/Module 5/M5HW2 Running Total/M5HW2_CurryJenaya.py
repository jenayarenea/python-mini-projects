#CTI 110
#M5HW2 - Running Total
#Jenaya Curry
#16 October 2017
#Takes user input of grades, calculates the average, and displays a letter grade.

def main ():
    total = 0
    numberInput = float(input('Enter a number? '))

    while numberInput > -1:
        total = total + numberInput
        numberInput = float(input('Enter a number? '))
    print ('Total: ',total)
main ()
