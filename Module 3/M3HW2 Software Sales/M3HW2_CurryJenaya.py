#CTI 110
#M3HW2
#Jenaya Curry
#3 October 2017
#Software Sales

def main():
    discount10 = 10
    discount20 = 20
    discount30 = 50
    discount40 = 100
    packageQuantity = float(input('Enter the number of packages purchased: '))

    if packageQuantity >= discount40:
      discount = .40
    elif packageQuantity >= discount30:
      discount = .30
    elif packageQuantity >= discount20:
      discount = .20
    elif packageQuantity >= discount10:
      discount = .10
    else:
      print('You do not qualify for a discount.')
      discount = 0
    subtotal = (packageQuantity * 99)
    discountTotal = subtotal * discount
    purchaseCost = (subtotal) - (discount * subtotal)
    print ('SUBTOTAL:$',format(subtotal,'.2f'))
    print ('DISCOUNT:$',format(discountTotal,'.2f'))
    print ('TOTAL COST:$',format(purchaseCost,'.2f'))
main()
main()
main()
main()
main()
