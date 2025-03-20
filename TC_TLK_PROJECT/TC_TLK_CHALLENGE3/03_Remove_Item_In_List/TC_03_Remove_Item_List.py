# -----------------------------------------------------------------------------
# Name:        Grocery List - Removing item
# Purpose:     Modify the list by removing item in the list.
#
# Author:      TC
# Created:     March 20, 2025
# -----------------------------------------------------------------------------

#Creat grocery list with items in it and display
grocerylist = ["pen", "pineapple", "apple", "ballpoint pen"]
print("The current grocery list is:", ", ".join(grocerylist))

#Ask the user which item in the list should be remove
litem = input("What item in the list would you like to remove? ")

#If item in list exist, remove it and display
if litem in grocerylist:
    grocerylist.remove(litem)
    print("The current grocery list is:", ", ".join(grocerylist))
else:
    print("The item not in the list.")