#Ch 12 Programming Assignment
#Jared Adamson
#Part B
# Reads a file.

'''
Create a program called envelope.py that prompts the user to input the following, storing each in a separate variable:

Recipient's name
Address
City
State
Zip Code
Then, the program should create a new file called envelope.txt and write the data into it data that creates the envelope: 
Your name and return address at the top-left followed by the recipient's name and address near the middle, as seen below. 
Make sure to close the file after finished writing to it.

Display the envelope after it is created.

Sample output file:
Jose Pena
123 Main St.
Avondale, AZ 85392


          Yuri Davidson
          456 Pine Ave
          Litchfield Park, AZ 85393
'''
varEnvelope = open('envelope.txt', 'w')

varName = input('Enter recipient\'s Name:')
varAddress = input('Enter recipient\'s Street Address:')
varCity = input('Enter recipient\'s City:')
varState = input('Enter recipient\'s State:')
varZip = input('Enter recipient\'s Zip Code:')

#writing my address info.
varEnvelope.write('Jared Adamson')
varEnvelope.write('\n')
varEnvelope.write('18765 New Address')
varEnvelope.write('\n')
varEnvelope.write('Mesa, AZ 85676')
varEnvelope.write('\n')
varEnvelope.write('\n')

#Writing inputed address info to file.
varEnvelope.write(' ' * 10 + varName)
varEnvelope.write('\n')
varEnvelope.write(' ' * 10 + varAddress)
varEnvelope.write('\n')
varEnvelope.write(' ' * 10 + f'{varCity}, {varState} {varZip}')


varEnvelope.close()


#Printing envelope contents.  

myFile = open ('envelope.txt', 'r')

for x in myFile:
    print(x, end ='')