# Module 5: Conditional Statements

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Why Conditionals Matter](#why-conditionals-matter)
  - [Comparison Operators](#comparison-operators)
  - [Logical Operators](#logical-operators)
  - [The if Statement](#the-if-statement)
  - [The if-else Statement](#the-if-else-statement)
  - [The if-elif-else Statement](#the-if-elif-else-statement)
  - [Nested Conditionals](#nested-conditionals)
  - [Membership Operators](#membership-operators)
  - [Truthy and Falsy Values](#truthy-and-falsy-values)
  - [Try and Except](#try-and-except)
  - [Operator Precedence](#operator-precedence)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

This is where your programs start making decisions. Up until now, everything ran top to bottom in order. Conditionals let your code branch, choosing different paths based on conditions. This is one of three fundamental control structures in programming (sequence, selection, iteration) and it shows up in every real program you'll ever write.

## Learning Objectives

- Understand the purpose of if, elif, and else statements
- Write conditional logic to control program flow based on user input or data
- Use logical operators (and, or, not) to combine or modify conditions
- Build nested conditionals for complex decision-making
- Apply conditionals to practical problems like input validation
- Identify and fix common errors in conditional statements

## Key Concepts

### Why Conditionals Matter

Without conditionals, your programs just do the same thing every time. Conditionals make them responsive: validating user input, controlling game logic, making calculations based on data, building menus, and handling errors. Every interactive program uses them.

### Comparison Operators

These compare two values and return `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `5 < 7` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 6` | `False` |

Big one to remember: `=` is assignment, `==` is comparison. Mixing them up is one of the most common beginner mistakes.

Strings can be compared too. They're compared based on Unicode values (basically alphabetical order), and the comparison is case-sensitive:

```python
print("apple" < "banana")      # True (a comes before b)
print("apple" == "Apple")      # False (case-sensitive)
```

### Logical Operators

Use these to combine multiple conditions:

| Operator | What It Does | Example |
|----------|-------------|---------|
| `and` | True only if BOTH conditions are true | `5 > 3 and 4 < 6` returns `True` |
| `or` | True if AT LEAST ONE condition is true | `5 < 2 or 3 > 1` returns `True` |
| `not` | Reverses the boolean value | `not True` returns `False` |

#### Truth Tables

**and** requires both to be True:

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**or** requires at least one to be True:

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**not** flips the value:

| A | not A |
|---|-------|
| True | False |
| False | True |

Python uses short-circuit evaluation: with `and`, if the first condition is False, it doesn't even check the second. With `or`, if the first condition is True, it skips the second.

### The if Statement

The simplest conditional. If the condition is True, the indented code runs. If False, it's skipped.

```python
if condition:
    # this runs only if condition is True
```

The colon and the indentation (4 spaces) are required. The Python interpreter will error if the body is empty or not indented.

```python
x = int(input("Enter a number: "))
if x > 0:
    print("x is positive")
print("Done checking")           # this always runs regardless
```

If you enter a negative number, the `print("x is positive")` line is skipped entirely. The last line runs no matter what because it's not indented under the if.

### The if-else Statement

Adds a second path: if the condition is False, the else block runs instead. One or the other always executes, never both.

```python
if condition:
    # runs if True
else:
    # runs if False
```

There is NO condition after `else`. That's a common mistake. It's just `else:`.

```python
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

### The if-elif-else Statement

For checking multiple conditions in sequence. Python checks them top to bottom and runs the FIRST one that's True, then skips the rest. The else is a catch-all if nothing matched.

```python
score = float(input("Enter score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print("Grades are posted!")
```

Once a match is found, everything below it is ignored. If you enter 75, it checks `>= 90` (False), `>= 80` (False), `>= 70` (True), prints "Grade: C", and skips the rest.

The order of your conditions matters. If you check `>= 60` before `>= 90`, a score of 95 would match `>= 60` first and print the wrong grade.

### Nested Conditionals

An if statement inside another if statement. Useful when you need to check multiple conditions in a specific order.

```python
age = 19
has_license = True

if age >= 16:
    print("You're old enough to drive.")
    if has_license:
        print("And you have a license, go drive!")
    else:
        print("But you need a license first.")
else:
    print("You're too young to drive.")
```

The inner if/else only runs if the outer if is True. Indentation is what tells Python which else belongs to which if. Try to keep nesting to 2-3 levels max. If you're going deeper, there's probably a cleaner way to write it.

### Membership Operators

Use `in` and `not in` to check whether a value exists in a sequence (string, list, tuple, set, dict):

| Operator | What It Does |
|----------|-------------|
| `in` | Returns True if value is found |
| `not in` | Returns True if value is NOT found |

```python
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Found it!")

if "grape" not in fruits:
    print("Not in the list")
```

### Truthy and Falsy Values

Python evaluates certain values as True or False even when they're not booleans:

| Falsy (evaluates to False) | Truthy (evaluates to True) |
|---------------------------|---------------------------|
| `False` | `True` |
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]` (empty list) | Any non-empty list |
| `None` | Most other objects |

This means you can write things like:

```python
name = input("Enter your name: ")
if name:                           # True if name is not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")
```

### Try and Except

Not technically a conditional, but it handles errors in a similar way. Wrap dangerous code (like converting user input to a number) in a `try` block. If it crashes, the `except` block runs instead of the whole program blowing up.

```python
raw = input("Enter a number: ")
try:
    number = int(raw)
    print(f"You entered {number}")
except:
    print("That's not a valid number")
print("Program continues either way")
```

Without try/except, entering "hello" would crash the program with a traceback. With it, the except block catches the error and the program keeps going.

Keep your try blocks small. Only put the dangerous line in there, not everything. If multiple lines are in the try block and one crashes, the rest of that block is skipped.

### Operator Precedence

When an expression has multiple operators, Python evaluates them in this order (highest to lowest):

| Priority | Operators |
|----------|----------|
| 1st | `()` Parentheses |
| 2nd | `**` Exponentiation |
| 3rd | `*`, `/`, `//`, `%` |
| 4th | `+`, `-` |
| 5th | `<`, `<=`, `>`, `>=`, `==`, `!=` (comparison) |
| 6th | `not` |
| 7th | `and` |
| 8th | `or` |

When in doubt, use parentheses to make your intent clear:

```python
# unclear
if x > 5 and y > 10 or z < 2:

# clear
if (x > 5 and y > 10) or z < 2:
```

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Using `=` instead of `==` | SyntaxError | Use `==` for comparison |
| Forgetting the colon `:` | SyntaxError | Always end if/elif/else with `:` |
| Wrong indentation | Wrong code runs or IndentationError | Use 4 spaces consistently |
| Writing `else if` instead of `elif` | SyntaxError | Python uses `elif` |
| Putting a condition after `else` | SyntaxError | `else` has no condition, just `:` |
| Wrong elif order | Wrong branch executes | Check highest values first |
| Using multiple `if` instead of `elif` | Multiple branches can run | Use `elif` when only one should run |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/conditionals).

| File | Description |
|------|-------------|
| [ifstatement.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/ifstatement.py) | Basic if statements and comparison operators |
| [ifelse.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/ifelse.py) | if-else with number and temperature checks |
| [ifelif.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/ifelif.py) | if-elif-else weather decision system |
| [logicaloperators.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/logicaloperators.py) | and, or, not with login system and driving example |
| [conditionalslides.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/conditionalslides.py) | All examples from the slides: nesting, validation, debugging |
| [moduleintro.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/conditionals/moduleintro.py) | Code from the module intro video |

## My Example Code

| File | Description |
|------|-------------|
| [if_vs_elif.py](examples/if_vs_elif.py) | Why multiple `if` statements all run but `elif` stops after the first match |

## Resources

- [Course GitHub Repository: Conditionals](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/conditionals)
- [Think Python 2e: Conditionals](https://greenteapress.com/wp/think-python-2e/)
- [Python for Everybody: Conditional Execution](https://www.py4e.com/book.php)