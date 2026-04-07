# Module 3: Data Types, Variables, & Expressions

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Data Types](#data-types)
  - [Variables](#variables)
  - [Operators](#operators)
  - [Order of Operations (PEMDAS)](#order-of-operations-pemdas)
  - [Input and Output](#input-and-output)
  - [F-String Formatting](#f-string-formatting)
  - [Type Conversion](#type-conversion)
  - [Comparison and Logical Operators](#comparison-and-logical-operators)
  - [Random Numbers](#random-numbers)
  - [Comments](#comments)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

This is where you actually start writing Python. Everything before this was theory and setup. This module covers the building blocks of any program: how to store data, what types of data exist, how to do math, how to get input from users, and how to display output. Everything you learn here gets used in every program you write going forward.

## Learning Objectives

- Understand Python data types (int, float, str, bool)
- Declare, assign, and manipulate variables following naming conventions
- Use arithmetic, comparison, logical, and assignment operators
- Combine variables, operators, and values into expressions
- Handle input/output with `input()` and `print()`, including formatting
- Write single-line and multi-line comments
- Write simple programs using the above concepts

## Key Concepts

### Data Types

Python has 4 primitive data types you need to know:

| Type | What It Stores | Examples |
|------|---------------|----------|
| `int` | Whole numbers | `10`, `-3`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `str` | Text (in quotes) | `"hello"`, `'123'` |
| `bool` | True or False | `True`, `False` |

You can check a variable's type with `type()`:

```python
x = 42
print(type(x))  # <class 'int'>
```

Python is dynamically typed, meaning you don't declare types and a variable can change types. This is flexible but can be tricky if you're not paying attention.

### Variables

Variables are named containers that hold values. You assign a value with `=` and Python figures out the type automatically.

```python
name = "Ada"
age = 25
height = 5.8
is_student = True
```

#### Naming Rules

| Rule | Example |
|------|---------|
| Can contain letters, numbers, underscores | `my_var123` |
| Cannot start with a number | `2variable` is invalid |
| Cannot contain spaces or hyphens | `variable-name` and `variable name` are invalid |
| Case-sensitive | `name` and `Name` are different variables |
| Cannot use Python reserved words | `if`, `else`, `for`, `while`, etc. |

#### Naming Conventions

| Convention | When to Use | Example |
|-----------|-------------|---------|
| `snake_case` | Variables and functions | `student_name`, `total_price` |
| `ALL_UPPERCASE` | Constants | `DISCOUNT_RATE`, `TAX_RATE` |

### Operators

#### Arithmetic Operators

| Operator | Name | What It Does | Example |
|----------|------|-------------|---------|
| `+` | Addition | Adds two values | `5 + 3 = 8` |
| `-` | Subtraction | Subtracts | `10 - 4 = 6` |
| `*` | Multiplication | Multiplies | `3 * 4 = 12` |
| `/` | Division | Always returns a float | `10 / 3 = 3.333` |
| `//` | Floor Division | Drops the decimal | `10 // 3 = 3` |
| `%` | Modulus | Returns the remainder | `7 % 3 = 1` |
| `**` | Exponentiation | Raises to a power | `2 ** 3 = 8` |

#### Compound Assignment Operators

Shorthand for updating a variable:

| Operator | What It Does | Same As |
|----------|-------------|---------|
| `+=` | Add and assign | `x = x + 5` |
| `-=` | Subtract and assign | `x = x - 3` |
| `*=` | Multiply and assign | `x = x * 2` |
| `/=` | Divide and assign | `x = x / 4` |

### Order of Operations (PEMDAS)

Python follows standard math order:

| Priority | Operators | Notes |
|----------|----------|-------|
| 1st | `()` | Parentheses first, always |
| 2nd | `**` | Exponents (evaluates right to left) |
| 3rd | `*`, `/`, `//`, `%` | Left to right |
| 4th | `+`, `-` | Left to right |

`5 + 3 * 2 = 11` not `16`, because multiplication happens before addition.

### Input and Output

#### `input()`

Reads user input. **Always returns a string.** You have to cast it before doing math.

```python
name = input("Enter your name: ")           # returns a string
age = int(input("Enter your age: "))         # cast to int
price = float(input("Enter price: "))        # cast to float
```

If you forget to cast and try to do math with it, you'll get a TypeError.

#### `print()`

Displays output. Has two useful parameters:

| Parameter | What It Does | Default | Example |
|-----------|-------------|---------|---------|
| `sep` | Changes separator between values | Space `" "` | `print("a", "b", sep="-")` outputs `a-b` |
| `end` | Changes what prints at the end | Newline `"\n"` | `print("hello", end=" ")` stays on same line |

```python
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry
print(2025, 1, 15, sep="-")                    # 2025-1-15
```

### F-String Formatting

F-strings let you embed variables and expressions inside strings. Put an `f` before the quotes and use `{}` for variables.

```python
name = "Ada"
age = 25
print(f"Name: {name}, Age: {age}")
```

Common format specifiers:

| Specifier | What It Does | Example | Output |
|-----------|-------------|---------|--------|
| `:.2f` | 2 decimal places | `f"{3.14159:.2f}"` | `3.14` |
| `:,d` | Commas in integers | `f"{7600:,d}"` | `7,600` |
| `:,.2f` | Commas + 2 decimals | `f"{7600.1:,.2f}"` | `7,600.10` |
| `:02d` | Leading zeros | `f"{4:02d}"` | `04` |
| `:b` | Binary | `f"{4:b}"` | `100` |
| `:x` | Hexadecimal | `f"{31:x}"` | `1f` |
| `:e` | Scientific notation | `f"{44:e}"` | `4.400000e+01` |

### Type Conversion

Converting between types with casting functions:

```python
num_str = "123"
num_int = int(num_str)       # string to int
num_float = float(num_str)   # string to float
age_str = str(25)            # int to string
```

Watch out for truthy/falsy values:

| Falsy (evaluates to `False`) | Truthy (evaluates to `True`) |
|-----------------------------|------------------------------|
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]` (empty list) | Any non-empty list |

Adding a string and an int doesn't work. `"5" + 10` gives a TypeError. You need to cast one of them first.

Also: `"5" + "10"` gives `"510"` (string concatenation), not `15`. Watch your types.

### Comparison and Logical Operators

#### Comparison Operators

| Operator | What It Does |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

#### Logical Operators

| Operator | What It Does |
|----------|-------------|
| `and` | Both conditions must be True |
| `or` | At least one must be True |
| `not` | Reverses the boolean value |

```python
is_passing = score >= 70
has_honors = gpa > 3.0 and credits >= 120
needs_help = not is_passing
```

### Random Numbers

The `random` module lets you generate random values:

```python
import random

random.randint(1, 10)       # random int between 1 and 10 (inclusive)
random.random()             # random float between 0.0 and 1.0
random.choice(['a', 'b'])   # picks a random item from a list
```

### Comments

Comments explain your code to humans. Python ignores them when running.

```python
# Single-line comment (use the hash symbol)

"""
Multi-line comment
or docstring. Can span
multiple lines.
"""
```

Best practice: explain **why** you're doing something, not just what. Keep them concise and update them when you change code.

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/variables).

| File | Description |
|------|-------------|
| [variables.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/variables.py) | Variables and constants |
| [datatypes.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/datatypes.py) | Built-in data types with printed examples |
| [operator.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/operator.py) | Arithmetic operators |
| [expressions.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/expressions.py) | Complex formulas and compound assignment operators |
| [comparison.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/comparison.py) | Comparison and logical operators |
| [comments.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/comments.py) | Documentation practices with a circle area calculation |
| [inputoutput.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/inputoutput.py) | User input and formatted output |
| [ex1calculator.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/ex1calculator.py) | Simple calculator combining input, arithmetic, and output |
| [moduleinfo.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/moduleinfo.py) | Code examples from the module intro video |
| [shoppingcart.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/variables/shoppingcart.py) | Capstone example: variables, operators, input, formatting in a receipt generator |

## My Example Code

These are additional examples covering topics not fully shown in the class repo.

| File | Description |
|------|-------------|
| [sep_and_end.py](examples/sep_and_end.py) | `sep` and `end` parameters in `print()` |
| [random_examples.py](examples/random_examples.py) | `random` module: `randint()`, `random()`, `choice()` |
| [floor_division_and_modulus.py](examples/floor_division_and_modulus.py) | `//` and `%` with practical examples (phone number, time conversion) |
| [fstring_formatting.py](examples/fstring_formatting.py) | F-string format specifiers: `:.2f`, `:,d`, `:02d`, `:b`, `:x`, `:e` |

## Resources

- [Course GitHub Repository: Variables](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/variables)
- [Python Style Guide (PEP 8)](https://peps.python.org/pep-0008/)
- [Think Python 2e (Downey)](https://greenteapress.com/wp/think-python-2e/)