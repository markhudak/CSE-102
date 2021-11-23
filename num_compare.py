## Mark Hudak
## 06/09/2020
## CSE102 Summer
## This program will take user input and compare
## two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1>num2:
    print('The number %d is greater than %d'% (num1, num2))
elif num2>num1:
    print('The number %d is greater than %d'% (num2, num1))
else:
    print('The number %d is equal to  %d'% (num1, num2))
