#Ch 8 Programming Assignment
#Jared Adamson
#Part A
# Creates a grocery list for shopping at the market.

'''
Part A
Create a program called grocery_list.py that allows the user to input a list of items to buy at the supermarket. 
It should begin by asking the user to input the number of items to add to the list. Then, it should use a loop
 to prompt the user to input that many items, storing each in the list.

After the items have been entered, it should output the full list.
'''

gList = []

numTime = int(input('How many items would you like to add?'))

for x in range(numTime):
    addItem = input('What item would you like to add?')
    gList.append(addItem)

print(gList)