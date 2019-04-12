#CTI 110
#M6HW2 Guessing Game
#Jenaya Curry
#29 November 2017
#This program creates a random number guessing game.

def main():
    playGame()
    playAgain = input('Do you want to play again? Enter y to keep playing.')
    while playAgain == 'y':
      main()
    else:
      print('Ok. Thanks for playing!')
def playGame():
    import random

    randomNumber = random.randint(1,100)
    numberGuess = int(input('Pick a whole digit number from 1-100. \
     Enter 0 to quit.'))
    while guessesTaken != 0:
         if numberGuess == randomNumber:
            print ('Congratulations! You guessed correctly!')
            break
         elif numberGuess < randomNumber:
            print ('Too Low!')
         elif numberGuess > randomNumber:
            print ('Too High!')
            
main()
