#Ch 7 Programming Assignment
#Jared Adamson
#Part B
#Formates a sports team name.

"""
Create a program that accepts a the name of a sports team--including city--and then convert it to all 
uppercase with underscore characters in place of any spaces; output the result. Be sure to give the user 
adequate instructions for using the program. Name the file str_modifier.py.

Sample Program Run:
Enter your full name: New York Yankees
The new version of this name is NEW_YORK_YANKEES
"""

team = input("Please the name of a sports team including the city:")

team = team.upper()
splt = team.split(' ')
team = '_'.join(splt)

print("The new version of this name is ", team)
