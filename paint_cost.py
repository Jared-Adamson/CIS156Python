#Ch 10 Programming Assignment
#Jared Adamson
#Part A
# Prints area and cost to paint a wall.

'''
Create a program called paint_cost.py that prompts the user to input the height of a wall (in feet), the width of the wall (in feet), and the cost of the paint used to cover it. 
Output the area of the wall (height x width) and the cost per square foot (cost / area).

Use try and at least two except statements to handle issues that arise if the user does not input numbers or enters zero as the area, outputting a relevant message for each issue.

'''

try:
    wHeight = abs(float(input("Input the height of a wall (in feet)")))
    wWidth = abs(float(input("Input the width of the wall (in feet):")))
    wCost = abs(float(input("Enter the cost of your paint:")))
    wArea = wHeight * wWidth
    sqftCost = wCost / wArea
    print('Wall Area: ', + wArea, '  Cost per square foot: ', + sqftCost)
except ZeroDivisionError:
        print('0 is not a valid entry.')
except:
    print('Invalid input, unable to compute.')
