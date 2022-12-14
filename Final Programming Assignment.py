#Final Programming Assignment
#Jared Adamson
#Hangman Game
#Let the user play a game of hangman.
#Hangman Ascii Art borrowed & tweeked from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

import random
playgame = "N"
error = 1

#Main Hangman Class used to get the game going and perform game functions. 
class hangmanGame:
    def __init__(self, gameArray, wordNum):
        self.chosenWord = gameArray[wordNum].upper()
        self.gameState = 0
        self.userLetter = ""
        self.matchWord = []
        self.tstWord = []
        self.gameArt = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
        self.wLength = len(self.chosenWord)
        self.cwList = list(self.chosenWord)
        for x in range(self.wLength):
            self.matchWord.append(x)
        for x in self.matchWord:
            self.tstWord.append("_")


    def printBoard(self):

        return self.gameArt[self.gameState]

#Collects user letter input and makes sure it is good returns the letter back.
    def getLetter(self):
        alph = False
        while alph == False:
            try:
                self.userLetter = input("Please enter a letter to check: ").upper()
                self.userLetter = self.userLetter[0]
                alph = self.userLetter.isalpha()
                if alph == False:
                    raise Exception("Invalid input.  Try again.")
                                        
            except:
                print("Invalid input.  Try again.")
                alph = False
        
        return self.userLetter

#updates the game state & checks if user guess is correct.
    def updateGame(self, letter):
        l = letter.upper()
        if l in self.cwList:
            for x in self.cwList:
                if l in self.cwList:
                    guess = self.cwList.index(l)
                    self.matchWord[guess] = l
                    self.tstWord[guess] = l
                    self.cwList[guess] = "_"
            print("Your guess was correct!")
            gUpdate = self.printBoard()
            w = "".join(self.tstWord)
            print(gUpdate)
            print(w)
            if self.matchWord == self.tstWord:
                self.gameState = -100
            return self.gameState
        else:
            self.gameState += 1
            print("Your guess was incorrect.")
            gUpdate = self.printBoard()
            w = "".join(self.tstWord)
            print(gUpdate)
            print(w)      
            return self.gameState       


#Opens a file with words to use.  If there is a problem uses a default list.
try:

    myFile = open("dictionary.txt")
    fContent = myFile.readlines()
    j = 0
    for x in fContent:
        fContent[j] = x.rstrip("\n")
        j += 1

except:

    fContent = ["bat", "cat", "hat", "test", "words"]

length = len(fContent)


#Initates the the game and handles errors
while error == 1: 
    try:
        playGame = input("Ready to play? Y for Yes or N for No: ").upper()
        print(playGame)

        if playGame == "Y":
            
            gameWord = random.randint(0,length - 1)
            newGame = hangmanGame(fContent, gameWord)
            print("Enter letters to guess the secret word. \nEnter all of the letters in the word in you win. \nEnter the incorrect letter too many times and it's game over!")   
            print(newGame.printBoard())
            
            error = 0

        elif playGame == "N":
            error = 0
            print("Closing Program.  Have a good day.")
        
        else:
            raise Exception("Invalid input.  Try again.")
            error = 1   

    except:
        print("Invalid input.  Try again.")
        error = 1

#Iterates thru the game methods to run the game.
while playGame == "Y":
         
    pick = newGame.getLetter()
    state = newGame.updateGame(pick)
    
    if state >= 6:
        playGame = "N"    
        print("You Lose! Thanks for playing.")
    if state == -100:
        playGame = "N"    
        print("You WIN! Thanks for playing!")