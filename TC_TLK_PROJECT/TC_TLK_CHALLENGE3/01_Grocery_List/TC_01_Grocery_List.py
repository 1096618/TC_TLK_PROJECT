# -----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     Create a list of groceries and then add new items to the list.
#
# Author:      TC
# Created:     March 19, 2025
# -----------------------------------------------------------------------------

#Display current grocery list
grocerylist = ["pen", "pineapple", "apple"]
print("The current grocery list is:", ", ".join(grocerylist))

#Ask if user want to add more than 1 item or not
statement = input("Would you like to add more to the list?(y/n): ")
if statement == "y":
    print("Type done when you're done adding.")

    #Loop adding into the list until inputted "done"
    while statement == "y":
        grocerylist.append(input("Please enter your grocery list: "))
        if "done" in grocerylist:
            grocerylist.remove("done")
            break
    print("The current grocery list is:", ", ".join(grocerylist))
else:
    print("Your grocery list is:", ", ".join(grocerylist))
