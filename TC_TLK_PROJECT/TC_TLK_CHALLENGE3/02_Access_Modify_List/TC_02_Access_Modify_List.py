# -----------------------------------------------------------------------------
# Name:        Grocery List - Access and modify
# Purpose:     Create a list of groceries and then add new items to the list.
#
# Author:      TC
# Created:     March 19, 2025
# -----------------------------------------------------------------------------

grocerylist = ["pen", "pineapple", "apple", "ballpoint pen"]
print("The current grocery list is:", ", ".join(grocerylist))
litem = input("What item in the list would you like to change? ")
if litem in grocerylist:
    nitem = input("What item would you like to replace it with ")
    grocerylist[grocerylist.index(litem)] = nitem
    print("The current grocery list is:", ", ".join(grocerylist))
