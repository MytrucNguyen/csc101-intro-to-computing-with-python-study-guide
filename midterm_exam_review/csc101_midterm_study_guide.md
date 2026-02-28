# CSC101 Midterm Exam Study Guide

Based on everything we covered together in Modules 1–6.

---

# Module 1: Course Introduction & Getting Started with Python

## Python Installation & Setup

- Download from python.org/downloads
- **Check "Add Python to PATH"** during installation (don't skip this)
- Verify: open terminal, type `python --version`

## Development Environments

| Tool | What It Is |
|------|-----------|
| **IDLE** | Comes free with Python. Simple, beginner-friendly. Run with **Run → Run Module (F5)** |
| **VS Code** | Professional editor. Install Python extension from Microsoft. Recommended for the course |
| **Google Colab** | Browser-based, no install needed. Great for labs and data science |
| **PyCharm** | Full Python IDE from JetBrains. Free Community Edition available |

## Running Python

- **Interactive mode** — type `python` in terminal, get `>>>` prompt, execute line by line
- **Script mode** — write code in a `.py` file, run with `python filename.py` or F5 in IDLE

## Basic Syntax & Structure

```python
import math                          # import a module
student_name = 'Mytruc'              # variable assignment
print("Pi is", math.pi)             # output with print()
name = input("Enter your name: ")   # get user input
```

- Python uses **indentation** (4 spaces) to define code blocks — no curly braces
- Files saved with `.py` extension
- `print()` displays output, `input()` reads user input

---

# Module 2: Introduction to Computers

## Computer Hardware Components

| Component | What It Does |
|-----------|-------------|
| **CPU** | The "brain" — executes instructions, ~3 billion times/sec |
| **RAM** | Temporary, fast, volatile (lost when powered off) |
| **Storage (HDD/SSD)** | Permanent, non-volatile, slower, larger capacity |
| **Input Devices** | Keyboard, mouse, microphone, camera |
| **Output Devices** | Monitor, printer, speakers |
| **Motherboard** | Connects all components together |

### The Fetch-Decode-Execute Cycle

The CPU processes instructions in a continuous loop:

1. **Fetch** — retrieve the next instruction from memory (RAM)
2. **Decode** — figure out what the instruction means
3. **Execute** — carry out the instruction (math, move data, etc.)

Then repeat. This cycle happens billions of times per second.

### CPU Speed (GHz)

**GHz (Gigahertz)** measures the CPU's clock speed — how many billions of cycles per second. A 3.0 GHz CPU performs approximately 3 billion fetch-decode-execute cycles per second. Higher GHz generally means faster processing.

## How Computers Store & Process Data

- Everything is **binary** (0s and 1s) at the hardware level
- Transistors act as tiny on/off switches (ON=1, OFF=0)
- All high-level code eventually gets converted to binary machine code

## Binary Number System & Data Representation

### Number Systems

| System | Base | Digits | Python Function |
|--------|------|--------|----------------|
| Decimal | 10 | 0–9 | — |
| Binary | 2 | 0, 1 | `bin()` |
| Octal | 8 | 0–7 | `oct()` |
| Hexadecimal | 16 | 0–9, A–F | `hex()` |

### Binary Conversion

Each position is a power of 2: `1010` = (1×8) + (0×4) + (1×2) + (0×1) = **10**

### Data Units

**Bit** (smallest, 0 or 1) → **Byte** (8 bits, 256 values) → **KB** (1,024 bytes) → **MB** → **GB** → **TB**

**How many values can N bits represent?** Use the formula **2ⁿ**:

| Bits | Values (2ⁿ) |
|------|------------|
| 1 bit | 2¹ = 2 |
| 4 bits | 2⁴ = 16 |
| 8 bits (1 byte) | 2⁸ = 256 |

### Character Encoding

| Encoding | Characters | Scope |
|----------|-----------|-------|
| **ASCII** | 128 | English only. `A`=65, `a`=97, `@`=64 |
| **Unicode (UTF-8)** | 140,000+ | All languages, emojis, symbols |

## Software (System vs. Application)

- **System software** — OS (Windows, macOS, Linux), drivers, utilities
- **Application software** — programs you use (browsers, games, Word)

## Programming Languages

- **High-level** (Python, Java) — human-readable, must be translated
- **Low-level** (Assembly, Machine Code) — closer to hardware
- **Compiled** (C, C++) — translated all at once before running
- **Interpreted** (Python) — translated and executed line by line

## Algorithm Basics

An **algorithm** is a step-by-step procedure for solving a problem. Three characteristics: **definite** (each step is clear), **finite** (it ends), **effective** (each step is doable).

**Decomposition** — breaking a large problem into smaller, manageable parts.

## Computer Architecture (SDLC)

Four core phases: **Planning → Design → Implementation → Testing**

1. **Planning** — define the problem, gather requirements
2. **Design** — create blueprint and architecture
3. **Implementation** — write the actual code
4. **Testing** — find bugs, verify correctness

---

# Module 3: Data Types, Variables & Expressions

## Primitive Data Types

| Type | What It Stores | Examples |
|------|---------------|----------|
| `int` | Whole numbers | `10`, `-3`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `str` | Text (in quotes) | `"hello"`, `'123'` |
| `bool` | True or False | `True`, `False` |

Check type with `type()`: `type(42)` → `<class 'int'>`

Python is **dynamically typed** — no type declarations needed, types can change.

## Variables

Variables are named containers. Assign with `=`.

**Naming rules:**
- Must start with a letter or underscore
- Can contain letters, numbers, underscores
- **Cannot** start with a number, use hyphens, or use spaces
- Case-sensitive (`name` ≠ `Name`)
- Use `snake_case` for variables, `ALL_CAPS` for constants

## Operators

### Arithmetic Operators

| Operator | What It Does | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 4` | `12` |
| `/` | Division (always float) | `10 / 3` | `3.333...` |
| `//` | Floor division (drops decimal) | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Compound Assignment Operators

`+=`, `-=`, `*=`, `/=`, `//=`, `%=`

`x += 5` is the same as `x = x + 5`

### Operator Precedence (PEMDAS)

1. `()` Parentheses — highest priority
2. `**` Exponentiation (right-to-left)
3. `*`, `/`, `//`, `%` — left-to-right
4. `+`, `-` — left-to-right

Example: `5 + 3 * 2` = `11` (not 16, multiplication first)

## Type Conversion (Casting)

| Function | Converts To | Example |
|----------|-----------|---------|
| `int()` | Integer | `int("42")` → `42`, `int(3.9)` → `3` |
| `float()` | Float | `float("3.14")` → `3.14`, `float(5)` → `5.0` |
| `str()` | String | `str(42)` → `"42"` |
| `bool()` | Boolean | `bool(0)` → `False`, `bool(1)` → `True` |

**Implicit conversion:** mixing int and float gives float: `5 + 2.0` → `7.0`

**Common error:** `"5" + 10` → TypeError. Must cast: `int("5") + 10` → `15`

**Watch out:** `"5" + "10"` → `"510"` (string concatenation, not addition)

## Input & Output

### `input()` — ALWAYS returns a string

```python
name = input("Enter your name: ")           # returns str
age = int(input("Enter your age: "))         # cast to int
price = float(input("Enter price: "))        # cast to float
```

### `print()` parameters

| Parameter | What It Does | Default | Example |
|-----------|-------------|---------|---------|
| `sep` | Separator between values | `" "` (space) | `print("a", "b", sep="-")` → `a-b` |
| `end` | What prints at the end | `"\n"` (newline) | `print("hi", end=" ")` → stays on same line |

### F-String Formatting

```python
name = "Alice"
price = 49.99
print(f"Name: {name}, Price: ${price:.2f}")
```

| Specifier | What It Does | Example | Output |
|-----------|-------------|---------|--------|
| `:.2f` | 2 decimal places | `f"{3.14159:.2f}"` | `3.14` |
| `:,d` | Commas in integers | `f"{7600:,d}"` | `7,600` |
| `:b` | Binary | `f"{10:b}"` | `1010` |
| `:x` | Hexadecimal | `f"{255:x}"` | `ff` |

## Constants & Comments

- Constants use `ALL_UPPERCASE`: `PI = 3.14159`
- Single-line comment: `# this is a comment`
- Multi-line comment: `"""this is a multi-line comment"""`

## Random Numbers

```python
from random import randint, random, choice
randint(1, 10)           # random int from 1 to 10 (inclusive)
random()                 # random float between 0.0 and 1.0
choice(["a", "b", "c"]) # random item from a list
```

---

# Module 4: Strings, Lists, Tuples, Sets & Dictionaries

## Strings

Ordered, **immutable** sequences of characters. Created with `' '`, `" "`, or `""" """`.

### Indexing & Slicing

```
 d   i   n   o   s   a   u   r
 0   1   2   3   4   5   6   7
-8  -7  -6  -5  -4  -3  -2  -1
```

```python
s = "dinosaur"
s[0]      # 'd'
s[-1]     # 'r'
s[1:4]    # 'ino' (start inclusive, stop exclusive)
s[:3]     # 'din' (from beginning)
s[5:]     # 'aur' (to end)
s[::-1]   # 'ruasonid' (reversed)
```

### String Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.split(delim)` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join(list)` | Join list into string | `" ".join(["Hello","World"])` → `"Hello World"` |
| `.replace(old, new)` | Replace all occurrences | `"fox".replace("fox","cat")` → `"cat"` |
| `.find(sub)` | Index of first occurrence (-1 if not found) | `"hello".find("ll")` → `2` |
| `.capitalize()` | First letter uppercase | `"hello".capitalize()` → `"Hello"` |
| `len(string)` | Length | `len("World!")` → `6` |

### String Concatenation & Repetition

```python
"hello" + " " + "world"  # "hello world"
"ha" * 3                  # "hahaha"
```

### Escape Characters

`\"` = double quote, `\'` = single quote, `\n` = newline, `\t` = tab

## Lists

Ordered, **mutable** collections in square brackets `[]`. Can hold mixed types and duplicates.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [5, 2, 9, 7]
mixed = [1, "two", 3.0, True]
```

### Accessing & Slicing

Same indexing as strings: `fruits[0]` → `"apple"`, `fruits[-1]` → `"cherry"`, `fruits[1:3]` → `["banana", "cherry"]`

### List Methods

| Method | What It Does |
|--------|-------------|
| `.append(item)` | Add to end |
| `.insert(index, item)` | Insert at position |
| `.remove(item)` | Remove first occurrence |
| `.pop(index)` | Remove and return item (default: last) |
| `.extend(list)` | Add all items from another list |
| `.sort()` | Sort in place |
| `.reverse()` | Reverse in place |
| `.count(item)` | Count occurrences |
| `.index(item)` | Index of first occurrence |
| `len(list)` | Number of elements |

### List Math Functions

`sum(list)`, `max(list)`, `min(list)` — work on lists of numbers

### List Operations

```python
[1,2] + [3,4]     # [1, 2, 3, 4] (concatenation)
[1,2] * 3          # [1, 2, 1, 2, 1, 2] (repetition)
```

### Copying vs. Referencing

```python
original = [1, 2, 3]
reference = original       # SAME list — changes affect both
copy = original[:]         # NEW list — independent copy
copy2 = original.copy()   # also a new copy
```

## Tuples

Ordered, **immutable** collections in parentheses `()`. Once created, can't add/remove/change.

```python
point = (10, 20)
x, y = point              # tuple unpacking
```

Only two methods: `.count()` and `.index()`. Can be used as dictionary keys (lists cannot).

## Sets

**Unordered** collections of **unique** elements in curly braces `{}`. No duplicates, no indexing.

```python
my_set = {1, 2, 3, 3}     # {1, 2, 3} — duplicates removed
empty_set = set()          # NOT {} — that creates a dict
```

**Methods:** `.add()`, `.remove()`, `.discard()`, `.pop()`

**Set math:** union `|`, intersection `&`, difference `-`, symmetric difference `^`

## Dictionaries

**Key-value pairs** in curly braces. Keys must be immutable. Fast lookups.

```python
student = {"name": "Alice", "age": 25, "grade": "A"}
student["name"]            # "Alice"
student.get("gpa", 0.0)   # 0.0 (default if key missing)
student["gpa"] = 3.8       # add new key-value pair
```

**Methods:** `.keys()`, `.values()`, `.items()`, `.get(key, default)`, `.pop(key)`, `.update(dict)`

## Structure Comparison

| Structure | Ordered? | Mutable? | Duplicates? | Syntax |
|-----------|---------|----------|------------|--------|
| String | Yes | No | Yes | `" "` |
| List | Yes | Yes | Yes | `[ ]` |
| Tuple | Yes | No | Yes | `( )` |
| Set | No | Yes | No | `{ }` / `set()` |
| Dict | Yes* | Yes | Keys: No | `{ k: v }` |

---

# Module 5: Conditionals

## Boolean Expressions & Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `5 < 7` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 6` | `False` |

**Watch out:** `==` is comparison, `=` is assignment. Using `=` in an `if` is a SyntaxError.

## Logical Operators

| Operator | What It Does | Example |
|----------|-------------|---------|
| `and` | Both must be True | `5 > 3 and 2 < 10` → `True` |
| `or` | At least one must be True | `5 > 3 or 2 > 10` → `True` |
| `not` | Reverses the value | `not True` → `False` |

**Short-circuit evaluation:** `and` stops at first `False`, `or` stops at first `True`.

## if Statements

```python
# Simple if
if score >= 60:
    print("Passing")

# if/else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if/elif/else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

**Key rule:** `elif` stops at the **first True condition** — only one block runs. Multiple separate `if` statements are **independent** — all conditions are checked.

## Nested Conditionals

```python
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need a license")
else:
    print("Too young")
```

Can often flatten with `and`: `if age >= 18 and has_license:`

## Truth Values (Truthy/Falsy)

| Falsy (evaluates to `False`) | Truthy (evaluates to `True`) |
|-----------------------------|------------------------------|
| `False`, `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]`, `()`, `{}`, `set()` | Any non-empty collection |
| `None` | Everything else |

## Conditional Expressions (Ternary)

```python
status = "adult" if age >= 18 else "minor"
```

## Common Patterns

```python
# Input validation
age = int(input("Age: "))
if age < 0 or age > 150:
    print("Invalid age")

# Range checking
if 60 <= score <= 80:    # Python supports chained comparisons
    print("In range")

# None check
if value is None:        # use 'is', not '=='
    print("No value")
```

---

# Module 6: Loops (Part 1)

## for Loops

Iterate over a sequence (string, list, tuple, range).

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "hello":
    print(char)
```

## The `range()` Function

| Syntax | What It Generates | Example |
|--------|------------------|---------|
| `range(stop)` | 0 to stop-1 | `range(5)` → `0,1,2,3,4` |
| `range(start, stop)` | start to stop-1 | `range(2, 6)` → `2,3,4,5` |
| `range(start, stop, step)` | start to stop-1 by step | `range(0, 10, 2)` → `0,2,4,6,8` |

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(3, 10):      # start at 3
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)
```

## while Loops

Repeats as long as condition is True.

```python
count = 0
while count < 5:
    print(count)
    count += 1     # DON'T forget to update — or infinite loop!
```

## Infinite Loops & How to Avoid Them

An infinite loop never stops because the condition never becomes False.

```python
# INFINITE LOOP — forgot to increment
count = 0
while count < 5:
    print(count)
    # missing: count += 1
```

**Always** make sure your while loop's condition will eventually become False.

## Loop Control Statements

| Statement | What It Does |
|-----------|-------------|
| `break` | Exit the loop immediately |
| `continue` | Skip rest of current iteration, go to next |
| `pass` | Do nothing (placeholder) |

```python
# break — exit early
for i in range(10):
    if i == 5:
        break
    print(i)       # prints 0, 1, 2, 3, 4

# continue — skip one iteration
for i in range(5):
    if i == 2:
        continue
    print(i)       # prints 0, 1, 3, 4 (skips 2)
```

## for vs while

| for loop | while loop |
|----------|-----------|
| Use when you know how many iterations | Use when you don't know how many |
| Iterates over a sequence or range | Repeats while condition is True |
| Python manages the loop variable | You manage the loop variable yourself |

```python
# Same output — for is cleaner for this task
for i in range(5):       # Python handles i
    print(i)

i = 0
while i < 5:             # You handle i
    print(i)
    i += 1
```

## Iterating Over Collections

```python
# List
for item in ["a", "b", "c"]:
    print(item)

# String
for char in "hello":
    print(char)

# Range for index-based access
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
```

## Accumulator Pattern

```python
total = 0
for i in range(1, 6):
    total += i
print(total)    # 15 (1+2+3+4+5)
```

## Nested Loops

```python
for i in range(2):
    for j in range(3):
        print(i, j)
# Output: 0 0, 0 1, 0 2, 1 0, 1 1, 1 2
# Total iterations: 2 × 3 = 6
```

---

# Quick Reference — Must-Know Facts

1. `input()` **always** returns a string — cast with `int()` or `float()` for math
2. `//` drops the decimal (floor division), `%` gives the remainder
3. `==` is comparison, `=` is assignment — don't mix them up
4. Strings are **immutable** — methods return new strings
5. Lists are **mutable** — methods modify in place
6. `{}` creates an empty **dict**, not a set — use `set()` for empty set
7. `elif` stops at first True — only one block runs
8. Multiple `if` statements are independent — all are checked
9. `and` needs **both** True, `or` needs **at least one** True
10. `break` exits the loop, `continue` skips to next iteration
11. `while` loops need their condition to eventually become False
12. `range(stop)` starts at 0 and **excludes** the stop value
13. F-strings: `f"{value:.2f}"` for 2 decimal places
14. `for` loops are best when you know the iteration count
15. `while` loops are best when you don't know when to stop