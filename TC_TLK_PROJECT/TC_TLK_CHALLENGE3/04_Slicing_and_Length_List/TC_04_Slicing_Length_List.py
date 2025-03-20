#WIP DONT EDIT EXCEPT ME OFC


placeholder = ["first", "second", "third"]
grocerylist = ["pen", "pineapple", "apple", "ballpoint pen", "pineapple pen", "apple pen"]
print("The current grocery list is:", ", ".join(grocerylist))
#print(len(grocerylist))



#itemab = input("What item would you like to slice ")
#itema, itemb = itemab.split()
#print(f"{itema} and {itemb}")
#slicedlist = grocerylist[grocerylist.index(itema):grocerylist.index(itemb)]
#print("The current grocery list is:", ", ".join(slicedlist))

cond1 = int(input("How many items would you like to slice?(0-3, and only next to each others plz) "))
if cond1 > 3:
    print("Invalid input")
    exit()
for i in range(cond1):
    cond2 = input(f"what {placeholder[0]} would you like to slice? ")
    placeholder.remove(0)
