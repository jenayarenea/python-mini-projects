#CTI 110
#Bonus Project
#Jenaya Curry
#19 September 2017 (Finished 28 September 2017): 9 days to complete.
#This program displays descriptions based on the category of user input hurricane.

def main():
    print('Welcome to an interactive Saffir-Simpson Scale. Begin below!')
    hurricaneName = input('What is the name of the hurricane? ')
    print(hurricaneName)
    hurricaneCategory = int(input('Which category is hurricane {}? '.format(hurricaneName)))
    if hurricaneCategory == 1 or hurricaneCategory == 2 or hurricaneCategory == 3 or hurricaneCategory == 4 or hurricaneCategory == 5  :
        print(hurricaneCategory)
    else:
        print('Invalid value. Hurricane category must be a number 1-5. Please\n\
    re-enter your answer.')
        hurricaneCategory = int(input('Which category is hurricane {}? '.format(hurricaneName)))
        print(hurricaneCategory) 

    areYouSure =input('Are you sure that {} is a category {} hurricane? '.format(hurricaneName,hurricaneCategory))
    if areYouSure == 'yes' or areYouSure == 'yea' or areYouSure == 'YES':
        print('Ok. Here are your results:')

    else:
        print('Then please re-enter your answer.')
        hurricaneCategory = int(input('Which category is hurricane {}? '.format(hurricaneName)))
        print(hurricaneCategory)  
    if hurricaneCategory == 1:
        print('Hurricane {} is a category {} storm.'.format(hurricaneName,hurricaneCategory)) 
        print('Winds: 74-95 mph')
        print('Winds Effects: damage to mobile homes and some homes of frame\n\
              construction. Numerous trees down and widespread power outages.\n\
              Roads blocked due to downed trees and power lines. Loose outdoor\n\
              items will become airborne projectiles. For example, an area as\n\
              large as a county could experience near total power loss.')
        
    elif hurricaneCategory == 2:
        print('Hurricane {} is a category {} storm.'.format(hurricaneName,hurricaneCategory)) 
        print('Winds: 96-110 mph')
        print('Winds Effects: severe damage to the majority of mobile homes and\n\
              homes of frame construction. Many trees down. Well-constructed homes\n\
              will have damage to shingles, siding and gutters. Extensive damage\n\
              to power lines and widespread power outages. Airborne debris could\n\
              injure or kill. Damage could extend well inland. For example,\n\
              multiple localities could experience near total loss of power\n\
              and water for several days.')
    elif hurricaneCategory == 3:
        print('Hurricane {} is a category {} storm.'.format(hurricaneName,hurricaneCategory))
        print('Winds:111-130 mph')
        print('Wind Effects: nearly all mobile homes destroyed. Severe damage to\n\
              most homes,including structural collapse. Airborne debris will\n\
              injure or kill. Severe damage to most low-rise apartment buildings\n\
              with partial roof and wall failure. Damage could extend well inland.\n\
              For example, large portions of the affected area could experience\n\
              total power and waer loss for more than a week.')
    elif hurricaneCategory == 4:
        print('Hurricane {} is a category {} storm.'.format(hurricaneName,hurricaneCategory)) 
        print('Winds: 131-155 mph')
        print('Wind Effects: catastrophic damage to residential structures. Most of\n\
        the affected area will be uninhabitable for weeks or longer. Nearly all\n\
        industrial buildings and low-rise apartment buildings severely damaged\n\
        or destroyed. Nearly all trees and power poles downed. Damage could extend\n\
        well inland. For example, large portions of the affected area will\n\
        experience total power and water loss for weeks and possibly months.')

    elif hurricaneCategory == 5:
        print('Hurricane {} is a category {} storm.'.format(hurricaneName,hurricaneCategory))
        print('Winds: 156+ mph')
        print('Wind Effects: similar to Category 4.')
        printCategory4=input('Would you like to see the effects of Category 4 winds?')
        if printCategory4 == 'yes' or printCategory4 =='yea' or printCategory4 == 'yep' or printCategory4 == 'YES':
              print('Wind Effects: catastrophic damage to residential structures.\n\
     Most of the affected area will be uninhabitable for weeks or\n\
     longer. Nearly all industrial buildings and low-rise apartment\n\
     buildings severely damaged or destroyed.Nearly all trees and\n\
     power poles downed.Damage could extend well inland. For example,\n\
     large portions of the affected area will experience total power\n\
     and water loss for weeks and possibly months.')
        else:
              print('Ok. Category 4 effects will not be shown.')

    print ("Source: A Category 1-5 hurricane: It's all about the wind - Press of Atlantic\n\
      City")
#program start
main()
main()
main()
main()
main()
