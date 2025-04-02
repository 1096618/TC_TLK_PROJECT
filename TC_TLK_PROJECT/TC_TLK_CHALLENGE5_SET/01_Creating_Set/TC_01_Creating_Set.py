# -----------------------------------------------------------------------------
# Name:        Creating set
# Purpose:     Creating a new set and add an item.
#
# Author:      TC
# Created:     Apri 2, 2025
# -----------------------------------------------------------------------------

print("Fruit basket:")
fruit = {"Apple", "Banana", "Cherry"}
print(", " .join(fruit)) #Make it look fancy

print()
print("Adding a new fruit")

new_fruit = input("Enter your fruit: ")
fruit.add(new_fruit)
print("Updated Fruit basket:")
print(", " .join(fruit))