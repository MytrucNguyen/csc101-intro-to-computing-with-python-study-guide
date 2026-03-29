# scope traps - the stuff that makes you stare at your screen wondering why it broke
# variable scope is simple in theory but the edge cases get everyone


# === TRAP 1: same variable name inside and outside a function ===
# they look like the same variable but they're completely separate
print("=== Same Name, Different Variable ===")

rate = 0.05    # global

def show_rate():
    rate = 0.75    # this is a NEW local variable, not the global one
    print(f"Inside function: {rate}")     # 0.75

show_rate()
print(f"Outside function: {rate}")        # 0.05 (unchanged!)

# the function created its own local 'rate' that disappeared when the function ended
# the global 'rate' was never touched
print()


# === TRAP 2: trying to modify a global variable without the global keyword ===
# reading a global works fine, but writing to it breaks
print("=== Reading vs Writing Global Variables ===")

score = 100

# reading works fine
def print_score():
    print(f"Score is: {score}")    # no problem, just reading

print_score()

# writing without global keyword breaks
def add_bonus():
    try:
        score += 10    # Error! Python sees the assignment and thinks score is local
    except UnboundLocalError as e:
        print(f"Error: {e}")
        print("Python saw 'score +=' and assumed score is local")
        print("But you never created a local score, so it crashed")

add_bonus()
print()

# the fix: use the global keyword
def add_bonus_fixed():
    global score
    score += 10
    print(f"Score after bonus: {score}")

add_bonus_fixed()    # Score after bonus: 110
print()


# === TRAP 3: local variables don't exist outside the function ===
# this one seems obvious but people forget it in longer programs
print("=== Local Variables Disappear ===")

def calculate_tax(amount):
    tax = amount * 0.08    # tax is local to this function
    total = amount + tax   # total is also local
    return total

result = calculate_tax(100)
print(f"Total: {result}")

# these don't exist out here
try:
    print(tax)
except NameError:
    print("'tax' doesn't exist outside the function")

try:
    print(total)
except NameError:
    print("'total' doesn't exist either")

# if you need the value outside, you have to return it
print()


# === TRAP 4: the better way - parameters and return values ===
# instead of messing with global variables, pass data in and get data out
print("=== Global vs Parameters (the right way) ===")

# BAD way - uses global
lives = 3

def lose_life_bad():
    global lives
    lives -= 1

lose_life_bad()
print(f"Bad way - lives: {lives}")    # 2, but now any function can mess with lives

# GOOD way - parameters and return
def lose_life_good(current_lives):
    return current_lives - 1

lives = 3
lives = lose_life_good(lives)
print(f"Good way - lives: {lives}")    # 2, and you control exactly when it changes

# the good way is easier to debug because you can see exactly
# where lives changes - it's right there in the assignment
print()


# === TRAP 5: function arguments are copies (for simple types) ===
# changing a parameter inside a function doesn't change the original
print("=== Parameters Are Copies ===")

def try_to_change(x):
    x = 999
    print(f"Inside function: x = {x}")

my_value = 42
try_to_change(my_value)
print(f"Outside function: my_value = {my_value}")    # still 42

# the function got a copy of 42, not a reference to my_value
# so changing x inside the function has zero effect on my_value
print()


# === QUICK REFERENCE ===
# 1. Same name inside and outside a function = two different variables
# 2. You can READ globals without any keyword
# 3. You can't WRITE to globals without 'global' - you'll get UnboundLocalError
# 4. Local variables die when the function ends
# 5. Prefer parameters + return values over global variables
# 6. Changing a parameter inside a function doesn't change the original (for int, str, float, bool)