basic_tuple = ("hello", True, 2, 3.14, ("World", "Gaia"))

#Loop printing woooooooo
print(f"There are {len(basic_tuple)} items in the tuple.") #Get length or how many item in tuple
while True:
    index = int(input("Enter a number between 1 and 5: "))
    if index >= 1 and index <= 5: #Check if index within valid range of item in tuple
        print(basic_tuple[index-1])
    else:
        print("Item out of range.")
        break