import time
import random

emoji = ["🍎", "🍓", "🍇", "🍒", "🍑"]
weights = [50, 35, 5, 15, 80]
# apple = 50, strawberry = 35, grape = 5, cherry = 15, peach = 80


grape_won = 0  # 🍇 tracker
cherry_won = 0  # 🍒 tracker
strawberry_won = 0  # 🍓 tracker
apple_won = 0  # 🍎 tracker
peach_won = 0  # ass tracker

tries_limit = 50
tries = 0

while True:

    if tries >= tries_limit:
        print(f"{tries_limit} tries reached! Stopping slot machine...!")
        break

    for i in range(30):
        a = random.choices(emoji, weights=weights, k=1)
        b = random.choices(emoji, weights=weights, k=1)
        c = random.choices(emoji, weights=weights, k=1)
        print(f"\r                     Slot: {a[0]} {b[0]} {c[0]}", end="", flush=True)
        time.sleep(0.1)
    tries += 1
    print()

    if a[0] == "🍇" and b[0] == "🍇" and c[0] == "🍇":
        print("                     MEGA JACKPOT")
        grape_won += 1
    elif a[0] == "🍎" and b[0] == "🍎" and c[0] == "🍎":
        print("                     Minor prize")
        apple_won += 1
    elif a[0] == "🍑" and b[0] == "🍑" and c[0] == "🍑":
        print("                     You won nothing")
        peach_won += 1
    elif a[0] == "🍓" and b[0] == "🍓" and c[0] == "🍓":
        print("                     Minor prize")
        strawberry_won += 1
    elif a[0] == "🍒" and b[0] == "🍒" and c[0] == "🍒":
        print("                     Minor prize")
        cherry_won += 1

print("Grape has won:", grape_won)
print("Cherry has won:", cherry_won)
print("Strawberry has won:", strawberry_won)
print("Apple has won:", apple_won)
print("Peach has won:", peach_won)