# Author: Mark Hudak
# Date: 05/30/2020
# Section: CSE 102
# Email: hudakm@miamioh.edu

print('Change Calculator') # Descriptor of program

# Requesting input of price from the cashier in cents
price = 100 * float(input('Enter the price of the item bought: '))

# Requesting input of amount of money given to the cashier in cents
pay = 100 * float(input('Enter the amount of money you give the cashier: '))

# Calculating total change in cents
change = pay - price

# Initializing variables with an equation attached to each variable to give proper return
# Equations build upon previous variables
# Works for desired use; would not produce a desirable result if one tried to use program
# in such a manner that would result with input of price being > than the money given to the cashier
dollars = int(change//100)
quarters = int((change - (dollars*100))//25)
dimes = int((((change - dollars*100) - quarters*25)//10))
nickles = int(((((change - dollars*100) - quarters*25) - dimes*10)//5))
pennies = int(((((change - dollars*100) - quarters*25) - dimes*10) - nickles*5))

# Printing results
print('Your change')
print('     dollars:     ', dollars)
print('     quarters:    ', quarters)
print('     dimes:       ', dimes)
print('     nickles:     ', nickles)
print('     pennies:     ', pennies)
print('Thank you for your business.')

