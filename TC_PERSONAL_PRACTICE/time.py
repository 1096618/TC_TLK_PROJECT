#import time
#time_limit = 30
#start_time = time.time() #time.time() start at 0 and start_time = 0 at the begining
#while True:
#    # Calculate the elapsed time
#    elapsed_time = time.time() - start_time #As the time go up it minus start time which is 0 and get the elapsed time
#
#    # Check if the time limit has been reached
#    if elapsed_time > time_limit:
#        print("Time's up! Game Over.")
#        break

    # Display how much time is left
#    time_left = time_limit - int(elapsed_time)
#    print(f"You have {time_left} seconds remaining.")

#a = 5341
#print(f"The number have {len(str(a))} digits")

import time
import random

emojia = ["🍎", "🍓", "🍇", "🍒", "🍑"]
emojib = ["🍎", "🍓", "🍇", "🍒", "🍑"]
emojic = ["🍎", "🍓", "🍇", "🍒", "🍑"]
weights = [50, 35, 5, 15, 80]
#apple = 50, strawberry = 35, grape = 5, cherry = 15, peach = 80


grape_won =0 #🍇 tracker
cherry_won =0 #🍒 tracker
strawberry_won =0 #🍓 tracker
apple_won =0 #🍎 tracker
peach_won =0  #ass tracker

time_limit = 220 #540
start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time up! Game over!")
        break
    for i in range(50):
        a = random.choices(emojia, weights= weights, k=1)
        b = random.choices(emojib, weights= weights, k=1)
        c = random.choices(emojic, weights= weights, k=1)
        print(f"\r                     Slot: {a[0]} {b[0]} {c[0]}", end="", flush=True)
        time.sleep(0.1)
    print()
    if a[0] == "🍇" and b[0] == "🍇" and c[0] == "🍇":
        print("MEGA JACKPOT")
        grape_won += 1
    elif a[0] == "🍎" and b[0] == "🍎" and c[0] == "🍎":
        print("Minor prize")
        apple_won += 1
    elif a[0] == "🍑" and b[0] == "🍑" and c[0] == "🍑":
        print("You lose nothing")
        peach_won += 1
    elif a[0] == "🍓" and b[0] == "🍓" and c[0] == "🍓":
        print("Minor prize")
        strawberry_won += 1
    elif a[0] == "🍒" and b[0] == "🍒" and c[0] == "🍒":
        print("Minor prize")
        cherry_won += 1

print("Grape has won:", grape_won)
print("Cherry has won:", cherry_won)
print("Strawberry has won:", strawberry_won)
print("Apple has won:", apple_won)
print("Peach has won:", peach_won)