# -----------------------------------------------------------------------------
# Name:        Accessing set element
# Purpose:     Write a program that loop print each element in a set
#
# Author:      TC
# Created:     April 2, 2025
# -----------------------------------------------------------------------------

colors = {"red", "blue", "green", "yellow"}
print("Colors list:")
print(", " .join(colors))
print()

while True:
    print()
    option = input("Would you like to add or remove the colors?(add/remove/view) ")
    if option == "add":

        print("Loop Adding Colors! Type 'done' to quit adding")
        while True:
            new_color = input("Enter new color: ")
            if new_color == "done":
                print()
                print("Updated colors:")
                print(", ".join(colors))
                break
            else:
                colors.add(new_color)
                print(f"{new_color} has been added")

    elif option == "remove":

        print("Loop Removing Colors! Type 'done' to quit removing")
        while True:
            removed_color = input("Enter color to remove: ")

            if removed_color in colors: #Check if color in set before adding

                #Check if user write done
                if removed_color == "done":
                    print()
                    print("Updated colors:")
                    print(", ".join(colors))
                    break

                else: #Removing color
                    colors.remove(removed_color)
                    print(f"{removed_color} has been removed")

            #Check if user write done
            elif removed_color == "done":
                print()
                print("Updated colors:")
                print(", ".join(colors))
                break

            else:
                print(f"{removed_color} does not exist")

    elif option == "view":
        print("Current colors:")
        print(", ".join(colors))

    else:
        print("Shutting down...")
        break
