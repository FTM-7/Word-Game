'''
Created on May 13, 2019

@author: Shivam Patel
'''
import random


class stringDatabase: 
    """This class loads the four_letter text file and manipulates it"""
    def load(self):
        """
        This function randomly chooses a word to get loaded
        @return: random word from the text file
        """
        return random.choice(open("four_letters.txt").readline().split())
