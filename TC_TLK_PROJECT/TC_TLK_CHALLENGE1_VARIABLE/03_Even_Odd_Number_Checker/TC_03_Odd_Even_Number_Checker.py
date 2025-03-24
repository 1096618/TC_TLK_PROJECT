# -----------------------------------------------------------------------------
# Name:        Even and Odd Number Checker
# Purpose:     To check if the number is odd or even and tell the user
#
# Author:      TC
# Created:     Feb 25, 2025
# -----------------------------------------------------------------------------

#Introduction message and ask for the number the user want to check as variable
print("Hello welcome to your really convoluted calculator to check Odd and Even numbers")
number = int(input("Please enter your number(Integer only): "))

#If the number is divisible by 2
if number % 2 == 0:
    print(f"The number {number} is even")

#Else number is odd
else:
    print(f"The number {number} is odd")