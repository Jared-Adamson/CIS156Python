#Ch 8 Programming Assignment
#Jared Adamson
#Part B
# 

'''
Part B
Create a program called courses.py that has a dictionary with 7 course names (for example: CIS105, ENG101, etc), 
along with the name of each associated instructor.

The list of courses that your program will accept needs to presented to the user. (Otherwise how will they know
 what to look for?)
Prompt the user for the name of a course to look up, or the word "quit" to exit.
After the user types in a course, it should look up and print that course's instructor.
The program should repeat this until the user enters "quit" at the prompt.
Note: The program does NOT need to gracefully handle the error that may occur if the course is not found in
 the dictionary; for now, your program only needs to work when a course is entered correctly.
'''

classDict = {
  "CPI101": "Ford",
  "CSE205": "Harris",
  "CSE310": "Palmer",
  "ENG101": "Guru",
  "MAT210": "Pennington",
  "CIS105": "Fett",
  "CSE350": "Jango",
}

print('These are the available courses:')
for x in classDict:
  print(x)

lookUp = ''

while lookUp != 'quit':
    lookUp = input('Please enter a course to look up the instructor, or the word "quit" to exit:')
    if lookUp != 'quit':
        print(f'Instructors Name: ', classDict[lookUp])
