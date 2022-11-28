#Ch 10 Programming Assignment
#Jared Adamson
#Part B
# Prints letter grade from grade percentage.

'''
Create a program called letter_grade.py that asks the user to input their current grade percentage and then outputs the corresponding letter grade (A through F).

Within a try-except structure raise (not just catch) two different exceptions: one if the user inputs a grade of less than zero and a different exception if the user 
inputs a grade greater than 100. Be sure to also handle input that is not a number.

Note that you can use a ValueError (as described in zyBooks 10.3) and do not need to create a custom exception (as described in 10.6).

'''

try:
    pCent = float(input('Please enter your current grade percentage:'))
    try:
    
        if (pCent < 0):
            raise ValueError('Invalid input.  Your grade percentage must be a positive number.')
        if (pCent > 100):
            raise ValueError('Invalid input.  Your grade percentage may not be greater than 100.')    

        grade = 'A' if pCent >= 90 \
            else 'B' if pCent >= 80 \
            else 'C' if pCent >= 70 \
            else 'D' if pCent >= 60 \
            else 'F'
       
        print('Your letter grade is: ', grade)
    
    except ValueError as excpt:
        print(excpt)
except ValueError:
    print('Invalid input. Be sure to enter a number.')

