Problem: Create a program that adds and removes element from a set

Additional additions: Choosing what to do and loop doing till done

Pseudo code:

Module adding:
1. Ask user to input new color `new_color = input("Input color")`
2. Add new color into color set `color.add(new_color)`

Module removing:
1. Ask user to input color to remove `removed_color = input("Input color")`
2. Check if color in set `if removed_color in color`
3. If color exist then remove `color.remove(removed_color)`

Logic:
1. User input command (add/remove/view)
2. Add:
    - Loop `Module adding`
    - When user input done break out of loop and return to input command
3. Remove:
    - Loop `Module removing`
    - When user input done break out of loop and return to input command
4. View:
   - Print curent color set
5. Else:
   - Break loop and quit