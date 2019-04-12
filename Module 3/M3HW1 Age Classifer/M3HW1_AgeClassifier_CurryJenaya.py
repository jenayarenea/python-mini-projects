#CTI-110
#M3HW1 - Age Classifier
#Jenaya Curry
#30 September 2017
#This program will classify a person's age based on user input.

def main():
    
    Adult = 20
    Teenager = 13
    Child = 1

    
    personName = input('Enter the person\'s name: ')
    print (personName)

    personAge = int(input('Enter {}\'s age: ' .format(personName)))
    print (personAge)

    if personAge >= Adult:
        print('{} is an adult.' .format(personName))
    elif personAge >= Teenager:
        print('{} is a teenager.'.format(personName))

    elif personAge > Child:
        print('{} is a child.'.format(personName))
    else:
        print('{} is an infant.'.format(personName))
main()
main()
main()
main()
