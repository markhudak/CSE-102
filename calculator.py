## Mark Hudak
## CSE102 summer 2020
## 06/08/2020
## This program provides basic mathematical operations for a user to use.
## Provides a display menu for the user to select what operation and then
## allows user to input two numbers. Make sure to input numbers in correct
## order. This calculator can provide decimals to the hundreth position.
## Be mindful that the output may not be entirely accurate(rounded)  due to use
## of the float function to provide decimal availability.

## printing user select menu
print('Select operation.')
print('      1.Add')
print('      2.Subtract')
print('      3.Multiply')
print('      4.Divide')

##initializing variables based off user input
operation = int(input('Enter your choice (1/2/3/4): '))
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

## if/else series to provide direction based off which operator
## was selected with correct opertations with the user input to
## achieve desirable results. Made use of float() to allow a 
## broader use of numbers.
if operation == 1:
    ans = float(num1 + num2)
    print('%.2f + %.2f = %.2f'%(num1, num2, ans))

elif operation == 2:
    ans = float(num1 - num2)
    print('%.2f - %.2f = %.2f'%(num1, num2, ans))

elif operation == 3:
    ans = float(num1 * num2)
    print('%.2f * %.2f = %.2f'%(num1, num2, ans))

elif operation == 4:
    ans = float(num1 / num2)
    print('%.2f / %.2f = %.2f'%(num1, num2, ans))
else:
    print('Invalid input!')


