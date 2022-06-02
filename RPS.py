# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:16:30 2022

@author: erenkaynarr
"""

import random,sys

print("****** Rock Paper Scissors *****")
win = 0
lose = 0
tie = 0

while True:
    print(f"Win: {win} Loss: {lose} Tie: {tie}")
    print("""Enter Your Move:
          r - rock
          p - paper
          s - scissors
          q - quit""")
    UserMove = input("Type one of r, p, s or q:")
    if UserMove == 'q':
        sys.exit()
              
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")
    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")
    elif randomNumber == 3:
        computerMove = 's'
        print("Scissors")
                    
    if UserMove == computerMove:
        print("Its tie !")
        tie += 1
    elif UserMove == 'r' and computerMove == 's':
        win += 1
        print("You Win !")
    elif UserMove == 'p' and computerMove == 'r':
        win += 1
        print("You Win !")
    elif UserMove == 's' and computerMove == 'p':
        win += 1
        print("You Win !")
    elif UserMove == 'r' and computerMove == 'p':
        lose += 1
        print("You Lose !")
    elif UserMove == 'p' and computerMove == 's':
        lose += 1        
        print("You Lose !") 
    elif UserMove == 's' and computerMove == 'r':
        lose += 1        
        print("You Lose !")
