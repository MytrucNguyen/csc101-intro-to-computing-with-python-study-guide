# Module 6: Loops Part 1 - While and For Loops

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Why Loops Matter](#why-loops-matter)
  - [While Loops](#while-loops)
  - [The Standard While Loop Formula](#the-standard-while-loop-formula)
  - [Common While Loop Patterns](#common-while-loop-patterns)
  - [For Loops](#for-loops)
  - [The range() Function](#the-range-function)
  - [Iterating Through Data](#iterating-through-data)
  - [Loop Control: break and continue](#loop-control-break-and-continue)
  - [Common Loop Patterns](#common-loop-patterns)
  - [When to Use for vs while](#when-to-use-for-vs-while)
  - [Nested Loops](#nested-loops)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

Loops let your code repeat without rewriting the same lines over and over. Need to print something 100 times? Process every item in a list? Keep asking for input until the user gets it right? Loops handle all of that. Python has two types: `while` loops (repeat while a condition is true) and `for` loops (repeat for each item in a sequence). This is the third fundamental control structure after sequence and selection (conditionals from Module 5).

## Learning Objectives

- Understand when and why to use loops for repetitive tasks
- Write while loops for condition-based repetition
- Write for loops to iterate over sequences (strings, lists, ranges)
- Use break and continue to control loop flow
- Choose the right loop type for different situations
- Solve problems using loop structures

## Key Concepts

### Why Loops Matter

Without loops, printing "hello" 5 times means writing 5 print statements. With a loop, it's 2 lines:

```python
for i in range(5):
    print("hello")
```

Loops are used for input validation, processing collections of data, counting, simulations, building menus, login systems, and basically any task that involves repetition.

### While Loops

A while loop keeps running as long as its condition is True. It checks the condition BEFORE each iteration, so if the condition starts as False, the loop body never runs (zero-trip loop).

```python
while condition:
    # loop body (indented)
    # must include something that eventually makes condition False
```

Simple countdown example:

```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blastoff!")
```

This prints 5, 4, 3, 2, 1, then "Blastoff!". When `n` becomes 0, the condition `n > 0` is False and the loop exits.

### The Standard While Loop Formula

Most while loops follow this three-step pattern:

```python
tracker = value              # 1) initialize the tracker variable
while logical_expression:    # 2) check: are we done?
    # code to repeat
    tracker = new_value      # 3) update the tracker
```

All three steps are essential:

1. **Initialize**: set the tracker variable BEFORE the loop starts
2. **Check**: the condition that determines whether to keep looping
3. **Update**: change the tracker inside the loop so the condition eventually becomes False

If you forget step 3, you get an **infinite loop**. The loop runs forever because the condition never changes:

```python
count = 0
while count < 5:
    print(count)
    # forgot count += 1, so count is always 0
```

### Common While Loop Patterns

**Counting pattern**: count up or down by any increment:

```python
# Count from 1 to 5
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Count down from 12 by 2s
counter = 12
while counter >= 0:
    print(counter)
    counter -= 2
```

**Accumulator pattern**: keep a running total while looping:

```python
total = 0
counter = 1
while counter <= 5:
    total += counter
    counter += 1
print(f"Sum of 1 to 5: {total}")    # 15
```

**Input validation**: keep asking until the user gives valid input:

```python
response = ""
while response != "yes" and response != "no":
    response = input("Please enter 'yes' or 'no': ")
print(f"You chose: {response}")
```

**Sentinel-controlled loop**: repeat until a special "stop" value is entered. The sentinel is a value that wouldn't normally be valid input (like -1 for positive numbers):

```python
number = int(input("Enter a number (-1 to stop): "))
total = 0
while number != -1:
    total += number
    number = int(input("Enter a number (-1 to stop): "))
print(f"Total: {total}")
```

**Infinite loop with break**: use `while True` and break out when done. This is common for menus and command loops:

```python
while True:
    user_input = input("Enter command: ")
    if user_input == "exit":
        break
    print(f"Processing: {user_input}")
```

### For Loops

A for loop iterates over each item in a sequence. You don't need to manage an iteration variable yourself. Python handles it.

```python
for variable in sequence:
    # loop body
```

The loop variable takes on each value in the sequence, one at a time. When there are no more items, the loop ends.

```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Done!")
```

This prints 5, 4, 3, 2, 1, then "Done!". The variable `i` is automatically set to each value in the list.

### The range() Function

`range()` generates a sequence of numbers for use with for loops. It takes up to 3 arguments:

| Function | Description | Output |
|----------|-------------|--------|
| `range(5)` | Start at 0, end before 5 | 0, 1, 2, 3, 4 |
| `range(2, 6)` | Start at 2, end before 6 | 2, 3, 4, 5 |
| `range(1, 10, 2)` | Start at 1, end before 10, step by 2 | 1, 3, 5, 7, 9 |
| `range(10, 0, -1)` | Start at 10, end before 0, step by -1 | 10, 9, 8, ..., 1 |
| `range(0, 10, 2)` | Start at 0, end before 10, step by 2 | 0, 2, 4, 6, 8 |
| `range(3, -2, -1)` | Start at 3, end before -2, step by -1 | 3, 2, 1, 0, -1 |

The end value is always **exclusive** (stops before it). Same off-by-one concept as slicing from Module 4.

`range()` returns an iterable, not a list. It's memory efficient because it generates numbers on demand rather than storing them all at once.

### Iterating Through Data

For loops work with any sequence, not just `range()`:

**Lists**:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Strings** (character by character):
```python
for char in "Python":
    print(char)
```

**Tuples**:
```python
for coord in (1, 2, 3):
    print(coord)
```

**Dictionaries** (loops over keys by default):
```python
grades = {"Ada": 85, "Grace": 92, "Margaret": 78}
for name in grades:
    print(f"{name}: {grades[name]}")
```

Tip: use singular/plural naming like `fruit`/`fruits` or `name`/`names` to make your code readable. Python doesn't care about the names, but it helps you read it.

### Loop Control: break and continue

**break** exits the loop immediately. The program jumps to the first line AFTER the loop:

```python
for num in range(10):
    if num == 5:
        break
    print(num)        # prints 0, 1, 2, 3, 4
print("Done")         # runs after break exits the loop
```

**continue** skips the rest of the current iteration and goes back to the top of the loop:

```python
for num in range(10):
    if num % 2 != 0:
        continue       # skip odd numbers
    print(num)         # prints 0, 2, 4, 6, 8
```

Use both sparingly. A well-structured loop condition is usually better than relying on break/continue. But sometimes they make code cleaner, especially for search operations or filtering.

### Common Loop Patterns

**Accumulator** (sum values):
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")    # 15
```

**Counter** (count specific items):
```python
text = "Hello World"
count = 0
for char in text:
    if char == "l":
        count += 1
print(f"Found {count} letter l's")    # 3
```

**Search** (find an item):
```python
names = ["Ada", "Grace", "Margaret"]
target = "Grace"
found = False
for name in names:
    if name == target:
        found = True
        break
if found:
    print(f"{target} found!")
```

**Finding the largest value**:
```python
numbers = [9, 41, 12, 3, 74, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest: {largest}")    # 74
```

### When to Use for vs while

| Use `for` when... | Use `while` when... |
|-------------------|-------------------|
| You know how many iterations | You don't know how many iterations |
| Iterating over a sequence (list, string, range) | The loop depends on a condition changing |
| Counting a specific number of times | Waiting for user input |
| Processing each item in a collection | Input validation |
| The number of iterations is computable | Implementing menus or command loops |

General rule: if you can count it or iterate over it, use `for`. If you're waiting for something to happen, use `while`.

### Nested Loops

A loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j}\t", end="")
    print()    # new line after each row
```

This creates a 5x5 multiplication table. The outer loop controls rows, the inner loop controls columns. For each row (each value of `i`), the inner loop runs 5 times. Keep nesting to 2-3 levels max.

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgetting to update the loop variable | Infinite loop | Always modify the tracker variable inside the loop |
| Off-by-one errors with `range()` | Loop runs one too many or too few times | Remember `range()` stops BEFORE the end value |
| Modifying a for loop variable inside the loop | Unexpected behavior | Let the for loop manage its own variable |
| Wrong indentation | Code runs outside/inside loop when it shouldn't | Check which lines are indented under the loop |
| Using `for` when you need `while` | Can't handle unknown iteration count | Use `while` for condition-based loops |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/loops1).

| File | Description |
|------|-------------|
| [whileloops.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops1/whileloops.py) | Basic while loop with quit command |
| [forloops.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops1/forloops.py) | For loops with range, strings, lists, tuples, dictionaries |
| [looppatterns.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/loops1/looppatterns.py) | Counting, input validation, sentinel loops, infinite loop with break |

## My Example Code

| File | Description |
|------|-------------|
| [while_vs_for.py](examples/while_vs_for.py) | Same tasks done with both loops to show when each one is the better choice |

## Resources

- [Course GitHub Repository: Loops](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/loops1)
- [Think Python 2e: Iteration](https://greenteapress.com/wp/think-python-2e/)
- [Python for Everybody: Loops and Iteration](https://www.py4e.com/book.php)
- [Introduction to Computational Thinking in Python: While Loops](https://muzny.github.io/csci1200-notes/06/1/while_loops_basics)