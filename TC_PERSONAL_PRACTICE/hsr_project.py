gem = int(input("How much gem do you have in HSR rn: "))
char = input("What character do you want next: ")
#dividing into pull and rounding
pull = gem//160
   #rpull = round(pull)
   #round() function will round to nearest integer for an example
   #9.6 -> 10 and 9.4 -> 9
   #// integer division will round to nearest integer toward negative infinity
#comparing number
print("=========================================================")
#broke case
if gem <= 160:
    print(f"Boi you aint getting {char} with {gem} gems")
#pray case
if gem > 160 and gem <= 1600:
    print(f"Better go pray RNGESUS to get {char} in {pull} pulls")
#okay case
if gem > 1600 and gem <= 8000:
    print(f"You have a chance to get {char} in {pull} pulls")
#50/50 case
if gem > 8000 and gem <= 14400:
    print(f"Pray you shall win 50/50 to get {char} in {pull} pulls")
#whale
if gem > 14400 and gem <=100000:
#eidolon case
    qes = input("Boi are you trying to get multiple eidolon? (yes/no)").strip().lower()
    if qes == "yes":
        eid = input("What eidolons? ")
#checking the required amount
        if eid == "1":
            if pull >= 180:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 180 pulls.")

        elif eid == "2":
            if pull >= 360:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 360 pulls.")

        elif eid == "3":
            if pull >= 540:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 540 pulls.")

        elif eid == "4":
            if pull >= 720:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 720 pulls.")

        elif eid == "5":
            if pull >= 900:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 900 pulls.")

        elif eid == "6":
            if pull >= 1080:
                print(f"Guaranteed {char} with {pull} pulls!")
            else:
                print(f"Better win 50/50 with {pull} pulls! You need a minimum of 1080 pulls.")

        else:
            print(f"Invalid eidolon choice.")
    else:
        print(f"Why the hell are you saving {pull} pulls for 1 {char}?!?!")
else:
    print(f"Aint no way you have {gem} gems AKA {pull} pulls!")

    

    

