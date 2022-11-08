
#Ch 8 Programming Assignment
#Jared Adamson
#Part A
# Tracks items in an online store.

'''
Directions
Create a program called shopping_cart.py that uses a class and objects to track a couple of items for purchase from an online store. There are three steps/sections to this program:

(1) Create the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()
Example of print_item_cost() output:

Bottled Water 10 @ $1.25 = $12.5
(2) In the main section of your code (not in the class definition), prompt the user for two items and create two objects of the ItemToPurchase class. 

Example of a program run after step 2:

Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3.50
Enter the item quantity:
1

Item 2
Enter the item name:
Bottled Water
Enter the item price:
1.25
Enter the item quantity:
10

(3) Add the costs of the two items together and output the total cost.

Example of output from additional code in step 3:

TOTAL COST
Chocolate Chips 1 @ $3.5 = $3.5
Bottled Water 10 @ $1.25 = $12.5

Total: $15.5

'''

class ItemToPurchase:
    
    #item_name, item_price, item_quantity
    
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = float(item_price) 
        self.item_quantity = int(item_quantity)
    
    def print_item_cost(self):
        return (f'{self.item_name} {self.item_quantity} @ {self.item_price} ' +  f'= ${self.item_price * self.item_quantity}')

cIN = input('Please enter the name of your 1st item: ')
cIP = input('Please enter the price for the item: ')
cIQ = input('Please enter the item quantity: ')

cInstance1 = ItemToPurchase(cIN, cIP, cIQ)

cIN = input('Please enter the name of your 2nd item: ')
cIP = input('Please enter the price for the item: ')
cIQ = input('Please enter the item quantity: ')

cInstance2 = ItemToPurchase(cIN, cIP, cIQ)

print('TOTAL COST')

print(cInstance1.print_item_cost())

print(cInstance2.print_item_cost())

print(f'Total:  ${(cInstance1.item_price * cInstance1.item_quantity) + (cInstance2.item_price * cInstance2.item_quantity)}')