# -----------------------------------------------------------------------------
# Name:        Temperature Advice
# Purpose:     To evaluate your current temperature and give suggestion
#              on what to do
#
# Author:      TC
# Created:     Feb 25, 2025
# -----------------------------------------------------------------------------

#Introduction message and ask for current temperature as variable
print("Hello this is your hard coded temperature AI advisor")
temperature = int(input("Please enter your temperature(In celsius): "))

#If the temperature is below 10 degree celsius
if temperature < 10:
    print(f"Your temperature is {temperature}°C: It's cold outside. Wear a jacket!")

#If the temperature is between 10 and 25 degree celsius
elif temperature >= 10 and temperature <= 25:
    print(f"Your temperature is {temperature}°C: It's a nice day. Wear short-sleeves!")

#If the temperature is above 25 degree celsius
elif temperature > 25:
    print(f"Your temperature is {temperature}°C: It's hot outside. Stay cool and bring water!")

#Invalid input
else:
    print("Invalid temperature")