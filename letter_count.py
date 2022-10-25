#Ch 7 Programming Assignment
#Jared Adamson
#Part A
# Counts letters in a words chosen by the user.

'''
Create a program in a file named letter_count.py. Prompt the user to enter three different words or phrases, 
one at a time; store each response in a separate variable. Next, prompt the user a letter they wish to count. 
Finally, count how many times the letter occurs in each of the three words/phrases, regardless of case 
(uppercase or lowercase), as well as the total; output a formatted table displaying the results. 
Be sure your program includes adequate directions for the user.

Sample Program Run:
Enter the first word: Apple
Enter the first word: Pear
Enter the first word: OrAnGe
Enter the letter to count: p 
Occurrences of p
---------------------------------
Apple                           2
Pear                            1
OrAnGe                          0
---------------------------------
Total                           3
'''
from itertools import count

#Collect words and the letter to count.

print("Please enter three different words or phrases, one at a time:")

wOne = input("Word/Phrase #1:")
wTwo = input("Word/Phrase #2:")
wThree = input("Word/Phrase #3:")

lc = input("Please enter the letter you wish to be counted:")

#Print the table with letter counts.

print(f"Occurrences of {lc}\n", "-" * 25)

lc = lc.lower()

print(f'{wOne:20}{wOne.lower().count(lc):>5}')
print(f'{wTwo:20}{wTwo.lower().count(lc):>5}')
print(f'{wThree:20}{wThree.lower().count(lc):>5}')
print("-" * 25)

wTotal = wOne.lower().count(lc) + wTwo.lower().count(lc) + wThree.lower().count(lc)

print(f'{"Total":20}{wTotal:>5}')
