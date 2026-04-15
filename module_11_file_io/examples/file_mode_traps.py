# file mode traps - the stuff that makes your data disappear or look wrong
# file I/O is simple but these gotchas get everyone at least once

import os


# === TRAP 1: write mode destroys everything ===
# 'w' doesn't mean "add to the file" - it means "delete everything and start fresh"
print("=== Trap 1: Write Mode Destroys Everything ===")

# create a file with some data
with open("trap1.txt", "w") as f:
    f.write("Important data line 1\n")
    f.write("Important data line 2\n")
    f.write("Important data line 3\n")

# read it back to prove it's there
with open("trap1.txt", "r") as f:
    print("Before 'w' mode:")
    print(f.read())

# now open it in 'w' mode to "add" one line
with open("trap1.txt", "w") as f:
    f.write("Just one new line\n")

# everything else is gone
with open("trap1.txt", "r") as f:
    print("After 'w' mode:")
    print(f.read())
    # only "Just one new line" - the other 3 lines are gone forever

# the fix: use 'a' for append mode
with open("trap1.txt", "a") as f:
    f.write("This line is added without deleting anything\n")

with open("trap1.txt", "r") as f:
    print("After 'a' mode:")
    print(f.read())
print()


# === TRAP 2: forgetting \n when writing ===
# write() does NOT add newlines for you like print() does
print("=== Trap 2: Forgetting Newlines ===")

with open("trap2.txt", "w") as f:
    f.write("Line 1")
    f.write("Line 2")
    f.write("Line 3")

with open("trap2.txt", "r") as f:
    print("Without \\n:")
    print(f.read())        # Line 1Line 2Line 3  (all smashed together)

# the fix: always add \n
with open("trap2.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open("trap2.txt", "r") as f:
    print("With \\n:")
    print(f.read())
print()


# === TRAP 3: not stripping \n when reading ===
# readlines() keeps the \n at the end of each line
# this causes invisible bugs when you try to compare or process strings
print("=== Trap 3: Invisible \\n When Reading ===")

with open("trap2.txt", "r") as f:
    lines = f.readlines()

print(f"Raw lines: {lines}")        # ['Line 1\n', 'Line 2\n', 'Line 3\n']

# this comparison fails because of the hidden \n
if lines[0] == "Line 1":
    print("Match!")
else:
    print(f"No match! '{lines[0]}' != 'Line 1'")    # no match because of \n

# the fix: strip each line
clean_lines = [line.strip() for line in lines]
print(f"Clean lines: {clean_lines}")   # ['Line 1', 'Line 2', 'Line 3']

if clean_lines[0] == "Line 1":
    print("Now it matches!")
print()


# === TRAP 4: writing numbers without str() ===
# write() only accepts strings - passing a number crashes
print("=== Trap 4: Writing Numbers ===")

age = 25
score = 95.5

try:
    with open("trap4.txt", "w") as f:
        f.write(age)        # TypeError!
except TypeError as e:
    print(f"Error: {e}")
    print("write() only accepts strings - you have to convert first")

# the fix: convert to string
with open("trap4.txt", "w") as f:
    f.write(str(age) + "\n")
    f.write(str(score) + "\n")
    # or use f-strings
    f.write(f"{age}\n")
    f.write(f"{score}\n")

with open("trap4.txt", "r") as f:
    print("Fixed version:")
    print(f.read())


# === TRAP 5: not using with - the file that never closes ===
# if an error happens between open() and close(), the file stays open
print("=== Trap 5: File Never Closes ===")

# BAD - if an error happens, close() never runs
try:
    f = open("trap5.txt", "w")
    f.write("Some data\n")
    # imagine an error happens here
    result = 1 / 0           # ZeroDivisionError!
    f.close()                 # this line never runs
except ZeroDivisionError:
    print("Error happened - file.close() was skipped!")
    f.close()                 # now you have to close it in the except block too

# GOOD - with always closes the file, even if an error happens
try:
    with open("trap5.txt", "w") as f:
        f.write("Some data\n")
        result = 1 / 0       # error happens
except ZeroDivisionError:
    print("Error happened - but 'with' already closed the file safely")
print()


# === TRAP 6: reading a file that doesn't exist ===
# without try/except, FileNotFoundError crashes your program
print("=== Trap 6: File Not Found ===")

# BAD - crashes
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError - always wrap file reads in try/except")

# GOOD - handle it gracefully
filename = "nonexistent_file.txt"
try:
    with open(filename, "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print(f"'{filename}' not found. Check the path and filename.")
print()


# cleanup temp files
for f in ["trap1.txt", "trap2.txt", "trap4.txt", "trap5.txt"]:
    if os.path.exists(f):
        os.remove(f)
print("(temp files cleaned up)")


# === QUICK REFERENCE ===
# 1. 'w' = write = DELETE EVERYTHING and start over
# 2. 'a' = append = add to the end, keep existing content
# 3. write() does NOT add \n - you have to do it yourself
# 4. readlines() keeps \n on every line - use .strip() to remove
# 5. write() only takes strings - use str() or f-strings for numbers
# 6. always use 'with open' so the file closes even if errors happen
# 7. always wrap file reads in try/except for FileNotFoundError