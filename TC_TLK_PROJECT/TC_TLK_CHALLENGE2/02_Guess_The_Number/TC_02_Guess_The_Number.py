# -----------------------------------------------------------------------------
# Name:        Guess the Number
# Purpose:     Write a program that generates a random number between 1 and 10 and keeps asking the user to guess it using a while loop until they guess correctly.
#
# Author:      TC
# Created:     March 7, 2025
# -----------------------------------------------------------------------------

#Import random module
import random

#===============================EASY===========================================#
#Define guess the number EASY mode function
def gtneasy():

    #Store a with random integer number within 0 and 10
    a = random.randint(0, 10)

    #print(a) #Reveal secret number line for quick testing
    #Set a counter as a variable to keep count of guesses
    counter = 0

    #Loop until found correct number
    while True:
        guess = int(input("Guess a number between 0 and 10: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} attempts.")
            break
        elif guess in range(a-2,a+2):
            print("HOT")
            counter += 1
        elif guess in range(a-5,a+5):
            print("A bit warm")
            counter += 1
        else:
            print("Cold")
            counter += 1

#===============================MEDIUM===========================================#
def gtnmedium():

    a = random.randint(0, 100)
    #print(a)
    counter = 0
    while True:
        guess = int(input("Guess a number between 0 and 100: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} attempts.")
            break
        elif guess in range(a-10,a+10):
            print("HOT")
            counter += 1
        elif guess in range(a-25,a+25):
            print("Warmer")
            counter += 1
        elif guess in range(a-50,a+50):
            print("A bit warm")
            counter += 1
        else:
            print("Cold")
            counter += 1

#===============================HARD===========================================#
def gtnhard():

    a = random.randint(0, 1000)
    #print(a)
    counter = 0
    while True:
        guess = int(input("Guess a number between 0 and 1000: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} attempts.")
            break
        elif guess in range(a - 10, a + 10):
            print("HOT")
            counter += 1
        elif guess in range(a - 25, a + 25):
            print("Very warm")
            counter += 1
        elif guess in range(a - 50, a + 50):
            print("Warm")
            counter += 1
        elif guess in range(a - 100, a + 100):
            print("A bit warm")
            counter += 1
        elif guess in range(a - 200, a + 200):
            print("A bit cold")
            counter += 1
        else:
            print("Cold")
            counter += 1

#===============================INPUT COMMAND===========================================#
while True:
    gamemode = input("What difficulty do you want to play (easy/medium/hard): ").lower()
    if gamemode == "easy":
        gtneasy()
    elif gamemode == "medium":
        gtnmedium()
    elif gamemode == "hard":
        gtnhard()
    else:
        print("Invalid input.")
        break
    again = input("Do you want to play again? (y/n): ").lower()
    if again == "n":
        break
#=======================================================================================#
