# how data flows through functions - the stuff that clicks once you see it
# if this is your first time writing functions, this is for you


# === STEP 1: defining a function does NOT run it ===
# this is the first thing that confuses people
print("=== Define vs Call ===")

def say_hello():
    print("Hello from inside the function!")

# nothing happened yet - Python just memorized the function
# the code inside only runs when you CALL it
print("Before the call")
say_hello()    # NOW it runs
print("After the call")
# output: "Before the call", "Hello from inside the function!", "After the call"
print()


# === STEP 2: arguments go IN, return values come OUT ===
# think of a function like a machine at a factory
# you feed something in (arguments) and it spits something out (return value)
print("=== Data Goes In, Data Comes Out ===")

def double(number):       # number goes IN (parameter)
    return number * 2     # result comes OUT (return value)

result = double(5)        # 5 goes in, 10 comes out
print(f"double(5) = {result}")

# the value 5 gets copied into the parameter 'number'
# the function does its thing and sends back 10
# you catch the 10 with 'result ='
print()


# === STEP 3: the argument and the parameter are separate ===
# people think they're the same variable - they're not
print("=== Arguments and Parameters Are Copies ===")

def add_ten(x):
    x = x + 10    # this changes x INSIDE the function
    return x

my_number = 5
new_number = add_ten(my_number)
print(f"my_number is still: {my_number}")    # still 5!
print(f"new_number is: {new_number}")         # 15

# my_number didn't change because the function got a COPY of 5
# it's like photocopying a document - writing on the copy
# doesn't change the original
print()


# === STEP 4: each call is independent ===
# the function starts fresh every time you call it
print("=== Each Call Starts Fresh ===")

def count_letters(word):
    count = 0
    for char in word:
        count += 1
    return count

# each call creates its own 'count' that starts at 0
print(f"'hello' has {count_letters('hello')} letters")
print(f"'hi' has {count_letters('hi')} letters")
print(f"'python' has {count_letters('python')} letters")
# they don't interfere with each other
print()


# === STEP 5: order matters with multiple parameters ===
# the first argument goes to the first parameter, second to second, etc.
print("=== Argument Order Matters ===")

def describe(name, age):
    print(f"{name} is {age} years old")

# correct order
describe("Alice", 25)    # Alice is 25 years old

# wrong order - Python doesn't know you mixed it up
describe(25, "Alice")    # 25 is Alice years old (nonsense)

# keyword arguments fix this - you can use any order
describe(age=25, name="Alice")    # Alice is 25 years old
print()


# === STEP 6: putting it all together ===
# a realistic example that uses everything above
print("=== Putting It Together: Pizza Order ===")

def calculate_pizza_cost(size, toppings):
    """Calculate the cost of a pizza based on size and number of toppings."""
    if size == "small":
        base_price = 8.00
    elif size == "medium":
        base_price = 10.00
    elif size == "large":
        base_price = 12.00
    else:
        base_price = 10.00    # default to medium

    topping_cost = toppings * 1.50
    return base_price + topping_cost

# the function doesn't know or care where these values come from
# you could hardcode them, get them from input, read from a file, etc.
cost1 = calculate_pizza_cost("large", 3)
cost2 = calculate_pizza_cost("small", 1)

print(f"Large pizza, 3 toppings: ${cost1:.2f}")
print(f"Small pizza, 1 topping:  ${cost2:.2f}")
print(f"Total:                   ${cost1 + cost2:.2f}")
# you can do math with the return values because they're just numbers
print()


# === QUICK REFERENCE ===
# 1. def memorizes the function - it doesn't run until you call it
# 2. arguments go in through the parentheses, return sends a value back out
# 3. the function gets a COPY of the argument - it can't change your original variable
# 4. each function call starts completely fresh
# 5. argument order matches parameter order (or use keyword arguments)
# 6. store the return value in a variable if you want to use it later