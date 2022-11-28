#Ch 12 Programming Assignment
#Jared Adamson
#Part A
# Reads a file.  Prints text from file. 

'''
Create a program called read_file.py that reads the address.txt file. Then, prompt the user to enter a line number (1 through 12), and display that line from the file. 
Keep repeating until the user decides to exit.
'''

myFile = open ('address.txt')

fContent = myFile.readlines()

userContinue = 'Y'

while userContinue == 'Y':

    lineRead = int(input('Enter the file line you wish to have read(1 thru 12):'))

    lineRead -= 1

    print(fContent[lineRead])

    userContinue = input('Would you line to read a diffrent line(Y for Yes N for No:').upper()

    

