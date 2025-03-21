# -----------------------------------------------------------------------------
# Name:        Grocery List - Slice and length
# Purpose:     Slice a list and find the length
#
# Author:      TC
# Created:     March 21, 2025
# -----------------------------------------------------------------------------

#Display messages, list and the length of the list
print("WELCOME TO LIST SLICING MACHINE AND IM TOTALLY NOT DOING THIS OUT OF FRUSTATION THAT I COULDNT TURN IT INTO SOMETHING THAT ISNT CODING")
grocerylist = ["pen", "pineapple", "apple", "ballpoint pen", "pineapple pen", "apple pen"]
print("The current grocery list is:", ", ".join(grocerylist))
print(f"There are {len(grocerylist)} item in the current list")

#enumerate(grocerylist,1) assign each item in a list with a number starting from 1
#example (1, "pen")
#then for each number and item it created, stored those into it's respective variable index, item
#then display it as 1.pen
#but since (f"{index}.{item}" for index, item in enumerate(grocerylist,1)) is just a list value generator
#you either print it using list() or join() it as a list like below
#print(list(f"{index}.{item}" for index, item in enumerate(grocerylist,1)))
print(", " .join([f"{index}.{item}" for index, item in enumerate(grocerylist,1)]))


#Ask the user to input the numbered item
slicestart = int(input("From left to right which number you want to slice from(1-5)"))
#In order for the user to not break the program, i make slicestart+1 so the user dont input any number below the number they inputted
sliceend = int(input(f"From left to right which number you want to slice from({slicestart + 1}-6)"))

#Sliced grocery list according to number inputted and assign it in a variable to make it simple when printing
slicedlist = grocerylist[slicestart - 1:sliceend]
print("The new list is:", ", ".join(slicedlist))


