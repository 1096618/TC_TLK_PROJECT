# -----------------------------------------------------------------------------
# Name:        Day of the Week Activity Recommender
# Purpose:     To give suggestion of an activity to do on multiple day
#
# Author:      TC
# Created:     Feb 26, 2025
# Updated:     Feb 27, 2025
# -----------------------------------------------------------------------------

# Introduction message and asking the user for the current day of the week
# and save it as variable
print("==================================================================")
print("Hello this your hard coded Activity Recommender bot ")

# Ask how many days the user wants to get suggested (up to 3)
num_days = int(input("How many days do you want to get an activity? (1-3): ").strip())

# Ensure the number of days is between 1 and 3
if num_days < 1 or num_days > 3:
    print("Please enter a valid number of days (between 1 and 3).")
else:
    print("==================================================================")

    #Import random module in python and list out the activity then store it in a variable
    import random
    activity = ("It's a great day to start a workout!",
                "It's a great day to read a book!",
                "It's a great day to have a movie night!!",
                "Try learning a new recipe!",
                "Go for a hike!",
                "Go hang out with friends!",
                "Enjoy the day by treating yourself!",
                "I have a hunch it's going to be your lucky day!",
                "It's a great day to learn a new skill!",
                "It's a great day to go to the beach!",
                "DON'T GO OUTSIDE TODAY, IT'S GOING TO BE THE END OF THE WORLD"
                )

    # define rda as "return random.choice(activity)"
    #"random.choice(activity)" output a random option from the list of activity
    def RDA():
        return random.choice(activity)

    # Ask the user for up to 3 days and display activities for each days
    for i in range(num_days):
        day = input(f"Please enter day {i + 1}: ").strip().lower()

        # Activity Recommender
        if day == "monday" or day == "mon":
            print(f"On Monday. {RDA()}")
        elif day == "tuesday" or day == "tue" or day == "tues":
            print(f"On Tuesday. {RDA()}")
        elif day == "wednesday" or day == "wed":
            print(f"On Wednesday. {RDA()}")
        elif day == "thursday" or day == "thu" or day == "thur" or day == "thurs":
            print(f"On Thursday. {RDA()}")
        elif day == "friday" or day == "fri":
            print(f"On Friday. {RDA()}")
        elif day == "saturday" or day == "sat":
            print(f"On Saturday. {RDA()}")
        elif day == "sunday" or day == "sun":
            print(f"On Sunday. {RDA()}")
        else:
            print("Invalid input.")