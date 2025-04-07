Probem: Update a set with a set and discard an item from a set

Pseudo code:
1. Create 2 set 
    - `set1 = {"item1", "item3", "item4"}`
    - `set2 = {"item2", "item1", "item5"}`
2. Ask user do they want to update or discard 
    1. Ask user to update set 1 to 2 or set 2 to 1
       1. Set 1 to 2 `set1.update(set2)`
       2. Set 2 to 1 `set2.update(set1)`
    2. Ask user which set do they want to discard
        1. Set 1: Ask user to input item to discard `set1.discard(item_to_discard)`
        2. Set 2: Ask user to input item to discard `set2.discard(item_to_discard)`
        