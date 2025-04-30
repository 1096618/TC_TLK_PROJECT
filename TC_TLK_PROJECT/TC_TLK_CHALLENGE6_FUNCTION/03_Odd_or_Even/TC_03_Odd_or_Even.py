# -----------------------------------------------------------------------------
# Name:        Odd or even
# Purpose:     Write a program that check odd or even using def function
#
# Author:      TC
# Created:     April 30, 2025
# -----------------------------------------------------------------------------

def odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter number to check: "))
odd_even(num)
