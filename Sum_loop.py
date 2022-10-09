#Ch 5 Programming Assignment
#Jared Adamson
#Part A
# Asks the user for a starting number and an ending number. 
# Then uses a loop to calculate the sum of every number from the first to the second.

print("Calculate the sum of every number from a starting number to an ending number.")
numStart = int(input("Enter your starting number: \n"))
numEnd = int(input("Enter your ending number: \n"))
sum = 0

if numStart > numEnd:
    x = numStart
    numStart = numEnd
    numEnd = x

numCount = numStart

while numCount <= numEnd:
    sum = sum + numCount
    numCount += 1

print("The sum of all numbers from ", numStart, " to ",  numEnd,  " is ", sum)
