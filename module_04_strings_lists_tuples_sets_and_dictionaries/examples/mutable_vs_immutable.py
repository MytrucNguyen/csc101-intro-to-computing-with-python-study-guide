# mutable vs immutable - why this matters

# STRINGS are immutable (can't change them)
name = "hello"
# name[0] = "H"   # this would crash with TypeError

# string methods don't change the original, they return a NEW string
upper_name = name.upper()
print(f"original: {name}")  # still "hello"
print(f"new string: {upper_name}")  # "HELLO"

# if you want to "change" a string, you reassign it
name = name.upper()
print(f"reassigned: {name}")  # now "HELLO"

print()

# LISTS are mutable (you CAN change them)
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"  # this works fine
print(f"modified list: {fruits}")  # ["avocado", "banana", "cherry"]

print()

# TUPLES are immutable (like strings, can't change them)
coordinates = (10, 20)
# coordinates[0] = 15   # this would crash with TypeError
print(f"tuple: {coordinates}")

# to "change" a tuple, you have to make a new one
coordinates = (15, 25)
print(f"new tuple: {coordinates}")

print()

# quick reference
print("=== Quick Reference ===")
print("Mutable (can change):   list, set, dict")
print("Immutable (can't change): str, tuple, int, float, bool")
