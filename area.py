# Author: Mark Hudak
# Email: hudakm@miamioh.edu
# Section: 00
# Date: 05/29/2020

'''
Purpose: to find the area of a rectangle, given the length
    and the width of the rectangle
Inputs:
    User supplies the length and the width of the rectangle as numbers
Outputs:
    User greeted and prompted for input of the two dimensions
    Recangle area will be displayed
'''
print("The Area of a Rectangle")
print()
length = int(input("Enter length of rectangle: "))
width  = int(input("Enter width of rectangle: "))
area = int(length * width)    
print()
print("The area of a rectangle with length ",length , "and width ", width , "is: ", area)  
