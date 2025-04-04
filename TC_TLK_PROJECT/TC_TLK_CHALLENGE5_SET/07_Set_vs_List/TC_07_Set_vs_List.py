# -----------------------------------------------------------------------------
# Name:        Set vs List
# Purpose:     Convert a set into a list and test it
#
# Author:      TC
# Created:     Apri 4, 2025
# -----------------------------------------------------------------------------

set = {"red", "blue", "green", "yellow", "orange", "purple", "pink"}
print("Current set:")
print(", ".join(set))

print()
print("Since set dont allow duplicate colors we can test that and see")
test = input("Input a duplicate color to add to current set: ")
set.add(test)
print()
print(", ".join(set))
print("As you can see the color didnt get added since it is a duplicate")
print()

quest = input("Would you like to convert set into a list?(y/n) ")
if quest == "yes" or quest == "y":
    list = list(set)
    print("Set has successfully been converted to list.")
    print("List:", ", ".join(list))
    print()

    print("Unlike set, list can be indexed and you can get specific item in list")
    print(f"There are {len(list)} items in this set.")
    index = int(input("Input index of item to see item in list: "))

    if index >= len(list) or index < 0:
        print("Index out of range")
    else:
        print(f"Index {index} is {list[index-1]} in list")