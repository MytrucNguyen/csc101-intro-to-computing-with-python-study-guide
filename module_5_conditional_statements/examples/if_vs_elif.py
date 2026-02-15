# if vs elif - why the difference matters
# Pokemon levels as an example

level = 36

# WRONG WAY: using multiple if statements
# ALL of these get checked, so multiple can run
print("=== Multiple if statements (wrong) ===")
if level >= 36:
    print("Charizard!")  # this runs
if level >= 16:
    print("Charmeleon!")  # this ALSO runs (36 >= 16 is True)
if level >= 1:
    print("Charmander!")  # this ALSO runs (36 >= 1 is True)

# you get all three, which doesn't make sense
# a Pokemon should only be one evolution at a time

print()

# RIGHT WAY: using elif
# only the FIRST match runs, then the rest is skipped
print("=== elif chain (correct) ===")
if level >= 36:
    print("Charizard!")  # this runs
elif level >= 16:
    print("Charmeleon!")  # skipped (already matched above)
elif level >= 1:
    print("Charmander!")  # skipped

# you get just Charizard, which is correct

print()

# try changing the level to see different results
level = 10

print(f"=== Level {level} ===")
if level >= 36:
    print("Charizard!")
elif level >= 16:
    print("Charmeleon!")
elif level >= 1:
    print("Charmander!")
else:
    print("No Pokemon yet!")
