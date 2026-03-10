# Module 7: Nested Loops & Exceptions

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Nested Loops](#nested-loops)
  - [How Nested Loops Work](#how-nested-loops-work)
  - [When to Use Nested Loops](#when-to-use-nested-loops)
  - [The range() Function Review](#the-range-function-review)
  - [Nested Loops with Data Structures](#nested-loops-with-data-structures)
  - [Pattern Printing](#pattern-printing)
  - [Block Scope and Variables in Nested Loops](#block-scope-and-variables-in-nested-loops)
  - [Break and Continue in Nested Contexts](#break-and-continue-in-nested-contexts)
  - [Predicting Loop Iterations](#predicting-loop-iterations)
  - [Debugging Nested Loops](#debugging-nested-loops)
  - [What Are Exceptions](#what-are-exceptions)
  - [Errors vs Exceptions](#errors-vs-exceptions)
  - [Common Built-in Exception Types](#common-built-in-exception-types)
  - [Handling Exceptions with try/except](#handling-exceptions-with-tryexcept)
  - [Catching Specific Exception Types](#catching-specific-exception-types)
  - [try with else and finally](#try-with-else-and-finally)
  - [Raising Exceptions](#raising-exceptions)
  - [Exception Handling in Nested Loops](#exception-handling-in-nested-loops)
  - [Best Practices](#best-practices)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

This module has two big topics. First, nested loops — putting a loop inside another loop. This is how you work with grids, tables, matrices, and any data that has rows and columns. The inner loop runs completely for every single iteration of the outer loop, which is where most of the confusion happens. Second, exceptions — runtime errors that crash your program unless you handle them. The try/except block lets you catch these errors and deal with them gracefully instead of showing the user a scary traceback message. Together, these two topics let you write programs that handle complex data and don't blow up when something goes wrong.

## Learning Objectives

- Understand nested loop fundamentals and when to use them for multi-dimensional problems
- Apply nested loop syntax with proper indentation using both for and while constructs
- Use nested loops to iterate through lists, 2D lists, strings, and other data structures
- Understand how variables behave at different levels of nested loops (block scope)
- Use `range()` with multiple parameters to control nested loop iterations
- Use break and continue correctly in nested contexts (they only affect the innermost loop)
- Identify and fix common nested loop bugs: infinite loops, wrong indentation, scope confusion, off-by-one errors
- Know the difference between syntax errors and exceptions (runtime errors)
- Handle exceptions using try, except, else, and finally blocks
- Raise exceptions manually using `raise` for input validation

## Key Concepts

### Nested Loops

A nested loop is a loop inside another loop. You already used loops in Module 6. Now you're putting one inside the other. Think of it like a clock — the minute hand (inner loop) goes all the way around 60 times for every 1 move of the hour hand (outer loop).

```python
for i in range(3):        # outer loop — runs 3 times
    for j in range(2):    # inner loop — runs 2 times PER outer iteration
        print(i, j)
```

Output:
```
0 0
0 1
1 0
1 1
2 0
2 1
```

Total prints: 3 × 2 = 6. The inner loop finishes all its iterations before the outer loop moves to the next one.

### How Nested Loops Work

This is the part that trips people up. Here's what actually happens step by step with a 3×3 grid:

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # new line after each row
```

1. `i` starts at 0. Inner loop runs with `j` = 0, 1, 2. Prints `(0,0) (0,1) (0,2)`. Then `print()` moves to next line.
2. `i` becomes 1. Inner loop **resets** `j` back to 0. Runs with `j` = 0, 1, 2. Prints `(1,0) (1,1) (1,2)`.
3. `i` becomes 2. Inner loop resets again. Runs with `j` = 0, 1, 2. Prints `(2,0) (2,1) (2,2)`.

The key insight: the inner loop variable resets to its starting value every time the outer loop moves forward. This is why nested loops work for grids — the outer loop handles rows, the inner loop handles columns.

You can also nest while loops, but it's more error-prone because you have to manage the reset yourself:

```python
i = 0
while i < 2:
    j = 0            # MUST reset j here, inside the outer loop
    while j < 3:
        print(f"i={i}, j={j}")
        j += 1       # MUST update j
    i += 1           # MUST update i
```

If you forget `j = 0` inside the outer loop, the inner loop only runs the first time. If you forget `j += 1`, you get an infinite loop.

### When to Use Nested Loops

- Working with multi-dimensional data (tables, grids, matrices)
- When data is structured hierarchically (lists within lists, strings within lists)
- Comparing each item in one collection with items in another collection
- Generating patterns or combinations
- Processing data that has multiple levels of structure

### The range() Function Review

Quick refresher since `range()` controls how your nested loops iterate:

```python
range(stop)              # range(3) → 0, 1, 2
range(start, stop)       # range(2, 5) → 2, 3, 4
range(start, stop, step) # range(0, 10, 2) → 0, 2, 4, 6, 8
```

Reverse counting: `range(5, 0, -1)` → 5, 4, 3, 2, 1

Remember: the end value is always **exclusive** (stops before it). Same rule as Module 6.

### Nested Loops with Data Structures

**2D List (Matrix) — iterating by element:**

A 2D list is a list where each element is itself a list. Think of it as rows and columns. The outer loop grabs each row, the inner loop grabs each value in that row.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

Output:
```
1 2 3
4 5 6
7 8 9
```

The `end=" "` keeps values on the same line. The `print()` after the inner loop moves to the next row. This pattern shows up in game boards, image processing, spreadsheet data, and matrix operations.

**2D List — using indices:**

Sometimes you need to know the position of each element, not just its value. Use `range()` and `len()` to get row and column indices:

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

Key points:
- `len(matrix)` gives the number of rows
- `len(matrix[i])` gives the number of columns in row `i` (each row can be different)
- `matrix[i][j]` accesses the element at row `i`, column `j`

**Processing strings in a list:**

```python
words = ["hello", "world", "python"]
for word in words:
    for letter in word:
        print(letter, end="-")
    print()
```

Output: `h-e-l-l-o-` then `w-o-r-l-d-` then `p-y-t-h-o-n-`

The outer loop grabs each string, the inner loop processes each character.

### Pattern Printing

Nested loops are commonly used to print ASCII art shapes. The outer loop controls rows, the inner loop controls what gets printed on each row.

**Right-angled triangle:**

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

Output:
```
*
**
***
****
*****
```

The inner loop uses `range(i)`, so row 1 prints 1 star, row 2 prints 2 stars, and so on. The outer loop starts at 1 (not 0) because `range(0)` would print nothing on the first row.

**Inverted triangle:**

Change the inner loop to `range(i, 5)` to flip it upside down:

```python
for i in range(5):
    for j in range(i, 5):
        print("*", end="")
    print()
```

**Right-aligned triangle (using spaces):**

You need two inner loops — one for spaces, one for stars. The total width stays constant:

```python
for i in range(5):
    for s in range(4 - i):        # spaces (decreasing)
        print(" ", end="")
    for j in range(i + 1):        # stars (increasing)
        print("*", end="")
    print()
```

Output:
```
    *
   **
  ***
 ****
*****
```

**Multiplication table:**

```python
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i * j}", end='\t')
    print()
```

**Find all pairs that sum to a value:**

```python
value = 10
for i in range(1, value + 1):
    for j in range(1, value + 1):
        if i + j == value:
            print(f"{i} + {j} = {value}")
```

### Block Scope and Variables in Nested Loops

In Python, loop variables don't disappear after the loop ends. They keep their last value. This is different from some other languages.

```python
for i in range(2):
    for j in range(3):
        product = i * j
        print(f"{i} * {j} = {product}")

# i, j, and product still exist here
print(f"After loops: i = {i}, j = {j}, product = {product}")
```

What to know about scope in nested loops:

- Variables created in the outer loop persist through all inner loop iterations
- Variables created in the inner loop are recreated with each inner loop iteration
- Loop variables (`i`, `j`, etc.) retain their **last value** after the loop completes

### Break and Continue in Nested Contexts

This is where it gets tricky. In nested loops, `break` and `continue` only affect the **innermost loop** they're inside. They don't touch the outer loop.

**break exits only the innermost loop:**

```python
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # exits inner loop only
        print(f"i={i}, j={j}")
    print("Outer loop continues")
```

When `j` hits 2, the inner loop stops, but the outer loop keeps going to the next value of `i`.

**continue skips to the next iteration of the innermost loop:**

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # skip j=1, but inner loop continues with j=2
        print(f"i={i}, j={j}")
```

**Breaking out of multiple loops — use a flag variable:**

Since `break` only exits one loop, you need a workaround to exit both. The most common approach is a boolean flag:

```python
found = False
for i in range(5):
    for j in range(5):
        if i * j == 12:
            found = True
            break       # exits inner loop
    if found:
        break           # exits outer loop
```

**Tracing break and continue together:**

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue    # skip when j == 1
        if i == 2 and j == 2:
            break       # stop inner loop early
        print(f"i={i}, j={j}")
```

Step-by-step trace:
- i=0: j=0 → print (0,0). j=1 → continue (skip). j=2 → print (0,2)
- i=1: j=0 → print (1,0). j=1 → continue (skip). j=2 → print (1,2)
- i=2: j=0 → print (2,0). j=1 → continue (skip). j=2 → break (exit inner loop, no print)

Output: `(0,0) (0,2) (1,0) (1,2) (2,0)`

### Predicting Loop Iterations

You can figure out how many times nested loops will run without executing them. This is useful for understanding performance.

If the inner loop is independent of the outer loop: multiply the counts. `range(3)` × `range(4)` = 12 iterations.

If the inner loop depends on the outer loop's variable, it forms a triangle:

```python
count = 0
for i in range(10):
    for j in range(i + 1):
        count += 1
# count = 1 + 2 + 3 + ... + 10 = 55
```

This is the same logic as the triangle pattern — row 1 has 1 iteration, row 2 has 2, and so on.

### Debugging Nested Loops

General tips:

- **Print loop variables** to track what's happening
- **Check indentation carefully** — one wrong indent changes which loop a line belongs to
- **Verify loop ranges match your data** — use `len(grid[i])` for columns, not `len(grid)`
- **Use descriptive variable names** — `row`/`col` or `i`/`j` are fine, but don't use the same name for both loops

### What Are Exceptions

Exceptions are events that occur during program execution that disrupt the normal flow. By now you've probably seen these — you try to divide by zero, convert "hello" to an integer, or access an index that doesn't exist, and Python throws an error with a traceback message. Those are exceptions.

When Python encounters an error it can't handle, it creates an exception object. If you don't catch it, it prints the traceback and your program crashes.

### Errors vs Exceptions

These are two different things:

- **Syntax errors** — mistakes in code structure that prevent execution entirely. Missing a colon, misspelling a keyword, wrong indentation. Python catches these BEFORE your program runs.
- **Exceptions** — errors that occur DURING program execution at runtime. Your code has valid syntax but something goes wrong when it runs. These can be caught and handled.

```python
# Syntax error — program won't even start
# if x > 5    ← missing colon

# Exception — program starts but crashes here
print(5 / 0)  # ZeroDivisionError at runtime
```

### Common Built-in Exception Types

| Exception | When It Happens | Example |
|-----------|----------------|---------|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Invalid value for the operation | `int("hello")` — can't convert "hello" to int |
| `TypeError` | Operation on incompatible types | `"hello" + 5` — can't add string and int |
| `IndexError` | Index out of range for a list | `my_list[10]` when list has 3 items |
| `KeyError` | Key not found in dictionary | `my_dict["phone"]` when key doesn't exist |
| `FileNotFoundError` | File doesn't exist | `open("nonexistent.txt")` |
| `NameError` | Variable not defined | `print(undefined_variable)` |

### Handling Exceptions with try/except

We briefly saw try/except in Module 5 for input validation. Now we go deeper. The `try`/`except` block catches exceptions so your program doesn't crash:

```python
try:
    # code that might cause an exception
    result = 10 / 0
except:
    # code that runs if an exception occurs
    print("An error occurred")
```

How the flow works:

1. Code in the `try` block executes
2. If an exception occurs, the rest of the `try` block is **skipped**
3. The `except` block catches the exception and runs
4. If no exception occurs, the `except` block is **skipped** entirely
5. Either way, the program continues after the try/except

Basic input validation:

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except:
    print("That's not a valid age!")
```

Without try/except, entering "hello" would crash with a traceback. With it, the except block catches the ValueError and the program keeps running.

### Catching Specific Exception Types

A bare `except:` catches everything, which isn't great. Different errors need different responses. Catch specific types so you can handle each one appropriately:

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 divided by {num} is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
```

- Enter `5` → works fine, prints the result
- Enter `0` → catches ZeroDivisionError
- Enter `t` → catches ValueError

You can also catch the exception object to get its error message:

```python
try:
    num = int("abc")
except ValueError as e:
    print(f"Error details: {e}")
# Output: Error details: invalid literal for int() with base 10: 'abc'
```

And you can handle multiple exception types in one handler:

```python
except (ValueError, TypeError):
    print("Invalid value or type")
```

### try with else and finally

Python gives you two more optional blocks for finer control:

**else** runs only if NO exception occurred in the try block:

```python
try:
    result = 100 / 25
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Success! Result is {result}")  # runs because no exception
```

**finally** ALWAYS runs, whether there was an exception or not. Used for cleanup like closing files:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
finally:
    print("This block always runs, no matter what.")
```

Key points about finally:
- Executes regardless of whether an exception occurs
- Used for cleanup operations like closing files and connections
- Runs even if `return`, `break`, or `continue` is used
- For each `try` block, there can be only one `finally` block

**Full flow:**

```python
try:
    result = risky_operation()
except SomeError:
    handle_error()        # runs ONLY if SomeError occurs
else:
    success_code()        # runs ONLY if NO exception
finally:
    cleanup_code()        # ALWAYS runs
```

Execution order:
1. `try` block executes
2. If exception → jump to matching `except`, skip `else`
3. If no exception → skip all `except` blocks, run `else`
4. `finally` runs no matter what

### Raising Exceptions

You can manually throw exceptions when you detect invalid conditions in your own code. This is useful for input validation inside functions:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    user_age = set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")
```

When to raise exceptions:
- Input validation fails
- Preconditions for a function aren't met
- A function cannot complete its intended purpose
- You detect an invalid state

**Re-raising** — catch an exception, log it, then pass it along:

```python
try:
    risky_function()
except ValueError as e:
    print(f"Logging error: {e}")
    raise  # re-raise the same exception
```

**Raising with `from`** — chain exceptions to show the original cause:

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero") from e
```

### Exception Handling in Nested Loops

You can combine try/except with nested loops to handle bad data without stopping the entire loop:

```python
data = [
    ["10", "20", "30"],
    ["40", "bad", "60"],
    ["70", "80", "90"]
]

for row_index, row in enumerate(data):
    for col_index, value in enumerate(row):
        try:
            number = int(value)
            print(f"[{row_index}][{col_index}] = {number}")
        except ValueError:
            print(f"[{row_index}][{col_index}] = Invalid data: '{value}'")
            continue
```

The loop keeps going even when it hits "bad" in row 1. Without try/except, the whole program would crash on that value.

### Best Practices

- **Be specific** — catch specific exception types, not all exceptions with a bare `except:`
- **Don't hide errors** — log or report them so you know what went wrong
- **Use finally for cleanup** — ensure resources like files are always closed
- **Fail gracefully** — provide helpful error messages to the user
- **Don't overuse exceptions** — use them for exceptional conditions, not as normal control flow

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Using the same variable name in both loops | Outer variable gets overwritten | Use unique names: `i`/`j`, `row`/`col` |
| Forgetting to reset the inner variable in nested while loops | Inner loop only runs once | Put the reset (`j = 0`) inside the outer loop |
| Forgetting to update the inner while loop variable | Infinite loop | Always include `j += 1` (or equivalent) in the inner loop |
| Wrong indentation in nested loops | Code belongs to wrong loop | Check that each level is indented correctly |
| Using `len(grid)` for columns instead of `len(grid[i])` | IndexError — off-by-one | Columns use `len(grid[i])`, rows use `len(grid)` |
| Using bare `except:` | Catches everything, hides real bugs | Catch specific types: `except ValueError:` |
| Putting too much code in the try block | Hard to tell what caused the exception | Keep try blocks small — only the risky line |
| Thinking `break` exits all loops | Only exits the innermost loop | Use a flag variable to break out of multiple loops |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/loops2).

| File | Description |
|------|-------------|
| [nestedloops.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops2/nestedloops.py) | Basic nested for loop — prints all (i, j) pairs |
| [control.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops2/control.py) | Control structures review — if/elif/else, while, for, break, continue |
| [exceptions.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops2/exceptions.py) | Exception handling with raise — safe_divide that catches ZeroDivisionError and re-raises as ValueError |

## My Example Code

| File | Description |
|------|-------------|
| [nested_loop_common_mistakes.py](examples/nested_loop_common_mistakes.py) | The mistakes everyone makes with nested loops — same variable name, forgetting to reset, break only exiting one loop |
| [exception_common_mistakes.py](examples/exception_common_mistakes.py) | The mistakes everyone makes with exceptions — bare except, too much in try, not knowing when to raise vs catch |

## Resources

- [Course GitHub Repository: Loops 2](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/loops2)
- [GeeksForGeeks: Python Nested Loops](https://www.geeksforgeeks.org/python/python-nested-loops/)
- [Real Python: Nested Loops](https://realpython.com/nested-loops-python/)
- [GeeksForGeeks: Break Out of Multiple Loops](https://www.geeksforgeeks.org/python/how-to-break-out-of-multiple-loops-in-python/)
- [Programiz: Break and Continue](https://www.programiz.com/python-programming/break-continue)