#Ch 5 Programming Assignment
#Jared Adamson
#Part B
#Prompts the user to input their age in years

numAge = int(input("Enter your age in years: \n"))

while numAge <= 0 or numAge >= 100:
    print("Invalid input.  Please try again.")
    numAge = int(input("Enter your age in years: \n"))

print("Thank you")