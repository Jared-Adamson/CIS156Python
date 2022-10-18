#Ch 6 Programming Assignment
#Jared Adamson
#Part B
# Program to calculate shipping price

"""
Part B
Create a program called shipping_price.py that calculates the shipping price for a purchase. 
Use a prompt to get (from the user) the number of items and the total weight of the package (in pounds). 
Then pass that data to a user-defined function that accepts both values as parameters and returns (not outputs)
a shipping price based on the following guidelines:

Less than 3 items and less than one pound: $5.00 shipping charge.
Less than 3 items and one pound or over: $7.50 shipping charge.
3 to 5 items and less than two pounds: $8.50 shipping charge.
Anything else: $10.00 shipping charge.
Display this returned value for the user.
"""

def shipPrice(quant, weight):

    if quant < 3 and weight < 1:
        cost = 5.00
    elif quant < 3 and weight >= 1:
        cost = 7.50
    elif (quant >= 3 and quant <= 5) and weight < 2.0:
        cost = 8.50
    else:
        cost = 10.00
    
    return cost

print("Please enter the number of items and the total weight of the package (in pounds). ")
i = int(input("Number of Items: "))
w = float(input("Weight of package: "))


print(f"The cost to ship your package is: ${shipPrice(i, w):.2f}")
