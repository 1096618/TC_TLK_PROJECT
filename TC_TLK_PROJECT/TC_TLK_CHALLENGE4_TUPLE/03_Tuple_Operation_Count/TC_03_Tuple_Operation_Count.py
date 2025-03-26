# -----------------------------------------------------------------------------
# Name:        Tuple Operation Count
# Purpose:     Write a program check how many item in a very very very very long tuple
#
# Author:      TC
# Created:     March 25, 2025
# -----------------------------------------------------------------------------

import time #Not necessary for the program but did it for the meme

#A very long tuple that you cant possibly count manually
long_random_tuple = ["apple", "banana", "banana", "milk", "apple", "milk", "egg", "banana", "egg", "bread","apple", "milk", "egg", "apple", "banana", "banana", "bread", "egg", "milk", "milk","banana", "bread", "apple", "bread", "banana", "banana", "milk", "bread", "egg", "egg","milk", "banana", "banana", "apple", "egg", "milk", "bread", "apple", "milk", "bread","banana", "apple", "egg", "egg", "banana", "milk", "banana", "bread", "milk", "apple","apple", "milk", "bread", "banana", "egg", "bread", "banana", "milk", "banana", "egg","milk", "bread", "apple", "banana", "banana", "milk", "bread", "apple", "apple", "egg","bread", "milk", "banana", "egg", "bread", "egg", "apple", "banana", "milk", "bread","apple", "apple", "egg", "milk", "egg", "milk", "bread", "banana", "milk", "banana","apple", "milk", "banana", "egg", "apple", "bread", "bread", "egg", "banana", "milk","banana", "egg", "bread", "milk", "bread", "apple", "banana", "milk", "milk", "banana","apple", "bread", "milk", "banana", "milk", "egg", "apple", "egg", "banana", "apple","milk", "egg", "apple", "bread", "banana", "banana", "egg", "apple", "milk", "egg","banana", "apple", "egg", "milk", "milk", "banana", "milk", "banana", "banana", "egg","apple", "milk", "milk", "bread", "bread", "milk", "banana", "egg", "banana", "bread","egg", "banana", "milk", "apple", "banana", "milk", "egg", "egg", "apple", "bread","bread", "egg", "banana", "apple", "banana", "egg", "milk", "apple", "banana", "milk","bread", "milk", "egg", "apple", "egg", "banana", "banana", "bread", "milk", "milk","banana", "egg", "milk", "apple", "bread", "banana", "egg", "banana", "milk", "milk","bread", "apple", "milk", "banana", "apple", "bread", "egg", "banana", "egg", "milk","egg", "apple", "banana", "bread", "banana", "apple", "milk", "banana", "egg", "bread","banana", "milk", "egg", "milk", "banana", "apple", "milk", "egg", "bread", "banana","banana", "egg", "milk", "apple", "milk", "bread", "apple", "bread", "banana", "milk","bread", "banana", "egg", "milk", "egg", "banana", "apple", "banana", "egg", "milk", "apple", "egg", "banana", "banana", "egg", "milk", "milk", "bread", "banana", "egg","apple", "banana", "banana", "milk", "apple", "milk", "egg", "banana", "egg", "bread","apple", "milk", "egg", "apple", "banana", "banana", "bread", "egg", "milk", "milk","banana", "bread", "apple", "bread", "banana", "banana", "milk", "bread", "egg", "egg","milk", "banana", "banana", "apple", "egg", "milk", "bread", "apple", "milk", "bread","banana", "apple", "egg", "egg", "banana", "milk", "banana", "bread", "milk", "apple","apple", "milk", "bread", "banana", "egg", "bread", "banana", "milk", "banana", "egg","milk", "bread", "apple", "banana", "banana", "milk", "bread", "apple", "apple", "egg","bread", "milk", "banana", "egg", "bread", "egg", "apple", "banana", "milk", "bread","apple", "apple", "egg", "milk", "egg", "milk", "bread", "banana", "milk", "banana","apple", "milk", "banana", "egg", "apple", "bread", "bread", "egg", "banana", "milk","banana", "egg", "bread", "milk", "bread", "apple", "banana", "milk", "milk", "banana","apple", "bread", "milk", "banana", "milk", "egg", "apple", "egg", "banana", "apple","milk", "egg", "apple", "bread", "banana", "banana", "egg", "apple", "milk", "egg","banana", "apple", "egg", "milk", "milk", "banana", "milk", "banana", "banana", "egg","apple", "milk", "milk", "bread", "bread", "milk", "banana", "egg", "banana", "bread","egg", "banana", "milk", "apple", "banana", "milk", "egg", "egg", "apple", "bread","bread", "egg", "banana", "apple", "banana", "egg", "milk", "apple", "banana", "milk","bread", "milk", "egg", "apple", "egg", "banana", "banana", "bread", "milk", "milk","banana", "egg", "milk", "apple", "bread", "banana", "egg", "banana", "milk", "milk","bread", "apple", "milk", "banana", "apple", "bread", "egg", "banana", "egg", "milk","egg", "apple", "banana", "bread", "banana", "apple", "milk", "banana", "egg", "bread","banana", "milk", "egg", "milk", "banana", "apple", "milk", "egg", "bread", "banana","banana", "egg", "milk", "apple", "milk", "bread", "apple", "bread", "banana", "milk","bread", "banana", "egg", "milk", "egg", "banana", "apple", "banana", "egg", "milk","apple", "egg", "banana", "banana", "egg", "milk", "milk", "bread", "banana", "egg"]
print("There are 5 unique item in the list: Apple, Banana, Milk, Bread, Egg")
print(f"And there are total of {len(long_random_tuple)} items")
check = input("Would you like to check how many items there are?(y/n) ").lower()

#If yes loop checking item in long tuple
if check == "yes" or check == "y":
    while True:
        checkitem = input("What item would you like to check? ").lower()
        if checkitem in long_random_tuple:
            print(f"There are {long_random_tuple.count(checkitem)} {checkitem} in the list")
        else:
            print(f"Item {checkitem} does not exist in the list")

        #Go again
        again = input("Would you like to check again?(y/n) ").lower()
        if again == "yes" or again == "y":
            continue
        else:
            print("Closing program", end=" "), time.sleep(1), print(".", end=" "), time.sleep(1), print(".", end=" "), time.sleep(1), print("."), time.sleep(1)
            break
else:
    print("Why you even bother running the script")