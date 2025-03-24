# -----------------------------------------------------------------------------
# Name:        Voting Eligibility test
# Purpose:     To check if person age is eligible to vote
#
# Author:      TC
# Created:     Feb 25, 2025
# -----------------------------------------------------------------------------

#Introduction message and ask for the age as variable
print("Hello this is your not really political bot")
age = int(input("Please enter your age: "))

#If age is 18 or higher
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")
