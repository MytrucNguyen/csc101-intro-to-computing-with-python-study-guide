# Module 8: Functions (Part 1)

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [What Are Functions](#what-are-functions)
  - [Why Use Functions](#why-use-functions)
  - [Defining a Function](#defining-a-function)
  - [Calling a Function](#calling-a-function)
  - [Built-in Functions](#built-in-functions)
  - [The Math Module](#the-math-module)
  - [Parameters and Arguments](#parameters-and-arguments)
  - [Positional Arguments](#positional-arguments)
  - [Keyword Arguments](#keyword-arguments)
  - [Default Parameter Values](#default-parameter-values)
  - [Variable Scope](#variable-scope)
  - [Return Statements](#return-statements)
  - [Using Return Values in Expressions](#using-return-values-in-expressions)
  - [Returning Multiple Values](#returning-multiple-values)
  - [Returning Lists](#returning-lists)
  - [Returning Dictionaries](#returning-dictionaries)
  - [Function Docstrings](#function-docstrings)
  - [Function Best Practices](#function-best-practices)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

Functions let you take a chunk of code, give it a name, and reuse it whenever you want. Instead of copying and pasting the same calculation in five different places, you write it once as a function and call it five times. If something breaks, you fix it in one place instead of hunting through your entire program. This module covers how to define your own functions, pass data into them with parameters, get data back with return statements, and document them with docstrings. You've already been using functions like `print()`, `input()`, `len()`, and `int()` since Module 1 - now you learn how to build your own.

## Learning Objectives

- Understand basic function concepts and terminology
- Write user-defined functions using the `def` keyword
- Know the difference between parameters (in the definition) and arguments (in the call)
- Use positional arguments, keyword arguments, and default parameter values
- Use return statements to send values back from functions
- Return multiple values using tuples, lists, and dictionaries
- Write docstrings to document what your functions do
- Understand variable scope - local vs global variables
- Use Python's built-in functions and the math module

## Key Concepts

### What Are Functions

A function is a named block of code that performs a specific task. You define it once, then call it whenever you need it. Think of it like the "store and reuse" pattern - the `def` is the store, and calling the function is the reuse.

```python
def greet():
    print("Hello!")

greet()    # call the function - prints "Hello!"
greet()    # call it again - prints "Hello!" again
```

The `def` part doesn't run any code. It just remembers it. The code only runs when you call the function by name with parentheses.

### Why Use Functions

- **Reduce repetition** - write once, use many times
- **Organize code** - break complex programs into smaller, manageable pieces
- **Easier debugging** - if something breaks, you know exactly which function to look at
- **Improve readability** - descriptive function names make code self-documenting
- **Reusability** - the same function can be called from anywhere in your program

Without functions, calculating the area of two rectangles means writing the same code twice:

```python
# Without functions - repetitive
area1 = 5 * 3
area2 = 7 * 4
```

With a function, you write the logic once:

```python
# With functions - reusable
def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 3)
area2 = calculate_area(7, 4)
```

### Defining a Function

Use the `def` keyword, followed by the function name, parentheses, and a colon. The function body is indented.

```python
def function_name(parameters):
    """Docstring: describes what function does"""
    # Function body
    # Code to execute
    return result
```

The parts:
- `def` - keyword that starts the definition
- Function name - descriptive, lowercase with underscores (same rules as variable names)
- Parameters - inputs in parentheses (optional)
- Docstring - describes what the function does (optional but recommended)
- Function body - indented code block
- Return statement - sends a value back (optional)

```python
def welcome_message():
    """Prints a welcome message to the user"""
    print("Welcome to CSC101!")
    print("Let's learn about functions!")
```

### Calling a Function

Use the function name followed by parentheses. If you don't call the function, it just sits there doing nothing.

```python
def greet():
    print("Hello!")

# Nothing happens until you call it
greet()    # NOW it prints "Hello!"
```

When Python sees a function call, it jumps to the function definition, runs the code inside, and then comes back to where it left off. Like leaving a breadcrumb so it knows where to return to.

### Built-in Functions

Python comes with many functions you've already been using. These don't need an import statement:

| Function | What It Does | Example |
|----------|-------------|---------|
| `print()` | Display output | `print("Hello")` |
| `input()` | Get user input (returns string) | `input("Name: ")` |
| `len()` | Length of a sequence | `len([1,2,3])` → `3` |
| `int()` | Convert to integer | `int("42")` → `42` |
| `float()` | Convert to float | `float("3.14")` → `3.14` |
| `str()` | Convert to string | `str(42)` → `"42"` |
| `type()` | Check data type | `type(42)` → `<class 'int'>` |
| `range()` | Generate number sequence | `range(5)` → `0,1,2,3,4` |
| `sorted()` | Return sorted version | `sorted([5,2,8])` → `[2,5,8]` |
| `abs()` | Absolute value | `abs(-5)` → `5` |
| `round()` | Round a number | `round(3.7)` → `4` |
| `max()` | Largest value | `max(10, 25, 5)` → `25` |
| `min()` | Smallest value | `min(10, 25, 5)` → `5` |
| `sum()` | Sum of a sequence | `sum([1,2,3,4,5])` → `15` |

### The Math Module

The math module has additional functions that need to be imported first:

```python
import math

math.sqrt(25)          # 5.0 (square root)
math.pow(2, 3)         # 8.0 (power)
math.pi                # 3.141592653589793
math.e                 # 2.718281828459045
math.ceil(4.3)         # 5 (round up)
math.floor(4.8)        # 4 (round down)
math.sin(math.pi/2)    # 1.0
math.cos(0)            # 1.0
math.log(10)           # natural log
math.log10(100)        # 2.0
```

Don't forget `import math` at the top of your file.

### Parameters and Arguments

This is a terminology distinction that matters:

- **Parameter** - the variable in the function definition. It's a placeholder.
- **Argument** - the actual value you pass in when calling the function.

Think of parameters as empty boxes and arguments as what you put in those boxes.

```python
def greet_person(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Alice")          # "Alice" is an argument
```

Functions can have zero, one, or many parameters:

```python
# No parameters
def say_hello():
    print("Hello!")

# One parameter
def square(number):
    result = number * number
    print(result)

square(5)    # Output: 25
square(10)   # Output: 100

# Multiple parameters
def calculate_area(length, width):
    area = length * width
    print(f"Area: {area}")

calculate_area(5, 3)    # Output: Area: 15
calculate_area(7, 4)    # Output: Area: 28
```

The number of arguments must match the number of parameters. If a function takes two parameters and you pass one argument, you get a TypeError.

### Positional Arguments

Positional arguments are matched to parameters based on their order. The first argument goes to the first parameter, the second to the second, and so on.

```python
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

introduce("Alice", 25, "Phoenix")    # Correct order
# Output: Alice is 25 years old and lives in Phoenix

introduce(25, "Alice", "Phoenix")    # Wrong order!
# Output: 25 is Alice years old and lives in Phoenix (incorrect!)
```

Order matters:

```python
def divide(numerator, denominator):
    result = numerator / denominator
    print(result)

divide(10, 2)    # Output: 5.0
divide(2, 10)    # Output: 0.2 (different result!)
```

### Keyword Arguments

Keyword arguments use parameter names to assign values. This lets you pass arguments in any order and makes your code more readable.

```python
def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}")

# Using positional arguments (order matters)
describe_pet("dog", "Rex", 3)

# Using keyword arguments (order doesn't matter)
describe_pet(name="Rex", age=3, animal="dog")
describe_pet(age=3, animal="dog", name="Rex")    # Same result!
```

**Mixing positional and keyword:** positional arguments must come BEFORE keyword arguments.

```python
def book_trip(destination, duration, travelers):
    print(f"Booking {duration} days in {destination} for {travelers} people")

# Correct: Positional first, then keyword
book_trip("Paris", duration=5, travelers=2)

# Error: Keyword before positional
# book_trip(destination="Paris", 5, 2)    # SyntaxError!
```

### Default Parameter Values

Functions can provide default values for parameters, making them optional when calling.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Output: Hello, Alice! (uses default)
greet("Bob", "Hi")                # Output: Hi, Bob! (overrides default)
greet("Charlie", greeting="Hey")  # Output: Hey, Charlie!
```

Multiple defaults:

```python
def create_account(username, email, role="user", active=True):
    print(f"Account created:")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Role: {role}")
    print(f"  Active: {active}")

# Only required parameters
create_account("alice123", "alice@email.com")

# Some optional parameters
create_account("bob456", "bob@email.com", role="admin")

# All parameters specified
create_account("charlie", "charlie@email.com", "moderator", False)
```

**Parameter order rule:** required parameters (no defaults) come first, optional parameters (with defaults) come last.

```python
# Correct
def process_order(item, quantity, discount=0, express=False):
    pass

# Incorrect - required parameter after optional
# def process_order(discount=0, item, quantity):    # SyntaxError!
```

### Variable Scope

Scope determines where a variable can be accessed.

- **Local variables** - created inside a function, only exist inside that function
- **Global variables** - created outside functions, accessible anywhere
- **Parameters** - local to the function they belong to

```python
def calculate(x, y):
    result = x + y    # result is LOCAL
    return result

# result doesn't exist here!
answer = calculate(5, 3)
print(answer)    # 8
# print(result)  # NameError: result is not defined
```

Variables inside functions are local. They don't exist outside the function. This helps prevent naming conflicts - you can use `result` inside ten different functions and they won't interfere with each other.

### Return Statements

A return statement sends a value back from a function to the code that called it. Think of return as the function's answer to whoever called it.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)    # Output: 8
```

Without a return statement, functions return `None` by default:

```python
def print_greeting(name):
    print(f"Greetings, {name}!")

result = print_greeting("Alice")    # Prints: Greetings, Alice!
print(result)                        # Output: None
```

A return statement immediately exits the function. No code after it runs:

```python
def check_age(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible yet"

print(check_age(20))    # Output: Eligible to vote
print(check_age(15))    # Output: Not eligible yet
```

Functions can return any data type:

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = get_grade(85)
print(f"Your grade is: {grade}")    # Output: Your grade is: B
```

### Using Return Values in Expressions

Return values can be stored in variables, printed directly, or used in calculations:

```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

# Use return values in calculations
result = square(5) + cube(2)    # 25 + 8 = 33
print(result)

# Use in conditions
if square(4) > 10:
    print("Square of 4 is greater than 10")
```

**Nested function calls** - use the return value of one function as an argument to another:

```python
def double(x):
    return x * 2

result = square(double(3))    # square(6) = 36
print(result)
```

### Returning Multiple Values

Python can return multiple values as a tuple. You can unpack them into separate variables:

```python
def get_name():
    first = "Alice"
    last = "Smith"
    return first, last    # Returns a tuple

first_name, last_name = get_name()
print(f"First: {first_name}, Last: {last_name}")
```

```python
def calculate_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

data = [10, 25, 30, 15, 20]
min_val, max_val, avg_val = calculate_stats(data)
print(f"Min: {min_val}")
print(f"Max: {max_val}")
print(f"Average: {avg_val}")
```

This is something other programming languages can't do as easily. In Python, returning multiple values is built in.

### Returning Lists

Use a list when you want to return a collection that might be modified or when the number of items varies:

```python
def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

result = get_factors(12)
print(f"Factors of 12: {result}")
# Output: Factors of 12: [1, 2, 3, 4, 6, 12]
```

```python
def split_scores(scores):
    passing = []
    failing = []
    for score in scores:
        if score >= 60:
            passing.append(score)
        else:
            failing.append(score)
    return passing, failing

all_scores = [85, 45, 92, 58, 73, 67, 55]
pass_list, fail_list = split_scores(all_scores)
print(f"Passing: {pass_list}")
print(f"Failing: {fail_list}")
```

### Returning Dictionaries

Use a dictionary when you want to return labeled/named values:

```python
def analyze_text(text):
    stats = {
        'length': len(text),
        'words': len(text.split()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }
    return stats

sample = "Hello World! This is Python."
results = analyze_text(sample)
print(f"Length: {results['length']}")
print(f"Words: {results['words']}")
print(f"Uppercase: {results['uppercase']}")
print(f"Lowercase: {results['lowercase']}")
```

```python
def create_student(name, age, major, gpa):
    student = {
        'name': name,
        'age': age,
        'major': major,
        'gpa': gpa,
        'status': 'active'
    }
    return student

student1 = create_student("Alice", 20, "Computer Science", 3.8)
print(student1)
```

### Function Docstrings

A docstring is a string literal that describes what a function does. It's written as the first line inside a function using triple quotes. You can view them with the `help()` function.

**Simple docstring:**

```python
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")
```

**Multi-line docstring:**

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    The formula used is: F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32
```

**Comprehensive docstring with Args and Returns:**

```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: The calculated BMI value
    """
    return weight / (height ** 2)
```

**Viewing docstrings:**

```python
def square(x):
    """Return the square of x."""
    return x * x

help(square)
```

**Docstring best practices:**
- Always write docstrings for your functions
- Write complete sentences - start with a capital letter and end with a period
- Be concise but clear
- Use imperative mood: "Calculate area", not "Calculates area"
- Document parameters and return values including types
- Update docstrings when you modify the function

### Function Best Practices

- **Descriptive names** - `calculate_average()` not `calc()`
- **Do one thing** - each function should have one clear purpose
- **Keep it short** - ideally under 20 lines
- **Always use docstrings** - document what it does
- **Consistent parameters** - related functions should use similar parameter names
- **Return, don't print** - let the caller decide what to do with the result

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgetting `()` when calling a function | References the function object instead of calling it | Always use `greet()` not `greet` |
| Wrong number of arguments | TypeError | Match the number of arguments to parameters |
| Wrong argument order (positional) | Function runs with wrong values in wrong parameters | Check the order, or use keyword arguments |
| Forgetting `return` | Function returns `None` instead of the value | Add `return` when you need a value back |
| Not storing the return value | The returned value is lost | Use `result = my_function()` |
| Keyword argument before positional | SyntaxError | Positional arguments always come first |
| Required parameter after optional | SyntaxError | Put required parameters first, defaults last |
| Using a local variable outside its function | NameError | Variables inside functions don't exist outside |
| Printing instead of returning | Can't use the result in calculations | Use `return` and let the caller decide to print |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/functions1).

| File | Description |
|------|-------------|
| [functions.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions1/functions.py) | Basic function examples - no return, return value, modify parameter, sum a list, enumerate |
| [functionnotes.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions1/functionnotes.py) | Comprehensive notes - parameters, arguments, positional/keyword, defaults, return values, multiple returns, docstrings |
| [functionslidecode.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions1/functionslidecode.py) | All code examples from the lecture slides |
| [docstringnotes.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions1/docstringnotes.py) | Docstring examples - single-line, multi-line, comprehensive format with Args/Returns |

## My Example Code

| File | Description |
|------|-------------|
| [return_vs_print.py](examples/return_vs_print.py) | Why returning a value is different from printing it, and when each one matters |
| [how_functions_work.py](examples/how_functions_work.py) | How data flows through functions - defining vs calling, arguments going in, return values coming out, each call starting fresh |

## Resources

- [Course GitHub Repository: Functions](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/functions1)
- [Think Python 2e: Functions](https://greenteapress.com/wp/think-python-2e/)
- [Python for Everybody: Functions](https://www.py4e.com/book.php)