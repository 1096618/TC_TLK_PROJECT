# -----------------------------------------------------------------------------
# Name:        Student list menu
# Purpose:     Write a program that have multiple function that can modify the student list.
#
# Author:      TC
# Created:     March 24, 2025
# -----------------------------------------------------------------------------

import copy

studentlist = [
    {"name": "Charlie", "age": 24, "major": "Biology"},
    {"name": "Bob","age": 22,"major": "Chemistry"},
    {"name": "Frank","age": 26,"major": "Physics"},
    {"name": "Alice Milad","age": 25,"major": "Physics"},
    {"name": "Jinwoo","age": 18,"major": "Criminology"},
    {"name": "Maddy", "age": 20, "major": "Music"},
    {"name": "Alice Wonder", "age": 19, "major": "Art"},
    {"name": "Malice Mephis", "age": 34, "major": "English"},
]

copystudentlist = copy.deepcopy(studentlist)

#DISPLAY CURRENT LIST
def displaycurrentlist():
    print("                 |Student list|")
    for index, student in enumerate(copystudentlist, start=1):
        print(f"{index}. Student Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

def displayoglist():
    print("                 |Student list|")
    for index, student in enumerate(studentlist, start=1):
        print(f"{index}. Student Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")


#MODIFYING STUDENT NAME/AGE/MAJOR
def modifying():
    displayoglist()
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("|Modifying student list|")
    while True:
        stid = int(input("Which student id do you want to modify?(number) "))
        student = studentlist[stid - 1]  # Get student index
        print(f"Student name: {student['name']}, Age: {student['age']}, Major: {student['major']} has been selected")

        #MODIFY NAME/AGE/MAJOR OF THE SELECTED STUDENT
        while True:
            mcond1 = input("What do you want to modify?(name/age/major) ")
            if mcond1 == "name":
                student["name"] = input("Input name: ")
                print("Name has been modified")
            elif mcond1 == "age":
                student["age"] = int(input("Input age: "))
                print("Age has been modified")
            elif mcond1 == "major":
                student["major"] = input("Input major: ")
                print("Major has been modified")
            else:
                print("Invalid input")
                break

            #KEEP MODIFYING SAME STUDENT
            mcond2 = input("Would you like to continue modifying?(y/n) ")
            if mcond2 == "y":
                continue
            else:
                print(f"New student id Student name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
                break

        #MODIFIY NEW STUDENT
        mcond3 = input("Would you like to modify another student?(y/n) ")
        if mcond3 == "y":
            continue
        else:
            print("Returning to main menu")
            break
    #Since we are modifying the original student list and it only display copy student list
    #we need to copy the new student list to copy student list
    global copystudentlist
    copystudentlist = copy.deepcopy(studentlist)

#SORTING NAME/AGE/MAJOR
def sorting():
    print("|Sorting student list|")
    while True:
        scond1 = input("Which categories would you like to sort by?(name/age/major) ")

        #SORTING BY NAME
        if scond1 == "name":
            namecond1 = input("Sort by alphabet or length(alp/len) ")
            namecond2 = input("And ascending or descending (asc/desc) ")
            if namecond1 == "alp" and namecond2 == "asc":
                copystudentlist.sort(key=lambda x: x["name"])
                print() #Leave empty line for better visual
                print("Name has been sorted alphabetically with ascending order!")
                displaycurrentlist()
            elif namecond1 == "alp" and namecond2 == "desc":
                copystudentlist.sort(key=lambda x: x["name"], reverse=True)
                print()  # Leave empty line for better visual
                print("Name has been sorted alphabetically with descending order!")
                displaycurrentlist()
            elif namecond1 == "len" and namecond2 == "asc":
                copystudentlist.sort(key=lambda x: len(x["name"]))
                print()  # Leave empty line for better visual
                print("Name has been sorted by length with ascending order!")
                displaycurrentlist()
            elif namecond1 == "len" and namecond2 == "desc":
                copystudentlist.sort(key=lambda x: len(x["name"]), reverse=True)
                print()  # Leave empty line for better visual
                print("Name has been sorted by length with descending order!")
                displaycurrentlist()
            else:
                print("Invalid input")
                break

        #SORTING BY AGE
        elif scond1 == "age":
            agecond1 = input("Sort by ascending or descending (asc/desc) ")
            if agecond1 == "asc":
                copystudentlist.sort(key=lambda x: x["age"])
                print()  # Leave empty line for better visual
                print("Age has been sorted with ascending order!")
                displaycurrentlist()
            elif agecond1 == "desc":
                copystudentlist.sort(key=lambda x: x["age"], reverse=True)
                print()  # Leave empty line for better visual
                print("Age has been sorted with descending order!")
                displaycurrentlist()
            else:
                print("Invalid input")
                break

        #SORTING BY MAJOR
        elif scond1 == "major":
            majorcond1 = input("Sort by alphabet or length(alp/len) ")
            majorcond2 = input("And ascending or descending (asc/desc) ")
            if majorcond1 == "alp" and majorcond2 == "asc":
                copystudentlist.sort(key=lambda x: x["major"])
                print()  # Leave empty line for better visual
                print("Major has been sorted alphabetically with ascending order!")
                displaycurrentlist()
            elif majorcond1 == "alp" and majorcond2 == "desc":
                copystudentlist.sort(key=lambda x: x["major"], reverse=True)
                print()  # Leave empty line for better visual
                print("Major has been sorted alphabetically with descending order!")
                displaycurrentlist()
            elif majorcond1 == "len" and majorcond2 == "asc":
                copystudentlist.sort(key=lambda x: len(x["major"]))
                print()  # Leave empty line for better visual
                print("Major has been sorted by length with ascending order!")
                displaycurrentlist()
            elif majorcond1 == "len" and majorcond2 == "desc":
                copystudentlist.sort(key=lambda x: len(x["major"]), reverse=True)
                print()  # Leave empty line for better visual
                print("Major has been sorted by length with descending order!")
                displaycurrentlist()
            else:
                print("Invalid input")
                break

        else:
            print("Invalid input")
            break

        scond2 = input("Continue sorting?(y/n) ")
        if scond2 == "y":
            print()  # Leave empty line for better visual
            continue
        else:
            print("Returning to main menu")
            break

#FILTERING/SEARCHING
def filtering():
    print("|Filtering student list|")
    while True:
        fcond1 = input("Which categories would you like to filter(name/age/major) ")

        #FILTER NAME
        if fcond1 == "name":
            fncond1 = input("Filter by word or starting with letter(word/letter) ")

            #FILTER NAME BY WORD
            if fncond1 == "word":
                word = input("Type in what do you want to filter by: ")
                filteredlist = list(filter(lambda x: word in x["name"].lower().split(), studentlist))
                print(f"There are {len(filteredlist)} results in the list:")
                for index, item in enumerate(filteredlist, start=1):
                    print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                global copystudentlist
                copystudentlist = copy.deepcopy(filteredlist)

            #FILTER NAME BY LETTER
            elif fncond1 == "letter":
                letter = input("Type in the letter you want to filter by: ")
                filteredlist = list(filter(lambda x: x["name"].lower().startswith(letter), studentlist))
                print(f"There are {len(filteredlist)} results in the list:")
                for index, item in enumerate(filteredlist, start=1):
                    print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                copystudentlist = copy.deepcopy(filteredlist)
            else:
                print("Invalid input")
                break

        #FILTER MAJOR
        elif fcond1 == "major":
            fmcond1 = input("Filter by word or starting with letter(word/letter) ")

            #FILTER NAME BY WORD
            if fmcond1 == "word":
                word = input("Type in what do you want to filter by: ")
                filteredlist = list(filter(lambda x: word in x["major"].lower().split(), studentlist))
                print(f"There are {len(filteredlist)} results in the list:")
                for index, item in enumerate(filteredlist, start=1):
                    print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                copystudentlist = copy.deepcopy(filteredlist)

            #FILTER NAME BY LETTER
            elif fmcond1 == "letter":
                letter = input("Type in the letter you want to filter by: ")
                filteredlist = list(filter(lambda x: x["major"].lower().startswith(letter), studentlist))
                print(f"There are {len(filteredlist)} results in the list:")
                for index, item in enumerate(filteredlist, start=1):
                    print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                copystudentlist = copy.deepcopy(filteredlist)
            else:
                print("Invalid input")
                break

        #FILTER AGE
        elif fcond1 == "age":
            facond1 = input("Filter by within a range or above/below value(range/value) ")

            #FILTER AGE BY RANGE
            if facond1 == "range":
                minage = int(input("Input minimum age: "))
                maxage = int(input("Input maximum age: "))
                filteredlist = list(filter(lambda x: minage <= x["age"] <= maxage , studentlist))
                print(f"There are {len(filteredlist)} results in the list:")
                filteredlist.sort(key=lambda x: x["age"])
                for index, item in enumerate(filteredlist, start=1):
                    print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                    copystudentlist = copy.deepcopy(filteredlist)

            #FILTER AGE BY VALUE
            elif facond1 == "value":
                age = int(input("Input age: "))
                agecond = input("Above or Below age: ")

                if agecond == "above":
                    filteredlist = list(filter(lambda x: age <= x["age"], studentlist))
                    print(f"There are {len(filteredlist)} results in the list:")
                    filteredlist.sort(key=lambda x: x["age"])
                    for index, item in enumerate(filteredlist, start=1):
                        print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                        copystudentlist = copy.deepcopy(filteredlist)

                elif agecond == "below":
                    filteredlist = list(filter(lambda x: age >= x["age"], studentlist))
                    print(f"There are {len(filteredlist)} results in the list:")
                    filteredlist.sort(key=lambda x: x["age"])
                    for index, item in enumerate(filteredlist, start=1):
                        print(f"{index}. Student Name: {item['name']}, Age: {item['age']}, Major: {item['major']}")
                        copystudentlist = copy.deepcopy(filteredlist)

                else:
                    print("Invalid input")
                    break

            else:
                print("Invalid input")
                break

        else:
            print("Invalid input")
            break
        fcond2 = input("Continue filtering?(y/n) ")
        if fcond2 == "y":
            continue
        else:
            print("Returning to main menu")
            break

#ADDING
def adding():
    print("|Adding a student to list|")
    while True:
        name = input("Input name: ")
        age = int(input("Input age: "))
        major = input("Input major: ")
        studentlist.append({"name": name, "age": age, "major": major})
        print(f"{name} added to student list")
        print(f"Student name: {name}, Age: {age}, Major: {major}")

        addcond1 = input("Continue adding?(y/n) ")
        if addcond1 == "y":
            continue
        else:
            print("Returning to main menu")
            break
    #Since we are adding to original student list
    #we need to copy the new student list to copy student list
    global copystudentlist
    copystudentlist = copy.deepcopy(studentlist)

#DELETE
def deleting():
    print("|Deleting a student in student list|")
    #print("The current list:")
    displayoglist()
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    while True:
        stid = int(input("Which student id do you want to delete?(number) "))
        student = studentlist[stid - 1] #Get student index
        print(f"Student name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
        twofa = input("Confirm delete student?(y/n) ")
        if twofa == "y":
            studentlist.remove(student)
            print(f"{student['name']} has been deleted from student list")
        else:
            dcond1 = input("Continue deleting?(y/n) ")
            if dcond1 == "y":
                continue
            else:
                print("Returning to main menu")
                break
        dcond1 = input("Continue deleting?(y/n) ")
        if dcond1 == "y":
            continue
        else:
            print("Returning to main menu")
            break
    #Since we are adding to original student list
    #we need to copy the new student list to copy student list
    global copystudentlist
    copystudentlist = copy.deepcopy(studentlist)

#reset
def listreset():
    global copystudentlist
    copystudentlist = copy.deepcopy(studentlist)

while True:
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("""          Welcome to the student list menu
      There are 7 function you can choose from:
          1. View student list(view)
          2. Modify student list(modify)
          3. Sort student list(sort)
          4. Filter student list(filter)
          5. Add a student to list(add)
          6. Delete a student from list(delete)
          7. Reset list format(reset)\n""")

    command = input("          Enter your choice: ")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    if command == "view" or command == "1":
        displaycurrentlist()
    elif command == "modify" or command == "2":
        modifying()
    elif command == "sort" or command == "3":
        sorting()
    elif command == "filter" or command == "4":
        filtering()
    elif command == "add" or command == "5":
        adding()
    elif command == "delete" or command == "6":
        deleting()
    elif command == "reset" or command == "7":
        listreset()
    else:
        print("Invalid input")
        break


