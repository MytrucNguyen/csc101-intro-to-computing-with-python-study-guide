# slicing explained - the off-by-one thing that trips everyone up

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#  index:    0        1         2        3         4

# the rule: list[start:stop]
# start = included
# stop  = NOT included (this is the confusing part)

# think of it as "start up to but not including stop"
print(fruits[1:3])  # ["banana", "cherry"]  (index 1 and 2, NOT 3)
print(fruits[0:2])  # ["apple", "banana"]   (index 0 and 1, NOT 2)

# leaving start empty = start from the beginning
print(fruits[:3])  # ["apple", "banana", "cherry"]

# leaving stop empty = go to the end
print(fruits[2:])  # ["cherry", "date", "elderberry"]

# negative indexing works too
print(fruits[-2:])  # ["date", "elderberry"] (last 2 items)

print()

# this works the EXACT same way with strings
word = "dinosaur"
#       01234567

print(word[0:4])  # "dino"  (index 0, 1, 2, 3 -- NOT 4)
print(word[4:])  # "saur"  (index 4 to the end)
print(word[::-1])  # "ruasonid" (reversed)

print()

# common mistake: thinking [1:3] gives you 3 items
# it gives you (stop - start) items: 3 - 1 = 2 items
numbers = [10, 20, 30, 40, 50]
print(f"numbers[1:3] = {numbers[1:3]}")  # [20, 30] -- 2 items, not 3
print(f"numbers[1:4] = {numbers[1:4]}")  # [20, 30, 40] -- 3 items
