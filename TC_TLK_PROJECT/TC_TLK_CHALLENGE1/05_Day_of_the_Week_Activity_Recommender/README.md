ORIGINAL PROBLEM

Problem: Create a Python program that suggests an activity based on the day of the week.

Pseudo Code:
1. Ask the user to enter the current day of the week (e.g., "Monday", "Tuesday").
2. Store the day in a variable.
3. Use conditional statements to recommend an activity based on the day.
    - If the day is "Monday", print: `"Start your week with a workout!"`
    - If the day is "Tuesday", print: `"It's a great day to read a book!"`
    - If the day is "Wednesday", print: `"Mid-week movie night!"`
    - If the day is "Thursday", print: `"Try a new recipe!"`
    - If the day is "Friday", print: `"Relax and enjoy the weekend!"`
    - If the day is "Saturday", print: `"Go for a hike!"`
    - If the day is "Sunday", print: `"Prepare for the week ahead with some self-care."`

MODIFY PROBLEM

Problem: Create a Python program that suggests an activity for multiple day up to 3

Pseudo code:
1. Print introduction msg
2. Ask user for the amount of day they want to get suggested while stripping any space before or after the word fo user convenient when using program
3. Save the input day as variable
4. Check if day is within 3 day limit and if it isnt print invalid
5. Import random module and save multiple activity in a variable
6. define RDA() as random.choice() to make it shorter (once again for convenient not necessary)
7. For the amount of day the user input, ask and repeat X amount of day to get activity while stripping uppercase into lowercase and stripping space
8. Bunch of if and elif to check for the user input and print the activity on each day

