# nested loop common mistakes - the stuff that trips everyone up
# and the right way to do it


# === MISTAKE 1: using the same variable name in both loops ===
# the inner loop overwrites the outer loop's variable
print("=== Same variable name (wrong) ===")
for i in range(3):
    for i in range(2):  # WRONG - this overwrites the outer i
        print(i, end=" ")
    print(f"  ← outer i is now {i}")
# after the inner loop, i is whatever the inner loop left it as
# you lose track of which row you're on
print()

# the fix: use different names
print("=== Different variable names (correct) ===")
for i in range(3):
    for j in range(2):  # j is separate from i
        print(f"({i},{j})", end=" ")
    print(f"  ← outer i is still {i}")
# i stays as expected, j does its own thing
print()


# === MISTAKE 2: forgetting to reset the inner variable in while loops ===
# for loops reset automatically, while loops don't
print("=== Forgot to reset j (wrong) ===")
i = 0
j = 0  # j starts at 0 out here
while i < 3:
    # j is already 3 from the first run, so inner loop never runs again
    while j < 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print(f"  ← j is {j}, inner loop won't run again")
    i += 1
# only prints the first row because j stays at 3
print()

# the fix: reset j inside the outer loop
print("=== Reset j inside outer loop (correct) ===")
i = 0
while i < 3:
    j = 0  # THIS IS THE KEY - reset j every time
    while j < 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
# for loops do this automatically, which is why they're easier for nested loops
print()


# === MISTAKE 3: thinking break exits ALL loops ===
# break only exits the innermost loop it's inside
print("=== break only exits inner loop ===")
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # only exits the j loop, not the i loop
        print(f"({i},{j})", end=" ")
    print(f"  ← i={i} still runs, break only killed the inner loop")
# you get (0,0), (1,0), (2,0) - the outer loop keeps going
print()

# if you need to break out of BOTH loops, use a flag
print("=== Breaking both loops with a flag ===")
found = False
for i in range(5):
    for j in range(5):
        print(f"checking ({i},{j})...", end=" ")
        if i * j == 12:
            print(f"FOUND IT! {i} * {j} = 12")
            found = True
            break  # exits inner loop
    if found:
        break  # exits outer loop
# without the flag + second break, the outer loop would keep searching
print()


# === MISTAKE 4: off-by-one with 2D list indices ===
# using len(grid) for both rows AND columns
print("=== Off-by-one with grid indices ===")
grid = [[1, 2], [3, 4], [5, 6]]
# this grid has 3 rows and 2 columns
# len(grid) = 3 (rows), len(grid[0]) = 2 (columns)

# WRONG way - using len(grid) for columns too
print("Wrong (crashes on non-square grids):")
try:
    for i in range(len(grid)):
        for j in range(len(grid)):  # WRONG - should be len(grid[i])
            print(grid[i][j], end=" ")
        print()
except IndexError as e:
    print(f"  IndexError: {e}")
    print("  because len(grid) is 3 but each row only has 2 columns")
print()

# RIGHT way - use len(grid[i]) for columns
print("Correct:")
for i in range(len(grid)):
    for j in range(len(grid[i])):  # columns = len of current row
        print(grid[i][j], end=" ")
    print()
print()


# === MISTAKE 5: wrong indentation changes everything ===
# where you put print() determines if it's inside or outside the inner loop
print("=== print() inside inner loop (wrong for grid) ===")
for i in range(3):
    for j in range(3):
        print("*", end="")
        print()  # WRONG - this is inside the inner loop, newline after every star
# you get each star on its own line instead of a row
print()

print("=== print() outside inner loop (correct for grid) ===")
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()  # RIGHT - newline after the inner loop finishes the row
# you get a proper 3x3 grid
print()


# === QUICK REFERENCE ===
# 1. Use different variable names for outer and inner loops
# 2. In while loops, reset the inner variable INSIDE the outer loop
# 3. break only exits ONE loop - use a flag for multiple
# 4. For 2D lists: rows = len(grid), columns = len(grid[i])
# 5. Check your indentation - one tab changes which loop owns the line
