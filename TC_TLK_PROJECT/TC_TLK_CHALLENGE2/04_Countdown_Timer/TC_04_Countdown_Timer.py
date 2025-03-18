# -----------------------------------------------------------------------------
# Name:        Countdown timer
# Purpose:     Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.
#
# Author:      TC
# Created:     March 18, 2025
# -----------------------------------------------------------------------------

#Note: i wanted to make an actual countdown timer and print with a delay of 1 second and can stop whenever you type stop while still counting down
#without input but it impossible without threading or async or something which are too advanced it seem

#Input in how many tick to countdown from
countdown = int(input("How many tick to countdown to? "))

#Loop until countdown is 0
while countdown > 0:
    print(countdown)
    countdown -= 1

    #If user type "stop", the loop will stop
    stop = input()
    if stop == "stop":
        break

print("Countdown timer stopped")

