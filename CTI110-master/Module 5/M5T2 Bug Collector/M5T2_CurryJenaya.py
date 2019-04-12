#CTI 110
#M5T2 - Bug collector
#Jenaya Curry
#10 October 2017
#This program records the amount of bugs collected everyday for seven days.

def main():
    # Initialize the accumulator.
    bugTotal = 0

    # Get the bugs collected for each day.
    for day in range (1,8):
        #Prompt the user
        print('How many bugs did you collect on day', day)

        #Input the number of bugs.
        bugsCollected = int(input())

        #Add bugs to total
        bugTotal += bugsCollected
        
    # Display the total bugs.
    print ('You collected a total of', bugTotal,'bugs.')
main()
    
