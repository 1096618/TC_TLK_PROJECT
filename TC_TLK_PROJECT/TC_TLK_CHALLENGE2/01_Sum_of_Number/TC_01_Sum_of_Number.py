# -----------------------------------------------------------------------------
# Name:        Sum of number
# Purpose:     To write a program that ask the user for n number
#              and calculates the sum of all numbers from 1 to n using a for loop
#
# Author:      TC
# Created:     March 5, 2025
# -----------------------------------------------------------------------------


#method 1

#Create an empty variable for later use
num = 0

#Ask for the user number to get the sum of and only accepting integers
x = int(input("Enter number:"))

#For loop and since range(x) would only get you to x-1 (input 5, output 4) we put x+1 (input 5, output 5)
for i in range(x+1):

    #Add each number generated from the loop into the empty variable while adding up the total
    num += i

#Display the total number we have added
print("The sum of number is",num)

#method 2
'''
#Create an empty list for later use
numlist = []
#Ask the user for the number to get the sum of and only accepting integers
urnum = int(input("Enter the number: "))
#For loop in a range that user inputted
for i in range(urnum+1):
    #Add all the number from the loop into the list
    numlist.append(i)
#Display the sum of the numbers from the list    
print("The sum of number is,sum(numlist))
'''