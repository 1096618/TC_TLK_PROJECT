# -----------------------------------------------------------------------------
# Name:        Set method
# Purpose:     Create a program that copy, delete and clear set.
#
# Author:      TC
# Created:     April 4, 2025
# -----------------------------------------------------------------------------

import time #VERY NOT NECESSARY

colors = {"red", "blue", "green", "white", "gray", "indigo"}
print("Current colors set:")
print(", ".join(colors))

print()

copy = input("Do you wish to copy the colors above into a new set? (Y/N): ")
if copy == "Y" or copy == "y":
    colors_copy = colors.copy()
    print("Copied colors!")
    print()
    print("Copied colors set:")
    print(", ".join(colors_copy))


    print()
    pop = input("Would you like to delete a random color? (Y/N): ")
    if pop == "Y" or pop == "y":
        colors_copy.pop()
        print("," .join(colors - colors_copy), "has been deleted.")
        print()
        print("New copied colors set:")
        print(", ".join(colors_copy))

        print()
        clear = input("Do you wish to clear the colors? (Y/N): ")
        if clear == "Y" or clear == "y" or clear == "N" or clear == "n":
            time.sleep(2)
            print("Every colors have been deleted.")
            colors_copy.clear()
            time.sleep(3)
            print()
            print("Jk you just deleted the copied colors.")
            time.sleep(1.5)
            print("You still got the original colors set.")
            print(", ".join(colors))

        else:
            print("Bruh")
    else:
        print("Bruh")
else:
    print("Bruh")