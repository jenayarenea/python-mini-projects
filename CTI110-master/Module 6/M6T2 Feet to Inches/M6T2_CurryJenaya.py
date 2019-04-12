#CTI 110
#M6T2 Feet to Inches
#Jenaya Curry
#16 November 2017
#This program converts feet to inches.

#Defines a constant for the number of inches per foot.
INFOOT = 12

# main function
def main():
    # Get a number of feet from the user.
    feet = float(input('Enter the number of feet: '))

    # Convert this to inches
    print(feet, ' feet equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INFOOT

# Call the main function.
main()
main()
main()
