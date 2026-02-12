# Module 4: Strings, Lists, Tuples, Sets, & Dictionaries

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Strings](#strings)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Sets](#sets)
  - [Dictionaries](#dictionaries)
  - [Comparing Data Structures](#comparing-data-structures)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

This module covers Python's built-in compound data structures: strings, lists, tuples, sets, and dictionaries. These are the tools you use to store, organize, and work with collections of data. Each one has different characteristics and is useful in different situations. Understanding when to use which one is a big part of writing good Python.

## Learning Objectives

- Explain the characteristics and differences among strings, lists, tuples, sets, and dictionaries
- Apply common string functions to manipulate and process text
- Create and manipulate lists by performing indexing, slicing, adding, updating, and iterating
- Use sets to perform operations such as union, intersection, and difference
- Construct and manage dictionaries by storing, accessing, updating, and iterating over key-value pairs

## Key Concepts

### Strings

A string is a sequence of characters. You create them with single quotes, double quotes, or triple quotes. Strings are **immutable**, meaning you can't change them after creation. Any operation that "changes" a string actually creates a new one.

```python
single_quote = 'Hello'
double_quote = "World"
multiline = '''This is a
multiline string'''
```

#### String Indexing

Every character in a string has a position (index) starting at 0:

```
 d   i   n   o   s   a   u   r
 0   1   2   3   4   5   6   7
```

```python
s = "dinosaur"
print(s[0])    # d
print(s[3])    # o
print(s[-1])   # r (negative indexing starts from the end)
print(s[8])    # IndexError: string index out of range
```

#### Escape Characters

| Escape Sequence | What It Does |
|----------------|-------------|
| `\"` | Double quote inside a double-quoted string |
| `\'` | Single quote inside a single-quoted string |
| `\n` | New line |
| `\t` | Tab |

```python
print("they said \"hello\"")     # they said "hello"
print('they said "hello"')       # they said "hello" (alternative)
```

#### String Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.upper()` | All characters to uppercase | `"hello".upper()` returns `"HELLO"` |
| `.lower()` | All characters to lowercase | `"HELLO".lower()` returns `"hello"` |
| `.capitalize()` | First letter uppercase | `"hello world".capitalize()` returns `"Hello world"` |
| `.strip()` | Removes leading/trailing whitespace | `"  hi  ".strip()` returns `"hi"` |
| `.replace(old, new)` | Replaces all occurrences | `"fox".replace("fox", "cat")` |
| `.split(delimiter)` | Splits string into a list | `"a,b,c".split(",")` returns `["a", "b", "c"]` |
| `.join(list)` | Joins a list into a string | `" ".join(["Hello", "World"])` returns `"Hello World"` |
| `.find(substring)` | Returns index of first occurrence (-1 if not found) | `"hello".find("ll")` returns `2` |
| `len(string)` | Returns the length | `len("World!")` returns `6` |

#### String Concatenation

Use `+` to combine strings. If you need to concatenate a number, cast it to a string first with `str()`.

```python
word1 = "hello"
word2 = "world"
sentence = word1 + " " + word2       # "hello world"
print("Sum: " + str(10 + 20))        # "Sum: 30"
```

### Lists

A list is an ordered, mutable collection of items inside square brackets `[]`. Lists can hold mixed data types and duplicates. Indexing starts at 0, just like strings.

```python
numbers = [5, 2, 9, 7, 5, 8, 1, 4, 3]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]
empty_list = []
```

#### Accessing Elements

```python
print(fruits[0])     # apple
print(fruits[-1])    # cherry (last element)
print(fruits[10])    # IndexError: list index out of range
```

#### Slicing

Syntax: `list[start:stop]` (stop is exclusive)

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[1:3])   # ["banana", "cherry"]
print(fruits[:2])    # ["apple", "banana"] (from beginning)
print(fruits[2:])    # ["cherry", "date"] (to end)
print(fruits[::-1])  # ["date", "cherry", "banana", "apple"] (reversed)
```

#### List Methods

| Method | What It Does |
|--------|-------------|
| `.append(item)` | Adds item to end |
| `.insert(index, item)` | Inserts item at specific position |
| `.remove(item)` | Removes first occurrence of item |
| `.pop(index)` | Removes and returns item at index (default: last) |
| `.extend(list)` | Adds all items from another list |
| `.sort()` | Sorts the list in place |
| `.reverse()` | Reverses the list in place |
| `.count(item)` | Counts occurrences of item |
| `.index(item)` | Returns index of first occurrence |
| `len(list)` | Returns number of elements |

#### List Math Functions

These work on lists of numbers:

| Function | What It Does |
|----------|-------------|
| `sum(list)` | Sum of all elements |
| `max(list)` | Highest value |
| `min(list)` | Lowest value |

#### List Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2         # [1, 2, 3, 4, 5, 6] (concatenation)
repeated = [1, 2] * 3           # [1, 2, 1, 2, 1, 2] (repetition)
```

#### Copying vs. Referencing

Be careful: `reference = original` does not copy a list. Both variables point to the same list. Use `.copy()` or slicing `[:]` to make an actual copy.

```python
original = [1, 2, 3]
reference = original          # same list in memory
copy = original[:]            # new list

reference[0] = 99
print(original)               # [99, 2, 3] (changed!)
print(copy)                   # [1, 2, 3] (unchanged)
```

### Tuples

A tuple is like a list but **immutable**. Once created, you can't add, remove, or change elements. Tuples use parentheses `()`.

```python
coordinates = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)    # comma is required for single-item tuple
```

Indexing and slicing work exactly like lists:

```python
print(colors[0])       # red
print(colors[-1])      # blue
```

#### Tuple Unpacking

You can assign each element to a variable in one line:

```python
x, y = coordinates     # x = 3, y = 4
r, g, b = colors       # r = "red", g = "green", b = "blue"
```

#### Tuple Methods

Tuples only have 2 built-in methods:

| Method | What It Does |
|--------|-------------|
| `.count(value)` | Number of times a value appears |
| `.index(value)` | Position of first occurrence |

#### When to Use Tuples

Use tuples for data that shouldn't change: coordinates, RGB colors, database records, dictionary keys. They're slightly more memory efficient than lists.

### Sets

A set is an **unordered** collection of **unique** elements inside curly braces `{}`. Duplicates are automatically removed. Sets have no index, so you can't access elements by position.

```python
numbers = {1, 2, 3, 4, 5}
car_brands = {"Toyota", "Honda", "Ford"}
duplicates = {1, 2, 2, 3, 3, 3}    # becomes {1, 2, 3}
empty_set = set()                    # not {}, that's an empty dict
```

#### Set Methods

| Method | What It Does |
|--------|-------------|
| `.add(item)` | Adds a single element |
| `.update(list)` | Adds multiple elements |
| `.remove(item)` | Removes item (raises KeyError if not found) |
| `.discard(item)` | Removes item (no error if not found) |
| `.clear()` | Removes all elements |

#### Set Operations

| Operation | Syntax | What It Returns |
|-----------|--------|----------------|
| Union | `set1 \| set2` | All elements from both sets |
| Intersection | `set1 & set2` | Only elements in both sets |
| Difference | `set1 - set2` | Elements in set1 but not set2 |

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 | set2)    # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1 & set2)    # {4, 5}
print(set1 - set2)    # {1, 2, 3}
```

### Dictionaries

A dictionary stores **key-value pairs** inside curly braces `{}`. Think of it like a real dictionary: you look up a word (key) to get its definition (value). Keys must be immutable (strings, numbers, tuples) and unique. Values can be anything.

```python
student = {
    "name": "Ada",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.85
}
```

#### Accessing Values

```python
print(student["name"])                      # Ada
print(student.get("gpa", "Not found"))      # 3.85
print(student.get("phone", "Not found"))    # Not found (safe access)
```

`.get()` is safer than `[]` because it won't crash if the key doesn't exist.

#### Modifying Dictionaries

```python
student["year"] = "Sophomore"       # add new key-value pair
student["age"] = 21                 # update existing value
del student["gpa"]                  # delete a key-value pair
student.clear()                     # remove everything
```

#### Dictionary Methods

| Method | What It Does |
|--------|-------------|
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| `.items()` | Returns all key-value pairs |
| `.get(key, default)` | Safe access with fallback value |
| `.pop(key)` | Removes and returns value for key |
| `.update(other_dict)` | Merges another dictionary in |

#### Checking for Keys

```python
print("name" in student)    # True
print("phone" in student)   # False
```

### Comparing Data Structures

| Feature | List `[]` | Tuple `()` | Set `{}` | Dict `{k:v}` |
|---------|----------|-----------|---------|-------------|
| Ordered | Yes | Yes | No | Yes* |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Values only |
| Indexed | Yes | Yes | No | By key |
| Use case | General collection, need to modify | Fixed data, coordinates, dict keys | Unique items, membership testing | Key-value lookups |

#### Converting Between Types

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)    # (1, 2, 3)
my_set = set(my_list)        # {1, 2, 3}
back_to_list = list(my_set)  # [1, 2, 3]
```

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/advanceddatatypes).

| File | Description |
|------|-------------|
| [stringbasics.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/stringbasics.py) | String creation, indexing, and find |
| [stringmethods.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/stringmethods.py) | Case conversion, strip, replace |
| [stringsplitting.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/stringsplitting.py) | Split and join with different delimiters |
| [strings.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/strings.py) | String iteration, ASCII values, concatenation |
| [listbasics.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/listbasics.py) | List creation, indexing, slicing, math |
| [listmethods.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/listmethods.py) | append, insert, remove, pop, sort, reverse |
| [arrays.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/arrays.py) | Lists as arrays with iteration and sum |
| [tuples.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/tuples.py) | Tuple creation, unpacking, immutability |
| [sets.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/sets.py) | Set operations: union, intersection, difference |
| [dictionaries.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/dictionaries.py) | Dictionary creation, access, modification, methods |
| [comparingstructures.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/comparingstructures.py) | Side-by-side comparison of all data structures |
| [emptycollections.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/emptycollections.py) | Empty collections, lengths, and boolean tests |
| [liststuplesdictionaries.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/liststuplesdictionaries.py) | Comprehensive demo with practical examples |
| [grademanagementsystem.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/advanceddatatypes/grademanagementsystem.py) | Capstone: all data structures in a grade tracker |

## My Example Code

These focus on the concepts that tend to trip students up the most.

| File | Description |
|------|-------------|
| [mutable_vs_immutable.py](examples/mutable_vs_immutable.py) | Why you can change a list but not a string or tuple |
| [slicing_explained.py](examples/slicing_explained.py) | The off-by-one confusion with `[start:stop]` |
| [copy_vs_reference.py](examples/copy_vs_reference.py) | Why `list_b = list_a` doesn't copy, and how to fix it |
| [sets_vs_dicts.py](examples/sets_vs_dicts.py) | Both use `{}` but work completely differently |

## Resources

- [Course GitHub Repository: Advanced Data Types](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/advanceddatatypes)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Introduction to Computational Thinking in Python](https://muzny.github.io/csci1200-notes/02/2/intro_python.html)
- [Python for Everybody](https://www.py4e.com/book.php)