name = input('Name: ')
counter = 0
if name == 'gps':
    while counter < 5:  # Loop until counter reaches 5
        passw = input('Password: ')

        if passw == "correct":
            print('Password is correct.')
            break  # Exit the loop when the correct password is entered

        else:
            print('Wrong password.')
            counter += 1  # Increment counter for incorrect attempts
        if counter == 5:
            print('Too many wrong attempts.')
            break
else:
    print("Name not in database")
