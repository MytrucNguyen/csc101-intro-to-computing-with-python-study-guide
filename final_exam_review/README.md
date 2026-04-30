# CSC101 Final Exam Study Guide

A comprehensive review covering Modules 1–11. This guide answers every question from the Final Exam Review Exercise and summarizes the key topics from the Final Exam Topics list.

**Note:** Modules 1–6 were also covered on the midterm. If you need a deeper review of those, check the [Midterm Study Guide](../midterm_exam_review/csc101_midterm_study_guide.md).

---

## Table of Contents

- [Module 1: Course Introduction & Getting Started with Python](#module-1-course-introduction--getting-started-with-python)
- [Module 2: Introduction to Computers](#module-2-introduction-to-computers)
- [Module 3: Data Types, Variables & Expressions](#module-3-data-types-variables--expressions)
- [Module 4: Strings, Lists, Tuples, Sets & Dictionaries](#module-4-strings-lists-tuples-sets--dictionaries)
- [Module 5: Conditionals](#module-5-conditionals)
- [Module 6 & 7: Loops](#module-6--7-loops)
- [Module 8: Functions](#module-8-functions)
- [Module 9: Advanced Functions & Modules](#module-9-advanced-functions--modules)
- [Module 10: Classes & Objects](#module-10-classes--objects)
- [Module 11: File Handling](#module-11-file-handling)
- [Study Tips](#study-tips)

---

## Module 1: Course Introduction & Getting Started with Python

**1. What is the difference between `print()` and `input()` functions?**

`print()` displays output to the console. `input()` pauses the program and waits for the user to type something, then returns what they typed as a string.

```python
print("Hello!")              # displays text
name = input("Your name: ")  # waits for user input, stores as string
```

**2. What is the purpose of proper indentation in Python?**

Indentation defines code blocks in Python. Other languages use braces `{}`, but Python uses indentation. Incorrect indentation causes `IndentationError` and can change the logic of your program.

```python
if True:
    print("This is inside the if block")    # indented = part of the if
print("This is outside the if block")       # not indented = runs regardless
```

**3. What is the purpose of comments in Python code?**

Comments explain what the code does for human readers. Python ignores them when running the program. Use `#` for single-line comments and triple quotes `"""` for multi-line docstrings.

**4. What is the difference between an IDE and a text editor?**

A text editor (like Notepad, Sublime Text) is for writing code — it's lightweight with basic features like syntax highlighting. An IDE (like PyCharm, VS Code, IDLE) is a full development environment that includes a text editor plus debugging tools, code completion, a built-in terminal, and project management.

**5. True or False: In Python, you must declare a variable's type before using it (like `int x;`)**

**False.** Python is dynamically typed. You just assign a value and Python figures out the type automatically. `x = 5` makes `x` an integer without any declaration.

---

## Module 2: Introduction to Computers

**6. What is the difference between system software and application software?**

System software manages the computer hardware and provides a platform for other software to run (e.g., operating systems like Windows, macOS, Linux). Application software is designed for end users to perform specific tasks (e.g., Word, Chrome, Spotify).

**7. Explain the binary number system.**

Binary (base-2) uses only two digits: 0 and 1. Each position represents a power of 2. Computers use binary because electronic circuits have two states: on (1) and off (0).

Example: `1011` in binary = `1×8 + 0×4 + 1×2 + 1×1` = `11` in decimal.

**8. What is an algorithm?**

An algorithm is a step-by-step set of instructions for solving a problem or completing a task. It must be unambiguous, have a clear start and end, and produce a correct result. A recipe is a real-world analogy for an algorithm.

**9. What is ASCII and why is it important?**

ASCII (American Standard Code for Information Interchange) assigns a numeric value to each character. For example, `'A'` = 65, `'a'` = 97, `'0'` = 48. It's important because computers store everything as numbers — ASCII provides a standard way to represent text.

**10. List the basic steps of the software development lifecycle.**

1. Requirements gathering / planning
2. Analysis / design
3. Implementation (writing code)
4. Testing / debugging
5. Deployment
6. Maintenance

---

## Module 3: Data Types, Variables & Expressions

**11. What are the four primitive data types in Python?**

`int` (integers like `5`, `-3`), `float` (decimal numbers like `3.14`, `-0.5`), `bool` (`True` or `False`), and `str` (strings like `"hello"`).

**12. What is the difference between `//` and `/` operators?**

`/` is regular division — always returns a float. `//` is floor division — divides and rounds down to the nearest integer.

```python
7 / 2     # 3.5
7 // 2    # 3
-7 // 2   # -4 (rounds toward negative infinity)
```

**13. What does the `%` operator do?**

The modulo operator returns the **remainder** after division.

```python
10 % 3    # 1 (10 ÷ 3 = 3 remainder 1)
15 % 5    # 0 (perfectly divisible)
7 % 2     # 1 (odd number check)
```

**14. What are valid variable naming conventions in Python?**

Variable names must start with a letter or underscore, can contain letters, numbers, and underscores, and are case-sensitive. They cannot be Python keywords (`if`, `for`, `class`, etc.). Convention is `snake_case` for variables and functions.

```python
my_name = "Alice"    # valid, good style
_count = 0           # valid
2nd_place = "Bob"    # INVALID - starts with a number
```

**15. Evaluate: `10 + 5 * 2 - 3 ** 2`**

Follow operator precedence (PEMDAS): exponents first, then multiplication, then addition/subtraction left to right.

```
10 + 5 * 2 - 3 ** 2
10 + 5 * 2 - 9         # 3 ** 2 = 9
10 + 10 - 9            # 5 * 2 = 10
20 - 9                 # 10 + 10 = 20
11                     # 20 - 9 = 11
```

**Answer: `11`**

**16. Write code to swap the values of two variables `a` and `b`.**

```python
a = 5
b = 10

# Python way (tuple unpacking)
a, b = b, a

# Traditional way (with temp variable)
temp = a
a = b
b = temp
```

**Bonus question from the review: What happens with `x = "5"` and `y = 3`, then `print(x + y)`?**

**`TypeError`** — you can't add a string and an integer. Fix: `print(int(x) + y)` → `8`, or `print(x + str(y))` → `"53"`.

---

## Module 4: Strings, Lists, Tuples, Sets & Dictionaries

**17. How do you access the first character of `s = "Python"`?**

```python
s = "Python"
s[0]    # 'P' — indexing starts at 0
```

**Bonus question: What does `text[1:4]` return when `text = "Python"`?**

```python
text = "Python"
text[1:4]    # 'yth' — starts at index 1, stops BEFORE index 4
```

**18. What is the difference between a list and a tuple?**

Lists are **mutable** (you can change, add, remove items). Tuples are **immutable** (once created, they can't be modified). Lists use `[]`, tuples use `()`.

```python
my_list = [1, 2, 3]
my_list[0] = 99        # works

my_tuple = (1, 2, 3)
my_tuple[0] = 99       # TypeError!
```

Use tuples for data that shouldn't change (coordinates, RGB colors). Use lists when you need to modify the data.

**19. What does the `strip()` method do?**

Removes leading and trailing whitespace (spaces, tabs, newlines) from a string. Useful when reading from files since lines often end with `\n`.

```python
"  hello  ".strip()      # "hello"
"hello\n".strip()         # "hello"
```

**20. How do you access the value for key `"name"` in this dictionary?**

```python
person = {"name": "Bob", "age": 25, "city": "NYC"}
person["name"]       # "Bob"
person.get("name")   # "Bob" (safer — returns None if key doesn't exist)
```

**21. How do you concatenate two strings?**

```python
first = "Hello"
second = "World"
result = first + " " + second    # "Hello World"
```

**22. How do you access the last element of a list?**

```python
my_list = [10, 20, 30, 40]
my_list[-1]    # 40 — negative indexing counts from the end
```

**23. What does the `keys()` method return?**

Returns a view of all keys in a dictionary.

```python
person = {"name": "Bob", "age": 25}
person.keys()    # dict_keys(['name', 'age'])
```

Also: `.values()` returns all values, `.items()` returns all key-value pairs as tuples.

---

## Module 5: Conditionals

**24. What is the output of `5 == 5.0`?**

**`True`** — Python compares the values, not the types. `5` (int) and `5.0` (float) have the same value.

**25. What is a nested conditional?**

An `if` statement inside another `if` statement. Used when you need to check a second condition only after the first is true.

```python
age = 25
has_license = True

if age >= 16:
    if has_license:
        print("Can drive")
```

**26. What are "truthy" and "falsy" values in Python?**

Falsy values evaluate to `False` in a boolean context: `False`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `None`. Everything else is truthy.

```python
if []:
    print("This won't print")     # empty list is falsy
if [1, 2]:
    print("This will print")      # non-empty list is truthy
```

**27. What is the difference between `and` and `or`?**

`and` requires **both** conditions to be true. `or` requires **at least one** to be true.

```python
True and False    # False
True or False     # True
```

**28. Write a conditional to check if a year is a leap year (divisible by 4).**

```python
year = 2024
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

**29. Write a conditional for checkout messages based on total sale.**

```python
total = 75

if total > 150:
    print("Free Shipping & Free Gift!")
elif total > 50:
    print("Free Shipping!")
else:
    print("Ready to checkout")
```

**Note:** Check the largest value first, otherwise `total > 50` would catch everything above 50 and you'd never reach the `> 150` check.

**30. Rewrite nested ifs as if-elif-else:**

```python
# Original (nested)
x = 10
if x > 0:
    if x < 20:
        print("Between 0 and 20")

# Rewritten (flat)
x = 10
if 0 < x < 20:
    print("Between 0 and 20")

# Or with elif
if x <= 0:
    print("0 or less")
elif x < 20:
    print("Between 0 and 20")
else:
    print("20 or more")
```

---

## Module 6 & 7: Loops

**31. Write a for loop that prints numbers 5 through 12.**

```python
for i in range(5, 13):    # range stops BEFORE 13
    print(i)
```

**32. How many times will "Hello" be printed?**

```python
count = 4
while count < 7:
    print("Hello")
    count += 1
```

**3 times.** `count` starts at 4, prints at 4, 5, 6, then `count` becomes 7 and the condition `7 < 7` is `False`.

**33. How do you iterate over a string?**

```python
for char in "Python":
    print(char)    # prints each character on its own line
```

**34. What is the difference between `range(5)` and `range(1, 5)`?**

`range(5)` generates `0, 1, 2, 3, 4` (starts at 0). `range(1, 5)` generates `1, 2, 3, 4` (starts at 1). Both stop before the end value.

**35. How would you print each name in the list?**

```python
names = ["Ron", "Harry", "Hermione"]
for name in names:
    print(name)
```

**36. What is the difference between a for loop and a while loop?**

A `for` loop iterates over a sequence (list, string, range) — you know how many times it will run. A `while` loop runs as long as a condition is true — you don't always know in advance how many iterations.

Use `for` when you know the number of iterations. Use `while` when you're waiting for a condition to change (like user input or a sentinel value).

**37. Write a loop that prints only even numbers from 1 to 10.**

```python
for i in range(2, 11, 2):    # start at 2, step by 2
    print(i)

# or
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

**38. What will this nested loop print?**

```python
for i in range(4):
    for j in range(i + 3):
        print(i, j)
```

```
0 0
0 1
0 2
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
3 5
```

When `i=0`, `j` goes 0–2 (3 iterations). When `i=1`, `j` goes 0–3 (4 iterations). When `i=2`, `j` goes 0–4 (5 iterations). When `i=3`, `j` goes 0–5 (6 iterations).

**39. Write a nested loop to print a 5x3 grid of asterisks.**

```python
for row in range(3):        # 3 rows
    for col in range(5):    # 5 columns
        print("*", end=" ")
    print()                 # newline after each row
```

Output:
```
* * * * *
* * * * *
* * * * *
```

**40. Write code to count how many times 'a' appears in a string.**

```python
text = "banana"
count = 0
for char in text:
    if char == 'a':
        count += 1
print(count)    # 3

# or use the built-in method
text.count('a')    # 3
```

**41. What's the output of `[x*2 for x in range(3)]`?**

**`[0, 2, 4]`** — list comprehension that doubles each value in `range(3)` which is `0, 1, 2`.

---

## Module 8: Functions

**42. What is the purpose of a function?**

A function is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, make code easier to test and debug, and break complex problems into smaller pieces.

**43. How do you define a function in Python?**

```python
def function_name(parameters):
    """Docstring describing what the function does."""
    # function body
    return result
```

**44. What is the difference between parameters and arguments?**

**Parameters** are the variables listed in the function definition. **Arguments** are the actual values passed when you call the function.

```python
def greet(name):       # name is a PARAMETER
    print(f"Hi {name}")

greet("Alice")         # "Alice" is an ARGUMENT
```

**45. What is variable scope?**

Scope determines where a variable can be accessed. **Local** variables exist only inside the function where they're created. **Global** variables are defined outside all functions and can be read anywhere. Python follows the LEGB rule: Local → Enclosing → Global → Built-in.

**46. Write a function that evaluates f(x) = 2x - 3.**

```python
def f(x):
    return 2 * x - 3

print(f(5))     # 7
print(f(0))     # -3
print(f(-1))    # -5
```

**47. Write a function that returns True/False based on string length vs a number.**

```python
def is_longer_than(text, number):
    return len(text) > number

print(is_longer_than("hello", 3))    # True (5 > 3)
print(is_longer_than("hi", 5))       # False (2 > 5 is False)
```

**48. What do each of these built-in functions do?**

| Function | What it does |
|----------|-------------|
| `len()` | Returns the length (number of items) of a sequence |
| `sum()` | Returns the sum of all items in an iterable |
| `max()` | Returns the largest item |
| `min()` | Returns the smallest item |
| `print()` | Displays output to the console |
| `input()` | Gets text input from the user (returns a string) |

**49. What happens if you call a function without providing a required argument?**

**`TypeError`** — Python tells you how many arguments were expected vs. how many were given.

```python
def greet(name):
    print(f"Hi {name}")

greet()    # TypeError: greet() missing 1 required positional argument: 'name'
```

---

## Module 9: Advanced Functions & Modules

**50. What does `import random` allow you to do?**

It gives you access to the `random` module's functions for generating random numbers, making random choices, and shuffling sequences.

```python
import random
random.randint(1, 10)                       # random int between 1-10
random.choice(["red", "blue", "green"])     # random item from list
```

**51. How do you import a module with an alias?**

```python
import datetime as dt
today = dt.date.today()

import numpy as np    # common convention
```

**52. What are three different ways to import from a module?**

```python
import math                   # standard import — use math.sqrt()
from math import sqrt, pi    # import specific items — use sqrt() directly
import math as m              # alias — use m.sqrt()
```

There's also `from math import *` but it's not recommended because you can't tell where functions came from.

**53. What does `random.randint(1, 10)` do?**

Returns a random integer between 1 and 10, **inclusive** (both 1 and 10 are possible results).

**54. How do you get the current date and time using the datetime module?**

```python
import datetime
now = datetime.datetime.now()      # current date and time
today = datetime.date.today()      # current date only
```

**55. What is the difference between `math.floor()` and `math.ceil()`?**

`math.floor()` rounds **down** to the nearest integer. `math.ceil()` rounds **up** to the nearest integer.

```python
import math
math.floor(4.7)    # 4
math.ceil(4.3)     # 5
math.floor(-2.3)   # -3 (toward negative infinity)
math.ceil(-2.3)    # -2 (toward positive infinity)
```

**56. What is the purpose of `__name__` and when does it equal `"__main__"`?**

`__name__` is a special variable that Python sets automatically. When you run a file directly, `__name__` is set to `"__main__"`. When the file is imported as a module, `__name__` is set to the module's name. This lets you write code that only runs when the file is executed directly:

```python
if __name__ == "__main__":
    # this only runs when you run this file directly
    # it does NOT run when someone imports this file
    main()
```

---

## Module 10: Classes & Objects

**57. What is Object-Oriented Programming (OOP)?**

OOP is a programming paradigm that organizes code around **objects** rather than functions. Objects bundle data (attributes) and functionality (methods) into reusable units. The four pillars are encapsulation, abstraction, inheritance, and polymorphism.

**58. What is a class?**

A class is a **blueprint or template** that defines the structure and behavior of objects. It specifies what attributes and methods objects of that type will have. Think of it as a cookie cutter — the class is the cutter, objects are the cookies.

**59. What is an object?**

An object is a specific **instance** created from a class with actual values. Each object has its own independent data.

```python
class Dog:
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")    # buddy is an object (instance of Dog)
rex = Dog("Rex")         # rex is a different object
```

**60. How do you define a class in Python?**

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # method body
        pass
```

Class names use **PascalCase** (capital first letter of each word).

**61. What is the `__init__()` method?**

The constructor — it runs automatically when you create a new object. It initializes the object's attributes (sets up its starting state).

```python
class Student:
    def __init__(self, name, grade):
        self.name = name      # set up initial attribute
        self.grade = grade    # set up initial attribute

s = Student("Alice", 90)     # __init__ runs automatically here
```

**62. How do you create an object (instantiate a class)?**

Call the class name like a function, passing the arguments that `__init__` expects (excluding `self`):

```python
my_dog = Dog("Buddy")
my_car = Car("red", "Honda")
```

**63. What is the purpose of the `self` parameter?**

`self` refers to the **current instance** of the class. It's how methods access the specific object's attributes and other methods. Python passes it automatically — you never pass `self` yourself when calling a method.

```python
class Dog:
    def __init__(self, name):
        self.name = name        # self.name belongs to THIS specific dog

    def bark(self):
        print(f"{self.name} says Woof!")    # access THIS dog's name
```

**64. What is the difference between a class attribute and an instance attribute?**

**Class attributes** are defined in the class body, shared by ALL instances. **Instance attributes** are defined in `__init__` with `self`, unique to each object.

```python
class Dog:
    species = "Canis familiaris"    # class attribute — shared by all dogs

    def __init__(self, name):
        self.name = name            # instance attribute — unique per dog
```

Change class attributes through the **class name** (`Dog.species`), not through an instance (or you'll create a shadow copy).

**65. How do you access an object's attributes?**

Use the dot operator:

```python
my_dog = Dog("Buddy")
print(my_dog.name)        # access attribute
my_dog.bark()             # call method
```

**66. Write a `Person` class with age attribute and methods: `__init__`, `get_age`, `set_age`, `can_vote`.**

```python
class Person:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def can_vote(self):
        return self.age >= 18

p = Person(20)
print(p.get_age())       # 20
print(p.can_vote())      # True

p.set_age(15)
print(p.can_vote())      # False
```

**67. Create a `Rectangle` class with methods to calculate area and perimeter.**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 3)
print(r.area())          # 15
print(r.perimeter())     # 16
```

---

## Module 11: File Handling

**68. How do you open a file for reading in Python?**

```python
file = open("data.txt", "r")    # 'r' for read mode
# or simply
file = open("data.txt")          # read mode is the default
```

**69. What are the different file modes?**

| Mode | Description |
|------|-------------|
| `'r'` | Read only (default) — file must exist |
| `'w'` | Write — creates file or **overwrites** existing content |
| `'a'` | Append — creates file or adds to the end |
| `'r+'` | Read and write |

**70. What is the difference between `'w'` and `'a'` modes?**

`'w'` (write) **deletes all existing content** and starts fresh. `'a'` (append) **keeps existing content** and adds new data to the end. Both create the file if it doesn't exist.

**71. Why should you close a file after opening it?**

Closing a file flushes the write buffer (saves changes to disk), releases system resources, and prevents file corruption. Without closing, changes may not be saved. Best practice: use `with open()` which closes automatically.

**72. Write code to read all lines from "students.txt" using `with`.**

```python
with open("students.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())    # strip removes the trailing \n
```

**73. How do you write text to a file?**

```python
with open("output.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Second line\n")
```

Remember: `write()` only accepts strings and does NOT add newlines automatically.

**74. What is the difference between absolute and relative file paths?**

**Absolute paths** specify the complete location from the root directory: `/Users/student/data.txt` or `C:/Users/Bob/notes.txt`. **Relative paths** are relative to the current working directory: `data.txt` or `../data/file.csv`. Relative paths are more portable — they work on different machines.

**75. What method reads one line at a time from a file?**

`readline()` — reads the next line and returns it as a string (including `\n`).

```python
with open("data.txt") as file:
    first_line = file.readline()
    second_line = file.readline()
```

**76. What are common file operation errors?**

| Error | Cause |
|-------|-------|
| `FileNotFoundError` | File doesn't exist at the specified path |
| `PermissionError` | No read/write permission |
| `ValueError` | Invalid data conversion (e.g., `int("abc")`) |
| `IndexError` | Accessing a row/column that doesn't exist |
| `UnicodeDecodeError` | File encoding mismatch |

Always wrap file operations in `try/except`:

```python
try:
    with open("data.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

**77. What does `os.path.join()` do and why is it useful?**

It combines path components using the correct separator for the operating system (`/` on Mac/Linux, `\` on Windows). This makes your code cross-platform.

```python
import os
path = os.path.join("Users", "student", "data.txt")
# On Mac/Linux: "Users/student/data.txt"
# On Windows: "Users\\student\\data.txt"
```

---

## Study Tips

**Key Areas to Focus On:**

- **Syntax accuracy** — colons, indentation, parentheses
- **Data structures** — know when to use list vs tuple vs dict vs set
- **Functions** — defining, calling, parameters vs arguments, scope
- **File handling** — `with open`, read/write modes, error handling
- **OOP basics** — classes, objects, `__init__`, `self`, class vs instance attributes
- **Loops** — for vs while, nested loops, list comprehensions
- **Modules** — importing, `math`, `random`, `datetime`, `csv`

**Practice Strategy:**

1. Review all previous assignments, labs, projects, and quizzes (including midterm)
2. Practice writing code, not just reading it
3. Trace code execution step by step — predict output before running
4. Combine concepts: functions with loops, OOP with file handling, modules with functions
5. Debug intentionally broken code
6. Understand **why** things work, not just memorize syntax

**Common Cross-Module Patterns:**

```python
# Function + Loop + List
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

# Class + File I/O
class StudentReader:
    def __init__(self, filename):
        self.filename = filename

    def read_students(self):
        with open(self.filename) as f:
            return [line.strip() for line in f.readlines()]

# Module + Function + Error Handling
import csv

def read_scores(filename):
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            next(reader)    # skip header
            return [(row[0], int(row[1])) for row in reader]
    except FileNotFoundError:
        print(f"{filename} not found")
        return []
```

---
