# -----------------------------------------------------------------------------
# Name:        Set operations
# Purpose:     Write a program that combine and compare sets using set operations.
#
# Author:      TC
# Created:     April 3, 2025
# -----------------------------------------------------------------------------

set1 = {"Red", "Green", "Blue", "Yellow", "White"}
set2 = {"Pink", "Green", "Cyan", "Yellow", "Black"}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print() #Leave empty space for better visual

print("Method 1")
print(f"Union of 2 sets: {set1.union(set2)}")
print(f"Intersection of 2 sets: {set1.intersection(set2)}")
print(f"Difference of set 1: {set1.difference(set2)}")
print(f"Difference of set 2: {set2.difference(set1)}")

print()
print("Method 2")
print(f"Union of 2 sets: {set1 | set2}")
print(f"Intersection of 2 sets: {set1 & set2}")
print(f"Difference of set 1: {set1 - set2}")
print(f"Difference of set 2: {set2 - set1}")