#CTI 110
#M3HW2
#Jenaya Curry
#3 October 2017
#Software Sales

def main():
    packageQuantity = float(input('Enter the number of packages purchased: '))
    if packageQuantity >=10:
        discount = .10
    elif packageQuantity >= 20:
        discount = .20
    elif packageQuantity >= 50:
        discount = .30
    elif packageQuantity >= 100:
        discount = .40
    elif packageQuantity <10:
        discount = 0
        print('You do not qualify for a discount.')

    subtotal = (packageQuantity * 99)
    purchaseCost = (subtotal) - (discount * subtotal)
    print ('SUBTOTAL:$',format(subtotal,'.2f'))
    print ('TOTAL COST:$',format(purchaseCost,'.2f'))
main()
main()
main()
main()
main()
