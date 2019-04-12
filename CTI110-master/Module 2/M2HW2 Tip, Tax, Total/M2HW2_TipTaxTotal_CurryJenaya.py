#CTI-110
#M2HW2 - Tip Tax Total
#Jenaya Curry
#17 September 2017
#This program calculates the total cost (food costs, tip, and tax)of a restaurant meal.

#Asks user to enter charge for food.
food_cost = float (input ('What is the charge for your food?'))
# Defines variables for 18% tip and 7% tax.
tip = food_cost *.18
tax = food_cost *.07
# Subtotal before applied discount.
total = food_cost + tip + tax
#Asks user for coupon amount - i.e. $5 off, the user enters "5"
discount = float (input('Do you have a coupon? Enter your amount off. If none, enter "0"'))
#Calculates food costs, tip, tax, and discount into one amount.
balance_due = food_cost + tip + tax - discount

print ('FOOD $', format(food_cost, ',.2f'))
print ('TIP $', format(tip, ',.2f'))
print ('TAX $', format(tax, ',.2f'))
print ('SUBTOTAL $', format(total, ',.2f'))
print ('DISCOUNT -$', format(discount, ',.2f'))
print ('BALANCE DUE $', format(balance_due, ',.2f'))

