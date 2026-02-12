# copy vs reference - one of the sneakiest bugs in Python

# THE PROBLEM: assignment doesn't copy a list
original = [1, 2, 3]
not_a_copy = original  # this does NOT make a copy

not_a_copy[0] = 99  # change the "copy"
print(f"original:   {original}")  # [99, 2, 3]  <-- it changed too!
print(f"not_a_copy: {not_a_copy}")  # [99, 2, 3]

# they are the SAME list in memory, just two names for it
print(f"same object? {original is not_a_copy}")  # True

print()

# THE FIX: use slicing [:] or .copy() to make an actual copy
original = [1, 2, 3]
actual_copy = original[:]  # this DOES make a copy
also_a_copy = original.copy()  # this also works

actual_copy[0] = 99
print(f"original:    {original}")  # [1, 2, 3]  <-- unchanged!
print(f"actual_copy: {actual_copy}")  # [99, 2, 3]
print(f"same object? {original is actual_copy}")  # False

print()

# WHY THIS MATTERS - a realistic example
# say you want to keep the original grades and make a modified version
grades = [85, 92, 78, 96]

# wrong way
adjusted = grades
adjusted[2] = 80
print(f"grades (oops):   {grades}")  # [85, 92, 80, 96] - original is ruined

# right way
grades = [85, 92, 78, 96]  # reset
adjusted = grades[:]  # actual copy
adjusted[2] = 80
print(f"grades (safe):   {grades}")  # [85, 92, 78, 96] - original is safe
print(f"adjusted:        {adjusted}")  # [85, 92, 80, 96]
