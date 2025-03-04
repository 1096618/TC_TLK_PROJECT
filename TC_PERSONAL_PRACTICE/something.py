#while True:
#    print("Welcome to TC-PERSONAL PRACTICE!")
#    again = input("Would you like to go again? (y/n): ").lower()
#    if again == "n":
#        break
#print("Thank you for testing TC-PERSONAL PRACTICE!")

'''
print("Welcome to WHO WANT TO BE A MILLIONAIRE.")
name = print("Please enter your name.")
lives = 3

#question 1
q1 = input("What does K in the TLK stand for? ")
if q1 == "Kennedy":
    print("CORRECT")
else:
    lives -= 1  # Reduce a life for a wrong answer
    print(f"Wrong answer. You have {lives} lives left.")
if lives == 0:
    print("You have lost all your lives. Game over!")
    return

#question 2
q2 = input("What does GPS stand for? ")
if q2 == "GamingPrOStuFF":
    print("CORRECT")
else:
    lives -= 1
    print(f"Wrong answer. You have {lives} lives left.")
if lives == 0:
    print("You have lost all your lives. Game over!")
    return

#question 3
q2 = input("What does WTF stand for? ")
if q2 == "What The Fudge":
    print("CORRECT")
else:
    lives -= 1
    print(f"Wrong answer. You have {lives} lives left.")
if lives == 0:
    print("You have lost all your lives. Game over!")
    return

#question 4
q2 = input("What is 9 + 10 =? ")
if q2 == "21":
    print("CORRECT")
else:
    lives -= 1
    print(f"Wrong answer. You have {lives} lives left.")
if lives == 0:
    print("You have lost all your lives. Game over!")
    return

#question 5
q2 = input("What is 1 + 1 =? ")
if q2 == "3":
    print("CORRECT")
else:
    lives -= 1
    print(f"Wrong answer. You have {lives} lives left.")
if lives == 0:
    print("You have lost all your lives. Game over!")
    return
'''

def millionaire():
    lives = 3

    print("Welcome to WHO WANT TO BE A DIGITAL MILLIONAIRE.")
    name = input("What is your name: ")
    print(f"{name} you have {lives} lives!.")

    print("First question!")
    q1 = input("What does K in the TLK stand for? ")
    if q1 == "Kennedy":
        print("CORRECT")
    else:
        lives -= 1
        print(f"Wrong answer. You have {lives} lives left.")
        if lives == 0:
            print("You have lost all your lives. Game over!")
            return

    print("Second question!")
    q1 = input("What does GPS stand for? ")
    if q1 == "GamingPrOStuFF":
        print("CORRECT")
    else:
        lives -= 1
        print(f"Wrong answer. You have {lives} lives left.")
        if lives == 0:
            print("You have lost all your lives. Game over!")
            return

    print("Third question!")
    q1 = input("What is 9 + 10? ")
    if q1 == "21":
        print("CORRECT")
    else:
        lives -= 1
        print(f"Wrong answer. You have {lives} lives left.")
        if lives == 0:
            print("You have lost all your lives. Game over!")
            return

    print("Fourth question!")
    q1 = input("How can fish fishes when fish is fish and if fish fishes then why fish fish? ")
    if q1 == "yes":
        print("CORRECT")
    else:
        lives -= 1
        print(f"Wrong answer. You have {lives} lives left.")
        if lives == 0:
            print("You have lost all your lives. Game over!")
            return


    print("Fifth question!")
    q1 = input("Is this game show rigged? ")
    if q1 == "no":
        print("CORRECT")
    else:
        lives -= 1
        print(f"Wrong answer. You have {lives} lives left.")
        if lives == 0:
            print("You have lost all your lives. Game over!")
            return

    if lives > 0:
        print(f"Congratulations {name}. You have won with {lives} lives left!")

millionaire()
