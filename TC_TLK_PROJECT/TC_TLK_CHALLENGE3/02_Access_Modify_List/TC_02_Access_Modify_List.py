# -----------------------------------------------------------------------------
# Name:        Grocery List - Access and modify
# Purpose:     Modify the list by changing existing item in the list.
#
# Author:      TC
# Created:     March 19, 2025
# -----------------------------------------------------------------------------

#Create a list with all the grocery items and display them
grocerylist = ["pen", "pineapple", "apple", "ballpoint pen"]
print("The current grocery list is:", ", ".join(grocerylist))

#Ask the user which item in the list to be replace
litem = input("What item in the list would you like to change? ")
if litem in grocerylist:

    #If item does exist then ask what item does user want to replace with
    nitem = input("What item would you like to replace it with ")
    grocerylist[grocerylist.index(litem)] = nitem
    print("The current grocery list is:", ", ".join(grocerylist))

else:
    print("Sorry, the item you are looking for is not in your grocery list.")
