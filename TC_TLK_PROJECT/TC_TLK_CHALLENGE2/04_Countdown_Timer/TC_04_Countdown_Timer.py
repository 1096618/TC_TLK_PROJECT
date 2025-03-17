import time
countdown = int(input("How many second to countdown to? "))
while countdown > 0:
    stop = input()
    if stop == "stop":
        break
    print(countdown)
    countdown -= 1
    time.sleep(1)


