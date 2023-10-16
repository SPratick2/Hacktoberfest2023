#import the necessary modules
import random
import time

#range of the values of a dice
if __name__=="__main__":

    print("-------  Welcome to RollTheDice !  -------")

    min_val = 1
    max_val = 6

    #to loop the rolling through user input
    roll_again = "yes"
    countSet = 1

    #loop unitl player quits the game
    while roll_again == "yes" or roll_again == "y" or roll_again == "Yes" or roll_again == "YES":
        #set nummber
        print("         Set Number :", countSet)
        countSet += 1

        #enter the players name
        p1 = input("          Enter Player1 name : ")
        p2 = input("          Enter Player2 name : ")

        print("          Rolling The Dices...")
        #provides 1.5s delay for rolling the dices
        time.sleep(1.5)
        
        #generating and printing 1st random integer from 1 to 6
        p1Val = random.randint(min_val, max_val)
        print("         ", p1, "has value of dice :", p1Val)
        
        #generating and printing 2nd random integer from 1 to 6
        p2Val = random.randint(min_val, max_val)
        print("         ", p2, "has value of dice :", p2Val)
        
        #comparing both players value and declaring a winner
        if p1Val > p2Val:   print("         ", p1, "has won the game !")
        elif p1Val < p2Val:     print("         ", p2, "has won the game !")
        else: print("          The result is a draw !")

        #asking user to roll the dice again. Any input other than yes or y will terminate the loop

        print("         Want to play again ? Yes or No")
        roll_again = input() 

    print("-------  Thanks for playing RollTheDice ! See you soon :)  -------")