'''
Created on May 13, 2019

@author: Shivam Patel 
'''
from stringDatabase import stringDatabase
from game import game
import sys


class guess:
    """This class is the game driver class i.e the main class"""
    title = "   ** The Great Guessing game **    "
    
   
    def menu(self):
        """ 
        This functions displays the Main Page of the Game 
        @return: the title of the game
        """
        
        return self.title
    
     
    def displayGuess(self):
        """ 
        This function displays the acronyms used in the game
        """
        print(" g = guess, t= tell me, l for a letter, and q to quit")
    
    
    def currentTurn(self):
        """ 
        This function starts the game
        @return: report if the player quits the game
                 calculates the score if correct/incorrect letter guesses
                 checks the guess is correct or not 
                 gives the name of the word while quiting if thw player opts for tell me option
        
        """
        guess  = "----"
        print()
        print("Current Guess : " , guess)
        
        myString = stringDatabase()
        myGame = game()

        check = myString.load()
        score = 0
        countGame = 0
        count=0
        badGuessCount =0
        missedLetterCount = 0
        print()
        for i in range(0,99):
                
                choice = input("Enter your choice : ")
                
                if choice == "l" :
                    letter = input("Enter a letter : ")
                    
                    if len(letter) > 1:
                        print("Only one Letter")
                    elif len(letter) == 0:
                        print("Type a Letter")
                    elif len(letter) == 1:
                        index = [];   
                        indexCheck = 0     

                        if letter in check :
                            for x in range(len(check)):
                                if letter == check[x]:
                                    index.append(x)
                                    
                            length = len(index)
                            guess = list(guess)
                            for i in range(length):
                                guess.remove(guess[index[i]])
                                guess.insert(index[i],letter)
                           
                            for i in guess:
                                print(i,end="")
                                   
                            score  = score  + myGame.wordFrequency(letter) 
                            print()
                            print("Letter Guess is Right")
                        elif letter not in check :
                            missedLetterCount = missedLetterCount + 1    
                            score = score - myGame.wordFrequency(letter)
                            print()
                            print("Letter Guess is Wrong")
                
        
                elif choice == "g":
                    
                    word = input("Enter the word :")

                    if word == check:
                        countGame =  countGame + 1
                        myGame.storeMissedLetters(missedLetterCount)
                        myGame.storeScore(score)
                        missedLetterCount = 0
                        score = 0
                        myGame.storeGame(countGame)
                        myGame.storeWord(word)
                        check = myString.load()
                        guess = "----"
#                         print("New Check :" , check)
                        print()
                        myGame.storeStatus("Success")
                        myGame.storeBadGuesses(badGuessCount)
                        print("Correct Guess") 
                        print()
                        decision = input("Do you want to Play Again ?  (y|n)")
                        if decision == "n":
                            print("Game Over")
                            print()
                            myGame.report()
                            sys.exit(0)
                    else:
                        badGuessCount =  badGuessCount + 1
                        print()
                        print("Incorrect Guess")
        
                elif choice == "q":
                    print()
                    print("Game Over !")
                    print("\n")
                    myGame.report()
                    flag=1
                    sys.exit(0)
        
                elif choice == "t":
                    countGame = countGame + 1
                    myGame.storeGame(countGame)
                    myGame.storeWord(check)
                    print("Word : ",check)
                    myGame.storeBadGuesses(badGuessCount)
                    myGame.storeMissedLetters(missedLetterCount)
#                     print(score)
                    myGame.storeScore(score)
                    missedLetterCount = 0
                    score = 0
                    myGame.storeStatus("Gave Up")
                    
#                     print("The word is " , check) 
                    check = myString.load()
                    guess = "----"
                    decision = input("Do you want to Play Again ? (y|n)")
                    if decision == "n":
                        print("Game Over")
                        print()
                        myGame.report()
                        sys.exit(0)
                        
     
                else:
                    print()
                    print("Invalid Input")
        
        
myGuess = guess()
print(myGuess.menu())
myGuess.displayGuess()
myGuess.currentTurn()
