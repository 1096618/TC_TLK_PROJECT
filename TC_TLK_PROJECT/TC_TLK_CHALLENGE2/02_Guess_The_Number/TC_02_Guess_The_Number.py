import random
def gtneasy():

    a = random.randint(0, 10)
#    print(a)
    counter = 0
    while True:
        guess = int(input("Guess a number between 0 and 10: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} times.")
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

def gtnmedium():

    a = random.randint(0, 100)
#    print(a)
    counter = 0
    while True:
        guess = int(input("Guess a number between 0 and 100: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} times.")
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

def gtnhard():

    a = random.randint(0, 1000)
#    print(a)
    counter = 0
    while True:
        guess = int(input("Guess a number between 0 and 1000: "))
        if guess == a:
            print("Correct!")
            counter += 1
            print(f"You guessed it in {counter} times.")
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

