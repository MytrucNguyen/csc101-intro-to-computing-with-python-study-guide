# Module 9: Functions Part 2 - Advanced Functions & Modules

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Modules](#modules)
  - [Import Methods](#import-methods)
  - [Common Built-in Modules](#common-built-in-modules)
  - [Advanced Function Parameters Review](#advanced-function-parameters-review)
  - [Variable-Length Arguments: *args](#variable-length-arguments-args)
  - [Variable-Length Keyword Arguments: **kwargs](#variable-length-keyword-arguments-kwargs)
  - [Combining Parameter Types](#combining-parameter-types)
  - [Variable Scope](#variable-scope)
  - [The global Keyword](#the-global-keyword)
  - [The nonlocal Keyword](#the-nonlocal-keyword)
  - [Scope Best Practices](#scope-best-practices)
  - [Error Handling in Functions](#error-handling-in-functions)
  - [Lambda Functions](#lambda-functions)
  - [Lambda with Built-in Functions](#lambda-with-built-in-functions)
  - [Designing Robust Functions](#designing-robust-functions)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

This module builds on the function basics from Module 8. You'll learn how to import modules to extend what Python can do without writing everything from scratch, how to write more flexible functions using `*args` and `**kwargs`, how variable scope works (local, global, nonlocal), and how to write lambda functions for quick one-off operations. You'll also learn about error handling inside functions and how to design functions that are robust and maintainable. The big takeaway is that Python's ecosystem of modules and libraries is what makes it so popular - why manually implement a square root function when you can just use `math.sqrt()`?

## Learning Objectives

- Import and use Python's built-in modules (math, random, datetime) with different import methods
- Create functions with default parameter values, keyword arguments, and variable-length argument lists (`*args`, `**kwargs`)
- Understand and apply local, global, and nonlocal variable scope using the `global` and `nonlocal` keywords
- Write lambda functions and use them with `map()`, `filter()`, and `sorted()`
- Implement error handling within functions using try/except
- Follow function documentation standards with comprehensive docstrings
- Design robust and maintainable functions using single responsibility principle
- Develop complex programs combining modules, advanced parameters, scope management, and error handling

## Key Concepts

### Modules

Modules are Python files containing pre-written code (functions, classes, variables) that extend Python's capabilities. They let you reuse code and access specialized functionality without writing everything from scratch.

Types of modules:
- **Built-in modules** - come with Python (math, random, datetime, os)
- **Standard library modules** - part of the Python installation
- **Third-party modules** - installed separately with `pip` (numpy, pandas)
- **User-created modules** - your own Python files that you import

When you import a module, Python runs all the code in that file. That's how it creates all the functions and variables for you to use. Python looks for modules in this order: the current directory, the PYTHONPATH environment variable, the standard library directories, and the site-packages directory for third-party packages.

### Import Methods

**Method 1: Standard import** - must use module name as prefix:

```python
import math
result = math.sqrt(16)    # must use math. prefix
```

**Method 2: Import specific items** - no prefix needed, but only imports what you list:

```python
from math import sqrt, pi
result = sqrt(16)          # no prefix
print(pi)
```

**Method 3: Import with alias** - shorter name for convenience:

```python
import datetime as dt
today = dt.date.today()

import math as m
result = m.sqrt(16)
```

This is common with libraries like numpy (`import numpy as np`) and pandas (`import pandas as pd`).

**Method 4: Import everything** - not recommended:

```python
from math import *
result = sqrt(25)    # works, but you can't tell where sqrt came from
```

This is frowned upon because you can't tell what came from the imported module and what didn't. If you're debugging a problem with a function, you can't easily track down where it was defined.

**Best practices for imports:**
- Place all imports at the top of your file
- Use standard import or import with alias for clarity
- Avoid `import *` in production code
- Use aliases for commonly used modules with long names

### Common Built-in Modules

**The math module:**

```python
import math

math.sqrt(25)          # 5.0 (square root)
math.pow(2, 3)         # 8.0 (power)
math.pi                # 3.141592653589793
math.e                 # 2.718281828459045
math.ceil(4.3)         # 5 (round up)
math.floor(4.7)        # 4 (round down)
math.factorial(5)      # 120
math.gcd(48, 64)       # 16 (greatest common divisor)
math.log(10)           # natural log
math.log10(1000)       # 3.0
math.log2(1000)        # ~9.97
math.sin(math.pi/2)    # 1.0
math.cos(0)            # 1.0
```

**The random module:**

```python
import random

random.randint(1, 10)                          # random int between 1-10
random.random()                                # random float between 0-1
random.choice(['red', 'blue', 'green'])        # random item from list

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                           # shuffle list in place
```

**The datetime module:**

```python
import datetime

now = datetime.datetime.now()       # current date and time
today = datetime.date.today()       # current date
birthday = datetime.date(2000, 5, 15)  # specific date
```

You can browse the full list of built-in modules at the [Python Module Index](https://docs.python.org/3/py-modindex.html).

### Advanced Function Parameters Review

Quick refresher from Module 8 - default parameter values let you make arguments optional:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice! (uses default)
print(greet("Bob", "Hi"))          # Hi, Bob! (overrides default)
```

**Rule:** default parameters must come after non-default parameters.

```python
# Correct
def create_profile(name, age, city="Unknown"):
    pass

# INCORRECT - SyntaxError
# def create_profile(name="John", age, city="Unknown"):
#     pass
```

### Variable-Length Arguments: *args

`*args` lets a function accept any number of positional arguments. It collects them into a tuple.

The problem it solves: what if you don't know how many arguments someone will pass?

```python
# Fixed parameters - only works with exactly 3 numbers
def multiply_three(a, b, c):
    return a * b * c

multiply_three(2, 3, 4)      # works (24)
# multiply_three(2, 3, 4, 5)  # TypeError - too many arguments
# multiply_three(2, 3)         # TypeError - too few arguments
```

With `*args`, it works with any number:

```python
def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply_all(2, 3))           # 6
print(multiply_all(2, 3, 4, 5))     # 120
print(multiply_all(7))              # 7
```

Another example - calculating an average of any number of values:

```python
def calculate_average(*numbers):
    return sum(numbers) / len(numbers)

print(calculate_average(1, 2, 3))          # 2.0
print(calculate_average(10, 20, 30, 40))   # 25.0
```

`*args` acts like a tuple inside the function, so you can loop through it, check its length, index into it, etc.

### Variable-Length Keyword Arguments: **kwargs

`**kwargs` lets a function accept any number of keyword arguments. It collects them into a dictionary.

```python
def create_user(**user_info):
    print("User created with:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

create_user(name="Alice", age=25, city="Boston", occupation="Engineer")
```

Output:
```
User created with:
  name: Alice
  age: 25
  city: Boston
  occupation: Engineer
```

This is useful when you don't know ahead of time what data someone might want to pass in - like inserting records into a database where different records have different fields:

```python
def insert_data(**data):
    for key, value in data.items():
        print(f"  {key}: {value}")

# First record has 4 fields
insert_data(name="Alice", email="alice@email.com", city="Boston", age=25)

# Second record only has 2 fields
insert_data(name="Bob", age=27)
```

### Combining Parameter Types

When you use different parameter types in one function, order matters:

1. Regular positional parameters
2. `*args`
3. Keyword-only parameters (after `*args`)
4. `**kwargs`

```python
def complex_function(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function(1, 2, 3, default="changed", extra1="a", extra2="b")
# Required: 1
# Args: (2, 3)
# Default: changed
# Kwargs: {'extra1': 'a', 'extra2': 'b'}
```

### Variable Scope

Scope determines where a variable can be accessed. Python follows the **LEGB rule** - when it sees a variable name, it looks in this order:

1. **L - Local** - variables defined inside the current function. Created when function is called, destroyed when it ends.
2. **E - Enclosing** - variables in outer functions (for nested functions)
3. **G - Global** - variables defined at the module level (outside all functions). Exist for the entire program.
4. **B - Built-in** - Python's built-in functions and constants (`print`, `len`, `str`, `int`). Always available.

**Local scope:**

```python
def my_function():
    local_var = 10    # only exists inside this function
    print(local_var)

my_function()          # works: prints 10
# print(local_var)     # NameError: local_var not defined outside
```

**Global scope:**

```python
global_var = 20

def print_global():
    print(global_var)    # can READ global variables

print_global()    # works: prints 20
```

**Local and global with the same name:**

```python
rate = 0.05    # global

def display_rate():
    rate = 0.75    # this creates a NEW local variable, doesn't change the global
    print(f"Inside function: {rate}")    # 0.75

display_rate()
print(f"Outside function: {rate}")       # 0.05 (unchanged)
```

### The global Keyword

If you want to actually modify a global variable from inside a function, you need the `global` keyword:

```python
counter = 0

def increment():
    global counter    # tells Python: use the global counter, don't create a local one
    counter += 1

increment()
increment()
print(counter)    # 2
```

Without `global`:

```python
counter = 0

def increment():
    counter += 1    # Error! Python thinks you're reading a local variable before assigning it

increment()    # UnboundLocalError
```

### The nonlocal Keyword

`nonlocal` lets a nested function modify a variable from the enclosing (outer) function:

```python
def outer():
    count = 0

    def inner():
        nonlocal count    # refers to count in outer function
        count += 1
        return count

    print(inner())    # 1
    print(inner())    # 2
    return count

print(outer())    # 2
```

Without `nonlocal`, the inner function would create its own local `count` instead of modifying the outer function's `count`.

### Scope Best Practices

- **Minimize global variables** - they make code harder to understand and debug
- **Pass parameters explicitly** - better than relying on global state
- **Return values** - instead of modifying global variables
- **Use global/nonlocal sparingly** - usually indicates there's a cleaner design

```python
# POOR: uses global variable
total = 0
def add_to_total(value):
    global total
    total += value

# BETTER: uses parameters and return values
def add_values(current_total, value):
    return current_total + value

total = add_values(total, 5)
```

### Error Handling in Functions

Functions should handle unexpected inputs gracefully instead of crashing.

**Basic try/except in a function:**

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Error: Cannot divide by zero
```

**Multiple exception types:**

```python
def safe_convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return f"Error: '{value}' cannot be converted to integer"
    except TypeError:
        return f"Error: Invalid type for conversion"
```

**Raising exceptions for input validation:**

```python
def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

try:
    print(calculate_grade(95))     # A
    print(calculate_grade(150))    # ValueError
except ValueError as e:
    print(f"Invalid input: {e}")
```

### Lambda Functions

A lambda is a small, anonymous function you create on the fly with the `lambda` keyword. It can take any number of arguments but is limited to a single expression - no if statements, no loops, no multiple lines, no `return` keyword. The result is automatically returned.

```python
lambda arguments: expression
```

Regular function vs lambda:

```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square_lambda = lambda x: x ** 2

print(square(5))           # 25
print(square_lambda(5))    # 25
```

Lambdas with multiple parameters:

```python
add = lambda x, y: x + y
print(add(3, 5))    # 8

full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))    # John Doe
```

**When to use lambda:**
- Short, simple operations
- One-time use with `map()`, `filter()`, `sorted()`
- Callback functions

**Avoid lambda for:**
- Complex logic (use regular functions)
- Multiple statements (lambda only allows one expression)
- When you need to reuse the function multiple times (give it a proper name)

### Lambda with Built-in Functions

Lambdas work naturally with `map()`, `filter()`, and `sorted()` because these functions expect a function as their first argument.

**map() - apply a function to every item:**

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)    # [1, 4, 9, 16, 25]

names = ["alice", "bob", "charlie"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)    # ['ALICE', 'BOB', 'CHARLIE']
```

**filter() - keep only items that meet a condition:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # [2, 4, 6, 8, 10]

names = ["Ann", "Robert", "Joe", "Elizabeth"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names)    # ['Robert', 'Elizabeth']
```

**sorted() - custom sorting with a key function:**

```python
numbers = [-5, 2, -8, 1, 9, -3]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)    # [1, 2, -3, -5, -8, 9]

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_students)
# [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]
```

### Designing Robust Functions

**Single Responsibility Principle** - each function should do ONE thing well:

```python
# POOR: function does too much
def process_order(items, customer):
    total = sum(item['price'] for item in items)
    if customer['is_premium']:
        total *= 0.9
    send_email(customer['email'], f"Your order total: ${total}")
    database.update_order(customer['id'], total)
    return total

# BETTER: separate concerns
def calculate_total(items):
    return sum(item['price'] for item in items)

def apply_discount(total, is_premium):
    return total * 0.9 if is_premium else total
```

**Naming conventions:**
- Use descriptive names: `calculate_monthly_payment()` not `calc()`
- Use verbs for actions: `get_user()`, `send_email()`, `validate_input()`
- Be consistent: if you use `get_` prefix, use it everywhere
- Avoid abbreviations: `customer` not `cust`

**Other best practices:**
- Keep functions short (ideally under 20 lines)
- Validate inputs at the start of the function
- Return values instead of modifying global state
- Always use docstrings

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Required parameter after default | SyntaxError | Put defaults last: `def f(required, optional="default")` |
| Using `import *` | Can't tell where functions came from, naming conflicts | Use `import math` or `from math import sqrt` |
| Modifying a global variable without `global` keyword | UnboundLocalError | Add `global variable_name` inside the function |
| Using `*args` or `**kwargs` when you know the parameters | Less readable, no IDE help | Use named parameters when you know them |
| Writing complex logic in a lambda | Hard to read and debug | Use a regular `def` function instead |
| Forgetting `list()` around `map()` or `filter()` | Get a map/filter object instead of a list | Wrap in `list()`: `list(map(lambda x: x*2, nums))` |
| Function doing too many things | Hard to test, debug, and reuse | Split into smaller functions (single responsibility) |
| Over-using global variables | Code is hard to understand and debug | Pass data through parameters and return values |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/functions2).

| File | Description |
|------|-------------|
| [overview.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions2/overview.py) | Comprehensive overview - imports, default parameters, *args, **kwargs, scope, global/nonlocal, lambdas |
| [advancedfunctions.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions2/advancedfunctions.py) | Positional-only parameters, keyword arguments, *args with stats function |
| [mapfiltersorted.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions2/mapfiltersorted.py) | Lambda with map(), filter(), and sorted() examples |
| [random_number.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/functions2/random_number.py) | Number guessing game using functions, random module, and input validation |

## My Example Code

| File | Description |
|------|-------------|
| [scope_traps.py](examples/scope_traps.py) | The scope mistakes that bite you - local vs global, same-name confusion, and when you actually need the global keyword |

## Resources

- [Course GitHub Repository: Functions 2](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/functions2)
- [Python Default Parameter Value (W3Schools)](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp)
- [Default Arguments in Python (GeeksForGeeks)](https://www.geeksforgeeks.org/default-arguments-in-python/)
- [Python args and kwargs: Demystified (Real Python)](https://realpython.com/python-kwargs-and-args/)
- [How to Use *args and **kwargs in Python (DigitalOcean)](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
- [Import: Official Python Documentation](https://docs.python.org/3/reference/import.html)
- [Modules: Official Python Documentation](https://docs.python.org/3/tutorial/modules.html)