MODIFIED PROBLEM: Write a game program that have 3 difficulty which generates a random number between `a` and `b` and keeps asking the user to guess it using a `while` loop **until they guess correctly**.  

Pseudo code:

Creating modules
1. Import random module to use random function
2. Define easy mode which guess the number between 1 to 10
+ Generate a random number within 1 and 10 and store it in `a` 
+ Variable `counter` = `0` for keeping track of attempts 
+ White true loop guessing function till correctly
+ If guess correctly, display attempts and stop function
+ Add in multiple else if statement that check when the user guess within a range of the number that has been generated and print whether it hotter or warmer while increasing `counter`
3. Define medium mode which guess the number between 1 and 100
4. Define hard mode which guess the number between 1 and 1000

Game menu

1. While true loop 
2. Ask the user which difficulty they want to play(easy/medium/hard)
3. Execute function based on what inputted
4. After finishing a game ask the user if they want to play again if no break loop

Minigame

- Landmine
- 