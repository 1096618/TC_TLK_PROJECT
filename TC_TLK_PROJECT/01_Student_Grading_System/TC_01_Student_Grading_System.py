# -----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To check your score and output your grade based on the score
#
# Author:      TC
# Created:     Feb 25, 2025
# -----------------------------------------------------------------------------

#Welcoming message and input the grade
print("Hello this is your simple dandy grade calculator!")

#Input grade as variable
grade = int(input("Please enter your grade: "))

#If grade is between 90 to 100
if grade >= 90 and grade <= 100:
    print("Your grade is A")

#If grade is between 80 and 89
elif grade >= 80 and grade <=89:
    print("Your grade is B")

#if grade is between 70 and 79
elif grade >= 70 and grade <=79:
    print("Your grade is C")

#If grade is between 60 and 69
elif grade >= 60 and grade <= 69:
    print("Your grade is D")

#If grade is below 60
elif grade < 60:
    print("Your grade is F")

#Invalid input
else:
    print("Invald Grade")