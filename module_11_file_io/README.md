# Module 11 — File I/O

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Why File I/O?](#why-file-io)
  - [Opening Files](#opening-files)
  - [File Modes](#file-modes)
  - [Writing to Files](#writing-to-files)
  - [Reading from Files](#reading-from-files)
  - [The with Statement](#the-with-statement)
  - [Working with File Paths](#working-with-file-paths)
  - [Processing Data from Files](#processing-data-from-files)
  - [Writing Lists to Files](#writing-lists-to-files)
  - [CSV Files](#csv-files)
  - [The csv Module](#the-csv-module)
  - [Exception Handling with Files](#exception-handling-with-files)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

File Input/Output (I/O) is how your programs interact with data stored on disk. Up until now, every variable you've created disappears when the program ends. File I/O lets you persist data beyond program execution — save it to a file, read it back later, or process large datasets from external sources like CSVs, JSON files, or databases. This module covers opening, reading, writing, and closing files, the `with` statement for safe file handling, CSV processing, and how to handle file-related errors with exceptions.

## Learning Objectives

- Understand the concept of File Input/Output (I/O)
- Write data to a file using write mode and append mode
- Read and process data from files using `read()`, `readline()`, and `readlines()`
- Implement the `with` statement for safe and efficient file handling
- Process `.csv` files for data science applications
- Handle File I/O errors with exception handling

## Key Concepts

---

### Why File I/O?

So far, all data has lived in variables that disappear when the program closes. File I/O solves this:

- **Data persistence** — store data beyond program execution
- **Large datasets** — read data from spreadsheets, databases, JSON files
- **Configuration** — read settings from external files
- **Data sharing** — share data between different programs

The basic file I/O operations are: open a file, read from it or write to it, and close the file.

---

### Opening Files

The `open()` function creates a file object that lets you interact with a file. It takes two arguments: the filename and the mode.

```python
file = open("data.txt", "r")    # open for reading
file = open("output.txt", "w")  # open for writing
file = open("log.txt", "a")     # open for appending
```

If only the filename is given (no path), Python looks in the current directory. If the file doesn't exist when reading, you get a `FileNotFoundError`.

**Always close files when done:**

```python
file = open("data.txt", "r")
content = file.read()
file.close()    # don't forget this!
```

---

### File Modes

| Mode | Description | File doesn't exist? | File already exists? |
|------|-------------|--------------------|--------------------|
| `'r'` | Read only (default) | `FileNotFoundError` | Opens normally |
| `'w'` | Write | Creates new file | **Overwrites everything** |
| `'a'` | Append | Creates new file | Adds to the end |

**Warning:** Write mode `'w'` deletes all existing content. If you want to keep what's already there, use append mode `'a'`.

---

### Writing to Files

Use `file.write()` to write data to a file. Important rules:

- `write()` accepts **strings only** — you must convert numbers with `str()`
- There are **no automatic newlines** — you must add `\n` explicitly
- You must call `file.close()` to save changes (it writes to a buffer first)

```python
file = open("output.txt", "w")
file.write("Hello, world!\n")
file.write("This will replace any old content.")
file.close()
```

**Writing numbers — must convert to string first:**

```python
name = "Alice"
age = 25
score = 95.5

file = open("data.txt", "w")
file.write(name + "\n")
file.write(str(age) + "\n")        # convert int to string
file.write(str(score) + "\n")      # convert float to string
file.close()
```

**Appending to an existing file:**

```python
file = open("log.txt", "a")
file.write("New entry at 06:46 PM MST\n")
file.close()
```

Each time you run this, the line is tacked onto the end. Existing content is preserved.

---

### Reading from Files

Three methods for reading:

**`read()` — reads the entire file as one string:**

```python
file = open("data.txt", "r")
content = file.read()       # entire file in one string
print(content)
file.close()
```

**`readline()` — reads the next line as a string:**

```python
file = open("data.txt", "r")
line = file.readline()      # first line only
print(line)
file.close()
```

**`readlines()` — reads all lines into a list:**

```python
file = open("data.txt", "r")
lines = file.readlines()    # list of strings, one per line
print(lines[0])             # first line
print(lines[2])             # third line
file.close()
```

Each line in the list includes the `\n` character at the end. Use `.strip()` to remove it:

```python
for line in lines:
    clean_line = line.strip()    # removes \n and whitespace
    print(clean_line)
```

---

### The with Statement

The `with` statement is the **recommended** way to handle files. It automatically closes the file when the block exits, even if an error occurs. No more forgetting `file.close()`.

```python
# without with — you have to remember to close
file = open("data.txt", "r")
content = file.read()
file.close()

# with — file closes automatically
with open("data.txt", "r") as file:
    content = file.read()
# file is closed here automatically
```

**Writing with `with`:**

```python
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
# file is closed and saved automatically
```

**Why use `with`:**

- Prevents file leaks (files left open)
- Cleaner code — no need for `file.close()`
- File closes even if an exception occurs inside the block

Unless you have a specific reason not to, always use `with open`.

---

### Working with File Paths

When the file isn't in the same folder as your script, you need to provide the full path.

**macOS / Linux:**

```python
open("/Users/student/Documents/data.txt", "r")
```

**Windows:**

```python
open("C:/Users/Bob/Desktop/notes.txt", "w")       # best — forward slashes work on all OS
open("C:\\Users\\Bob\\Desktop\\notes.txt", "w")    # works but messy — need double backslashes
```

**Best practice:** Always use forward slashes `/` in file paths. Python automatically converts them to the correct separator on Windows. This makes your code cross-platform.

---

### Processing Data from Files

You can use loops to process file data line by line. Here's a common pattern — reading numbers from a file and calculating the average:

```python
with open("test_data.txt", "r") as file:
    lines = file.readlines()

total = 0
count = 0
for line in lines:
    number = float(line.strip())    # strip \n, convert to float
    total += number
    count += 1

average = total / count
print(f"Average: {average}")
```

---

### Writing Lists to Files

If you have a list, you can write each item to a file using a loop:

```python
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
```

**Appending more items later:**

```python
new_students = ["Frank", "Grace"]

with open("students.txt", "a") as file:
    for student in new_students:
        file.write(student + "\n")
```

---

### CSV Files

CSV (Comma-Separated Values) is a plain-text format for tabular data. Each line is a row, values are separated by commas. It's widely supported by Excel, Google Sheets, and databases.

```
Title,Author,Year,Genre
The Hobbit,J.R.R. Tolkien,1937,Fantasy
Dune,Frank Herbert,1965,Science Fiction
```

**Manual CSV parsing** — read lines, strip newlines, split on commas:

```python
with open("books.csv") as file:
    rows = file.readlines()

list_csv = []
for row in rows:
    row = row.strip("\n")           # remove trailing newline
    cells = row.split(",")          # split into list by comma
    list_csv.append(cells)          # add row to 2-D list

print(list_csv)
# [['Title', 'Author', 'Year', 'Genre'], ['The Hobbit', 'J.R.R. Tolkien', '1937', 'Fantasy'], ...]
```

**Caution:** This manual approach assumes no commas inside quoted fields (e.g., `"Doe, John"`). For real-world CSVs, use the `csv` module instead.

---

### The csv Module

Python's built-in `csv` module handles edge cases like commas inside quoted fields, escaped characters, and blank lines.

```python
import csv

with open("books.csv", newline='') as file:
    reader = csv.reader(file)
    list_csv = [row for row in reader]    # list comprehension

print(list_csv)
```

**Why use the csv module:**

- Automatically handles quoted fields with commas (`"Orwell, George"`)
- Manages `\n` edge cases
- Use `newline=''` in `open()` to avoid blank lines on some systems

**Processing CSV data with error handling:**

```python
import csv

try:
    with open("scores.csv", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            score = int(row[1])
            print(f"{name}: {score}")
except FileNotFoundError:
    print("CSV file not found.")
except (IndexError, ValueError) as e:
    print(f"Invalid row format: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
```

---

### Exception Handling with Files

File operations are error-prone — the file might be missing, corrupted, or locked. Use `try/except` to handle errors gracefully.

**Basic try/except:**

```python
try:
    file = open("data.txt")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found!")
except:
    print("An error occurred")
```

**Problem:** If an error happens during `file.read()`, the file never gets closed. Best practice is to combine `with` and `try/except`:

```python
try:
    with open("data.txt") as file:
        content = file.read()
    # file auto-closed here
except FileNotFoundError:
    print("Error: File not found. Check the path.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"Unexpected error: {e}")
```

**Common file-related exceptions:**

| Exception | When it happens |
|-----------|----------------|
| `FileNotFoundError` | File path doesn't exist (reading) |
| `PermissionError` | No read/write access |
| `ValueError` | Invalid data conversion (e.g., `int("abc")`) |
| `IndexError` | Accessing a row/column that doesn't exist |
| `UnicodeDecodeError` | File encoding mismatch |

---

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgetting to close the file | File stays open, changes may not save | Use `with open()` — it closes automatically |
| Using `'w'` when you meant `'a'` | All existing content is deleted | Use append mode `'a'` to keep existing data |
| Forgetting `\n` when writing | All text ends up on one line | Add `\n` explicitly: `file.write("text\n")` |
| Writing a number without `str()` | `TypeError: write() argument must be str` | Convert first: `file.write(str(age) + "\n")` |
| Not stripping `\n` when reading | Extra blank lines, comparison failures | Use `line.strip()` to remove whitespace |
| Manual CSV parsing with commas in data | Fields get split incorrectly | Use the `csv` module instead of `split(",")` |
| Reading a file that doesn't exist | `FileNotFoundError` crashes the program | Wrap in `try/except` |

---

## Quick Reference

```python
# READING
with open("file.txt", "r") as f:
    content = f.read()        # entire file as string
    # or
    line = f.readline()       # one line
    # or
    lines = f.readlines()     # list of lines

# WRITING (overwrites!)
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write(str(42) + "\n")   # numbers must be str()

# APPENDING
with open("file.txt", "a") as f:
    f.write("Added to end\n")

# CSV with csv module
import csv
with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)            # each row is a list

# ERROR HANDLING
try:
    with open("file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
```

---

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/fileio).

| File | Description |
|------|-------------|
| [readfile.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/readfile.py) | Read a file and print its contents using `with open` |
| [writefile.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/writefile.py) | Write to a file using `open()` in write mode |
| [readingcsv.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/readingcsv.py) | Manual CSV parsing — readlines, strip, split |
| [csvmodule.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/csvmodule.py) | CSV parsing using the `csv` module with list comprehension |
| [data.txt](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/data.txt) | Sample data file — historic computers and their years |
| [books.csv](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/fileio/books.csv) | Sample CSV — book titles, authors, years, genres |

## My Example Code

| File | Description |
|------|-------------|
| [file_mode_traps.py](examples/file_mode_traps.py) | The traps that get everyone — write vs append, forgetting newlines, not stripping when reading, and the file-not-closed bug |
| [csv_processing.py](examples/csv_processing.py) | Reading and processing CSV data step by step — manual parsing vs the csv module, filtering rows, and handling bad data |

## Resources

- [Course GitHub Repository: File I/O](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/fileio)
- [Reading and Writing Files (Official Python Documentation)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python File Handling (W3Schools)](https://www.w3schools.com/python/python_file_handling.asp)
- [Reading and Writing CSV Files in Python (Real Python)](https://realpython.com/python-csv/)
- [csv Module (Official Python Documentation)](https://docs.python.org/3/library/csv.html)