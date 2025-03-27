# -----------------------------------------------------------------------------
# Name:        Guess the Number
# Purpose:     Write a program that generates a random number between 1 and 10 and keeps asking the user to guess it using a while loop until they guess correctly.
#
# Author:      TC
# Created:     March 7, 2025
# Updated:     March 27, 2025: Added highscore system
# -----------------------------------------------------------------------------
#GAME HIGHSCORE:
#- TC
#EASY MODE: 1
#MEDIUM MODE: 3
#HARD MODE: 4
# -----------------------------------------------------------------------------

#Import random module
import random
import time

#===============================EASY===========================================#
#Define guess the number EASY mode function
def gtneasy():

    #Store a with random integer number within 0 and 10
    a = random.randint(0, 10)
    #print(a) #Reveal secret number line for quick testing

    #Set a counter as a variable to keep count of guesses
    counter = 0

    #Loop until found correct number
    #If guess incorrect print hotter or warmer based on how far off you are and add 1 to the counter
    while True:
        guess = int(input("Guess a number between 0 and 10: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} attempts.")
            global neweasyscore
            neweasyscore = counter
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
            global newmediumscore
            newmediumscore = counter
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
            global newhardscore
            newhardscore = counter
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

#===============================HARD===========================================#
def impossible(time_limit):

    a = random.randint(0, 1000000)
    counter = 0
    start_time = time.time()

    print(f"You have {time_limit} second to guess it correctly good luck!")
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time up! Game over!")
            break
        guess = int(input("Guess a number between 0 and 1,000,000: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} attempts.")
            global newhardscore
            newhardscore = counter
            break
        elif guess in range(a - 10, a + 10):
            print("HOT")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1
        elif guess in range(a - 25, a + 25):
            print("Very warm")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1
        elif guess in range(a - 50, a + 50):
            print("Warm")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1
        elif guess in range(a - 100, a + 100):
            print("A bit warm")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1
        elif guess in range(a - 200, a + 200):
            print("A bit cold")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1
        else:
            print("Cold")
            time_left = time_limit - int(elapsed_time)
            print(f"You have {time_left} seconds remaining.")
            counter += 1

#===============================HIGHSCORE===========================================#
easyscore =999
neweasyscore =999
mediumscore =999
newmediumscore =999
hardscore =999
newhardscore =999
def highscore():
    #Get highscore for hard mode
    global newhardscore
    global hardscore
    if newhardscore < hardscore:
        hardscore = newhardscore

    #Get highscore for medium mode
    global newmediumscore
    global mediumscore
    if newmediumscore < mediumscore:
        mediumscore = newmediumscore

    #Get highscore for easy mode
    global neweasyscore
    global easyscore
    if neweasyscore < easyscore:
        easyscore = neweasyscore

    #Display highscore
    print("The highscore is:")
    print(f"Easy mode: {easyscore}")
    print(f"Medium mode: {mediumscore}")
    print(f"Hard mode: {hardscore}")
    print("The lower the score the better!")

#===============================INPUT COMMAND===========================================#
while True:
    print("#=======================================================================================#")
    gamemode = input("What difficulty do you want to play or check score (easy/medium/hard)(score): ").lower()
    if gamemode == "easy":
        gtneasy()
    elif gamemode == "medium":
        gtnmedium()
    elif gamemode == "hard":
        gtnhard()
    elif gamemode == "score":
        highscore()
    elif gamemode == "impossible":
        impossible(60)
    else:
        print("Invalid input.")
        print("Exiting program...")
        break
#=======================================================================================#
