#Ch 3 Programming Assignment
#Jared Adamson
#Part B

fDict = {
    'Bob': 65,
    'Sammy': 13,
    'Sue': 7,
    'Tammy': 62
}

print(fDict)

print(fDict['Sammy'])

fDict['Tim'] = 23

print(fDict)

searchDict = input("Enter a person to look up:")

print(fDict[searchDict])