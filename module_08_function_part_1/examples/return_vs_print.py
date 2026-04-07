# return vs print - they look similar but do completely different things
# this is the #1 thing that confuses people about functions


# === TASK 1: calculate tax on a purchase ===
# two versions of the same function - one prints, one returns
print("=== Tax Calculator ===")

# version 1: prints the result (bad habit)
def calculate_tax_print(amount):
    tax = amount * 0.08
    print(f"Tax: ${tax:.2f}")

# version 2: returns the result (better)
def calculate_tax_return(amount):
    return amount * 0.08

# both seem to work at first glance
calculate_tax_print(100)         # prints "Tax: $8.00"
tax = calculate_tax_return(100)  # returns 8.0, stored in variable
print(f"Tax: ${tax:.2f}")        # prints "Tax: $8.00"
# same output so far, so what's the difference?
print()


# === TASK 2: now try to USE the result ===
# this is where print falls apart
print("=== Using the Result ===")

# with return - you can do math with it
subtotal = 100
tax = calculate_tax_return(subtotal)
total = subtotal + tax
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax:      ${tax:.2f}")
print(f"Total:    ${total:.2f}")
print()

# with print - you can't do anything with it
subtotal = 100
result = calculate_tax_print(subtotal)   # prints "Tax: $8.00"
print(f"result is: {result}")            # None!
# total = subtotal + result              # TypeError: can't add None + int
# the function printed the answer but didn't give it back to you
print()


# === TASK 3: chaining functions together ===
# return values let you feed one function's output into another
print("=== Chaining Functions ===")

def double(x):
    return x * 2

def square(x):
    return x * x

# you can nest these because they return values
result = square(double(3))    # double(3) = 6, square(6) = 36
print(f"square(double(3)) = {result}")

# you can use them in expressions
total = double(5) + square(3)    # 10 + 9 = 19
print(f"double(5) + square(3) = {total}")

# you can use them in conditions
if square(4) > 10:
    print("square(4) is greater than 10")
print()

# none of this works if the function prints instead of returns
def square_print(x):
    print(x * x)

# result = square_print(double(3))   # prints 36, but result is None
# total = square_print(5) + 10       # TypeError: None + int


# === TASK 4: a function that returns None by accident ===
# if you forget the return statement, the function returns None
print("=== Forgetting Return ===")

def add_wrong(a, b):
    result = a + b
    # forgot to return result!

def add_right(a, b):
    result = a + b
    return result

answer1 = add_wrong(5, 3)
answer2 = add_right(5, 3)
print(f"add_wrong(5, 3) = {answer1}")    # None
print(f"add_right(5, 3) = {answer2}")    # 8
print()


# === TASK 5: when printing IS the right choice ===
# not every function needs to return something
# if the function's job is to display output, printing is fine
print("=== When Print is Correct ===")

def display_receipt(items, tax_rate=0.08):
    """Display a formatted receipt - this function's PURPOSE is to print"""
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    print("-" * 25)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax:      ${tax:.2f}")
    print(f"Total:    ${total:.2f}")
    print("-" * 25)

display_receipt([9.99, 14.50, 3.25])
# this is fine because displaying a receipt IS the task
# you wouldn't need to do math with a receipt
print()


# === QUICK REFERENCE ===
# return - gives the value BACK to the caller so they can use it
# print  - displays the value on screen and it's gone
#
# rule of thumb:
# - if someone might want to DO something with the result → return
# - if the function's whole job is to display something → print
# - when in doubt, return (the caller can always print it themselves)