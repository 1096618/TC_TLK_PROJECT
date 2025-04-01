import random

emoji = ["🍎", "🍓", "🍇", "🍒", "🍑"]
weights = [55, 35, 12, 20, 80]
# apple = 55, strawberry = 35, grape = 12, cherry = 20, peach = 80


grape_won = 0  # 🍇 tracker
cherry_won = 0  # 🍒 tracker
strawberry_won = 0  # 🍓 tracker
apple_won = 0  # 🍎 tracker
peach_won = 0  # ass tracker

tries_limit = 100000
simulation = "h" #change depending on you doing high amount of tries or low (high/h / low/l)
tries = 0 #DONT CHANGE THIS

while True:

    if tries >= tries_limit:
        print(f"{tries_limit} tries reached! Stopping slot machine...!")
        break

    for i in range(1):
        a = random.choices(emoji, weights=weights, k=1)
        b = random.choices(emoji, weights=weights, k=1)
        c = random.choices(emoji, weights=weights, k=1)
    tries += 1

    if a[0] == "🍇" and b[0] == "🍇" and c[0] == "🍇":
        grape_won += 1
    elif a[0] == "🍎" and b[0] == "🍎" and c[0] == "🍎":
        apple_won += 1
    elif a[0] == "🍑" and b[0] == "🍑" and c[0] == "🍑":
        peach_won += 1
    elif a[0] == "🍓" and b[0] == "🍓" and c[0] == "🍓":
        strawberry_won += 1
    elif a[0] == "🍒" and b[0] == "🍒" and c[0] == "🍒":
        cherry_won += 1

lose_count = tries_limit - grape_won - cherry_won - strawberry_won - apple_won - peach_won
grape_percentage = (grape_won/tries_limit)*100
cherry_percentage = (cherry_won/tries_limit)*100
strawberry_percentage = (strawberry_won/tries_limit)*100
apple_percentage = (apple_won/tries_limit)*100
peach_percentage = (peach_won/tries_limit)*100
lose_percentage = (lose_count/tries_limit)*100
win_percentage = 100 - lose_percentage

if simulation == "low" or simulation == "l":
        #IF doing low tries simulation
    print(f"Grape has won: {grape_won} | Winrate: {grape_percentage:.2f}%")
    print(f"Cherry has won: {cherry_won} | Winrate: {cherry_percentage:.2f}%")
    print(f"Strawberry has won: {strawberry_won} | Winrate: {strawberry_percentage:.2f}%")
    print(f"Apple has won: {apple_won} | Winrate: {apple_percentage:.2f}%")
    print(f"Peach has won: {peach_won} | Winrate: {peach_percentage:.2f}%")
    print(f"Lost: {lose_count} | Loserate: {lose_percentage:.2f}%")
else:
        #IF doing high tries simulation and want "1 in..."
    print(f"Grape has won: {grape_won} | Winrate: {grape_percentage:.2f}% | 1 in {1/(grape_percentage/100):,.0f}")
    print(f"Cherry has won: {cherry_won} | Winrate: {cherry_percentage:.2f}% | 1 in {1/(cherry_percentage/100):,.0f}")
    print(f"Strawberry has won: {strawberry_won} | Winrate: {strawberry_percentage:.2f}% | 1 in {1/(strawberry_percentage/100):,.0f}")
    print(f"Apple has won: {apple_won} | Winrate: {apple_percentage:.2f}% | 1 in {1/(apple_percentage/100):,.0f}")
    print(f"Peach has won: {peach_won} | Winrate: {peach_percentage:.2f}% | 1 in {1/(peach_percentage/100):,.0f}")
    print(f"Lost: {lose_count} | Loserate: {lose_percentage:.2f}% | 1 in {1 / (win_percentage / 100):,.0f}")