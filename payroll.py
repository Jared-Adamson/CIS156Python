#Ch 4 Programming Assignment
#Jared Adamson
#Part B
# Uses if statments to process employee pay

print("Please enter the following:")
job = input("Job title (\"B\" for barista, \"M\" for maintenance, \"G\" for general staff)?")
numHours = int(input("Number of hours worked during the week?"))
numYear = int(input("Number of years employed at the restaurant?"))

#output their gross pay amount (i.e., the amount they earn before taxes and other deductions), based on the following:

#Baristas earn $5/hour for the first year year, then earn $6/hour
#Maintenance workers earn $12/hour for the first 2 years, then earn $13.50/hour
#General staff make $15/hour for the first year, then earn $18/hour

if job == "B":
    if numYear <= 1:
        print("Gross pay: $" + str((numHours * 5.0)))
    else:
        print("Gross pay: $" + str((numHours * 6.0)))
elif job == "M":
    if numYear <= 2:
        print("Gross pay: $" + str((numHours * 12.0)))
    else:
        print("Gross pay: $" + str((numHours * 13.5)))
elif job == "G":
    if numYear <= 1:
        print("Gross pay: $" + str((numHours * 15.0)))
    else:
        print("Gross pay: $" + str((numHours * 18.0)))
else:
    print("Invalid Entry")