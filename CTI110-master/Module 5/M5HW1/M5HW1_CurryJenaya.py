#CTI 110
#M5HW1 - Distance Traveled
#Jenaya Curry
#16 October 2017
#This program displays the distance the vehicle has traveled each hour
#based on user speed and time period input.

def main ():
    SPEED = int(input('What is the speed of the vehicle in mph? '))
    HOURS = int(input('How many hours has it traveled? '))
    print('Hour','\tDistance Traveled' )
    print('----------------------------')
    for currentHour in range(1, HOURS + 1):
         distanceTraveled = SPEED * currentHour
         print(currentHour,'\t',distanceTraveled)
         

main ()       

