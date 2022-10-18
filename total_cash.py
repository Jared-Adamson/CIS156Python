#Ch 6 Programming Assignment
#Jared Adamson
#Part A
# Program to count the amount of monies in a wallet.

""" 
Part A
Create a program called total_cash.py that determines the total value of a wallet full of cash. 
It should ask the user to input the quantity of each denomination of bills (ones, fives, etc--up to hundreds). 
It should then call a function that accepts each of those values as arguments/parameters and returns 
(not prints!) the total amount of the cash. Finally, you should output the total value for the user to see.
For example, if a user has 3 ones, 3 tens, and 1 fifty, their total is $83 in cash.
""" 

cashDict = {
    "Ones" : 0,
    "Fives" : 0,
    "Tens" : 0,
    "Twenties" : 0,
    "Fifties" : 0,
    "Hundreds" : 0
    }

print("Input the quantity of each denomination of bills in your wallet. \n Ones: ", end = "")
o = int(input())
fv = int(input("Fives: "))
tn = int(input("Tens: "))
tw = int(input("Twenties: "))
fif = int(input("Fifties: "))
h = int(input("Hundreds: "))


def cashFunc(o, fv, tn, tw, fif, h):

    global cashDict

    cashDict["Ones"] = o*1
    cashDict["Fives"] = fv*5
    cashDict["Tens"] = tn*10
    cashDict["Twenties"] = tw*20
    cashDict["Fifties"] = fif*50
    cashDict["Hundreds"] = o*100

    val = cashDict.values()

    total = sum(val)

    return  total

print(f" Your wallet has a total of ${cashFunc(o, fv, tn, tw, fif, h)} in cash.")