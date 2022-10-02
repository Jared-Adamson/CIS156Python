#Ch 4 Programming Assignment
#Jared Adamson
#Part A
# Uses if statments to help customer choose a plan.

print("Please enter the following:")
poolDepth = int(input("Pool depth?"))
cPerMonth = int(input("Number of cleaning visits per month?"))
dcPerYear = int(input("Number of \"deep cleaning\" visits per year?"))

#Based on the input, use branching to recommend appropriate service plan options:

#A customer with a pool depth of 5 feet or less, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan A at $44 per month.
#A customer with a pool depth of 5 feet or less, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan B at $54 per month.
#A customer with a pool depth of more than 5 feet, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan C at $58 per month.
#A customer with a pool depth of more than 5 feet, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan D at $64 per month.

if (poolDepth <= 5) and ( cPerMonth < 4) and (dcPerYear < 3):
    print("You should choose Plan A at $44 per month") 
elif (poolDepth <= 5) and (( cPerMonth >= 4) or (dcPerYear >= 3)):
    print("You should choose Plan B at $54 per month") 
elif (poolDepth > 5) and ( cPerMonth < 4) and (dcPerYear < 3):
    print("You should choose Plan C at $58 per month") 
else :
    print("You should choose Plan D at $64 per month") 