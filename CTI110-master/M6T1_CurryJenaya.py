#CTI 110
#M6T1 Kilometers to Miles
#Jenaya Curry
#16 November 2017
#This program converts kilometers to miles.

#Define a variable for the conversion factor.
CFACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.  

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers:'))

    #Display the distance converted to miles.
    show_miles(kilometers)
    
# The show_miles function converts the parameter km from
#kilometers to miles and displays the result

def show_miles(km):
    #Calculate miles
    miles = km * CFACTOR

    #Display the miles.
    print(km, 'kilometers equals', format(miles, ',.2f'),'miles.')

# Call the main the function.
main()
main()
main()
    
