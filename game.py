'''
Created on May 13, 2019

@author: Shivam Patel
'''
class game:
    """ This class contains the information related to particular game"""
    
    numberOfGame = 0
    printgame = []
    status = []
    word = []
    badGuesses = []
    letter = []
    score = []
    finalScore = 0
    length = 0
    
    def storeGame(self,game):
         """ This function records and stores the number of games played by the player"""
         self.printgame.append(game)
         self.numberOfGame = game
         print("Number Of Games :" , self.numberOfGame)
    
    def storeStatus(self,status):
        """This function stores the Status of the game"""
        self.status.append(status)
        
    def storeWord(self,word): 
        """ This function stores the word in the game"""
        self.word.append(word)
    
    def storeBadGuesses(self,guess):
        """This function stores the number of bad guesses made by the player""" 
        self.badGuesses.append(guess)
    
    def storeMissedLetters(self,letters):
        """This function stores the letter missed by the player while guessing the word"""
        self.letter.append(letters)
    
    def storeScore(self,score):
        """This function stores the score of the game"""
        self.score.append(score)
       
    def wordFrequency(self,letter):
        """This function returns the value of the letter value"""
        
        value = {"a":8.17,"b":1.49,"c":2.78,"d":4.25,"e":12.70,"f":2.23,"g":2.02,"h":6.09,"i":6.97,"j":0.15,"k":0.77,"l":4.03,"m":2.41,"n":6.75,"o":7.51,"p":1.93,"q":0.10,"r":5.99,"s":6.33,"t":9.06,"u":2.76,"v":0.98,"w":2.36,"x":0.15,"y":1.97,"z":0.07}
        return value[letter]    
        
    def report(self):
        """This function displays the report of the game"""
        print(" Game      Word     Status     Bad Guesses   Missed Letters   Score")
        print("-----      ----     ------      ----------   --------------    -----")

        for x in range(self.numberOfGame):
            print(self.printgame[x],"         " , self.word[x] ,"     ",self.status[x], "        ",self.badGuesses[x],"          ",self.letter[x],"       ",self.score[x],"\n")
        
        print()
        for i in range(self.numberOfGame):
            self.finalScore = self.finalScore + self.score[i]
        print("Final Score : " , self.finalScore)
        