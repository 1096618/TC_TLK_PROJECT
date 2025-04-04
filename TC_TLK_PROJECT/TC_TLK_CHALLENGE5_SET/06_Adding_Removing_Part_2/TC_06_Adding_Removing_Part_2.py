# -----------------------------------------------------------------------------
# Name:        Adding Removing Part 2
# Purpose:     Update a set with item from set 2 and discard an item from set
#
# Author:      TC
# Created:     Apri 4, 2025
# -----------------------------------------------------------------------------


colors1 = {"blue", "green", "cyan"}
colors2 = {"red", "blue", "indigo"}

print("Current colors sets:")
print("Color set 1: ",", " .join(colors1))
print("Color set 2: ",", " .join(colors2))

print()

while True:
    question = input("Do you want to update the colors set or discard color (update/discard): ").lower()
    if question == "update":

        update = input("Do you want to update the colors set 1 or 2 (1/2): ")
        if update == "1":
            colors1.update(colors2)
            print("Updated colors sets 1:")
            print("Color set 1: ",", " .join(colors1))
        elif update == "2":
            colors2.update(colors1)
            print("Updated colors sets 2:")
            print("Color set 2: ",", " .join(colors2))
        else:
            print("Wot does that mean mate")

    elif question == "discard":

        discard = input("Do you want to discard the colors set (1/2): ")
        if discard == "1":
            dis_item = input("What color do you want to discard?: ")
            if dis_item in colors1:
                colors1.discard(dis_item)
                print("Updated color set 1: ",", " .join(colors1))
            else:
                print("Item not found")

        if discard == "2":
            dis_item = input("What color do you want to discard?: ")
            if dis_item in colors2:
                colors2.discard(dis_item)
                print("Updated color set 2: ",", " .join(colors2))
            else:
                print("Item not found")