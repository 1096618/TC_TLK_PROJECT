# -----------------------------------------------------------------------------
# Name:        Skipping even numbers
# Purpose:     Write a program that prints numbers from `1` to `10`, but **skips even numbers** using the `continue` statement.
#
# Author:      TC
# Created:     March 17, 2025
# -----------------------------------------------------------------------------

#Ask the user for the range of number to print
x = int(input("Input first number:"))
y = int(input("Input second number:"))

#Loop print till satisfied the range
for i in range(x, y+1):

    #Only the number diveded by 2 and reminader is 0
    if i % 2 == 0:
        print(i)