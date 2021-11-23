#Author: Mark Hudak
#Email: hudakm@miamioh.edu
#Section: CSE 102 
#Date: 05/29/2020
'''
Purpose: to find the area of a rectangle, given the length
    and width of the rectangle
Inputs:
    User supplies the length and the width of the rectangle as numbers
Outputs:
    User greeted and prompted for input of the two dimensions
    Rectangle area will be displayed
'''

print('The Area of a Rectangle')
print()
length = int(input("Enter length of rectangle: "))
width = int(input('Enter width of rectangle: '))
area = length * width
print()
print('The are of a rectangle with length ',length ,'and width ',width ,'is: ',area)
