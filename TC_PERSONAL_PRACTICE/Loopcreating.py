count = 0
a = "a"
while count < 50:
    print(a)

    if count < 25:
        a += "a"  # Add an "a" to the string (growing)
    else:
        a = a[:-1]  # Remove the last "a" from the string (shrinking)

    count += 1

    # Break when count reaches 50
    if count == 50:
        break