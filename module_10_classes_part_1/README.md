# Module 10 — Classes (Part 1): Introduction to OOP

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [Classes vs. Objects](#classes-vs-objects)
  - [Defining a Class](#defining-a-class)
  - [The __init__ Method (Constructor)](#the-__init__-method-constructor)
  - [The self Parameter](#the-self-parameter)
  - [Instance Methods](#instance-methods)
  - [Class Attributes vs. Instance Attributes](#class-attributes-vs-instance-attributes)
  - [Encapsulation](#encapsulation)
  - [UML Class Diagrams](#uml-class-diagrams)
  - [The Four Pillars of OOP](#the-four-pillars-of-oop)
  - [Naming Conventions (PEP 8)](#naming-conventions-pep-8)
  - [Variable Naming for Instances](#variable-naming-for-instances)
  - [Common Mistakes](#common-mistakes)
- [Example Code From the Class](#example-code-from-the-class)
- [My Example Code](#my-example-code)
- [Resources](#resources)

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects** rather than functions and logic. Objects bundle **data** (attributes) and **functionality** (methods) into reusable units. This module covers how to define classes, create objects, use constructors and instance methods, and understand the difference between class and instance attributes.

### Why Use OOP?

- **Organization** — group related data and functions together
- **Reusability** — create multiple objects from the same class
- **Maintainability** — easier to update and debug
- **Real-world modeling** — represent real entities naturally in code

## Learning Objectives

- Explain the role of classes as blueprints for creating objects and distinguish between a class and an instance
- Write Python code to define a class with attributes and methods using the `class` keyword and instantiate objects from it
- Define instance attributes using the `__init__` method and create instance methods to perform operations on object data
- Correctly use the `self` parameter to access and manipulate instance attributes and methods within a class
- Identify and implement class attributes shared across all instances and understand how they differ from instance attributes
- Apply encapsulation by organizing data and methods within a class and interacting with objects through method calls

## Key Concepts

---

## Classes vs. Objects

A **class** is a blueprint or template. It defines what an object should contain and how it should behave.

An **object** (also called an **instance**) is a specific realization of that template, created from a class with actual values.

**Analogy:** The class is the cookie cutter. The object is the actual cookie.

```python
# Class = blueprint
class Dog:
    pass

# Objects = instances created from the blueprint
my_dog = Dog()
your_dog = Dog()
```

You can build many objects from one class. Each object is independent — changing one does not affect another.

---

## Defining a Class

Use the `class` keyword, followed by the class name (PascalCase) and a colon. The class body is indented.

```python
class ClassName:
    # class body goes here
    pass
```

Use `pass` as a placeholder if you want an empty class for testing.

---

## The `__init__` Method (Constructor)

The `__init__` method is a **constructor** that runs automatically when you create a new object. It sets up the object's initial state by assigning values to **instance attributes**.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute
```

**Key points:**

- `__init__` runs automatically when creating an object — you never call it directly
- It always takes `self` as the first parameter
- Parameters after `self` become the values you pass when creating instances
- Each instance gets its own copy of the attributes

### Creating Objects with Attributes

```python
my_dog = Dog("Buddy", 3)
your_dog = Dog("Max", 5)

print(my_dog.name)    # Buddy
print(your_dog.age)   # 5
```

Each object has its own independent data. `my_dog.name` is `"Buddy"` and `your_dog.name` is `"Max"` — they don't interfere with each other.

---

## The `self` Parameter

`self` is a reference to the **current instance** of the class. It's how the object refers to itself.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width      # store in THIS instance
        self.height = height    # store in THIS instance

    def area(self):
        return self.width * self.height  # access THIS instance's data
```

**Rules:**

- `self` must be the first parameter in every instance method
- You don't pass `self` when calling methods — Python does it automatically
- Use `self.attribute_name` to access instance attributes
- Use `self.method_name()` to call other instance methods

### Common Mistake: Forgetting `self`

```python
class Example:
    def __init__(self, value):
        value = value       # WRONG — doesn't save to the instance
        self.value = value  # CORRECT — saves to the instance
```

Without `self.`, the assignment creates a local variable that disappears when `__init__` ends. The attribute is never stored on the object.

---

## Instance Methods

Instance methods are functions defined inside a class that operate on a specific object. They always take `self` as their first parameter, giving them access to that object's attributes and other methods.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_info(self):
        return f"{self.name} is {self.age} years old"

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! Now {self.age} years old.")
```

```python
my_dog = Dog("Buddy", 3)
my_dog.bark()            # Buddy says Woof!
print(my_dog.get_info()) # Buddy is 3 years old
my_dog.have_birthday()   # Happy Birthday Buddy! Now 4 years old.
```

Each method uses `self` to interact with the individual dog it belongs to. `bark()` makes **that** dog speak. `have_birthday()` updates **that** dog's age, leaving all other `Dog` instances untouched.

---

## Class Attributes vs. Instance Attributes

### Instance Attributes

- **Unique** to each object
- Defined inside `__init__` using `self`
- Created when `__init__` runs during object creation

```python
self.name = name   # each object gets its own name
```

### Class Attributes

- **Shared** by all instances of the class
- Defined in the class body, outside of any method
- Accessed via the class name or any instance

```python
class Dog:
    species = "Canis familiaris"  # class attribute — shared by all dogs

    def __init__(self, name):
        self.name = name          # instance attribute — unique per dog
```

```python
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(dog1.name)     # Buddy
print(dog2.name)     # Max
```

### Changing Class Attributes

Changing a class attribute through the **class name** affects all instances:

```python
class BankAccount:
    interest_rate = 0.02

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(acc1.interest_rate)  # 0.02
print(acc2.interest_rate)  # 0.02

BankAccount.interest_rate = 0.03  # change via class name

print(acc1.interest_rate)  # 0.03 — updated for ALL instances
print(acc2.interest_rate)  # 0.03 — updated for ALL instances
```

### Shadowing Trap

Assigning through an **instance** creates a new instance attribute that **shadows** the class attribute:

```python
acc1.interest_rate = 0.05  # creates instance attribute on acc1 only!
print(acc1.interest_rate)  # 0.05 — acc1's own copy
print(acc2.interest_rate)  # 0.03 — still uses the class attribute
```

**Rule of thumb:** Use class attributes for data that should be the same across all instances (defaults, config values, counters). Use instance attributes for data that varies per object (names, balances, records).

---

## Encapsulation

Encapsulation is the practice of bundling an object's data and the methods that operate on that data into a single, self-contained unit. It hides internal details and exposes only a clean interface.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # leading underscore = "protected by convention"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance
```

```python
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())  # 120
```

Users interact through methods (`deposit`, `withdraw`, `get_balance`) rather than touching `_balance` directly. This protects the object's integrity.

### Privacy Conventions

Python doesn't enforce true privacy — it relies on naming conventions:

| Convention | Meaning | Example |
|---|---|---|
| `name` | Public — access from anywhere | `self.name` |
| `_name` | Protected — "don't touch from outside" | `self._balance` |
| `__name` | Name-mangled — becomes `_ClassName__name` internally | `self.__account_id` |

---

## UML Class Diagrams

UML (Unified Modeling Language) diagrams are a visual blueprint for designing classes before writing code. A UML class diagram has three sections:

```
+-------------------------------+
|          ClassName            |
+-------------------------------+
| - attribute1: type            |
| - attribute2: type            |
+-------------------------------+
| + method1(param: type): type  |
| + method2(): type             |
+-------------------------------+
```

- **Top section** — class name
- **Middle section** — attributes (variables)
- **Bottom section** — methods (functions)

### Access Modifiers

| Symbol | Meaning | Description |
|---|---|---|
| `+` | Public | Accessible from anywhere |
| `-` | Private | Accessible only within the class |

Usually attributes are private (`-`) and methods are public (`+`).

### Example: Student Class UML

```
+---------------------------+
|         Student           |
+---------------------------+
| - name: str               |
| - student_id: int         |
+---------------------------+
| + __init__(name, id)      |
| + display_info()          |
+---------------------------+
```

Translates to:

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}")
```

---

## The Four Pillars of OOP

Module 10 focuses on **encapsulation**. The other three pillars will be covered in later modules:

1. **Encapsulation** — bundle data and methods together; protect internal state
2. **Abstraction** — hide complex details behind simple interfaces
3. **Inheritance** — a class can inherit attributes/methods from another class
4. **Polymorphism** — different classes can share the same interface but behave differently

---

## Naming Conventions (PEP 8)

| Element | Convention | Examples |
|---|---|---|
| Class names | PascalCase | `Dog`, `BankAccount`, `StudentProfile` |
| Methods | snake_case | `bark()`, `get_info()`, `have_birthday()` |
| Instance variables | snake_case | `name`, `account_balance`, `x_loc` |
| Constants | UPPER_CASE | `MAX_SPEED`, `TARGET_VALUE` |
| Protected attributes | `_leading_underscore` | `_balance`, `_internal_id` |
| Strongly private | `__double_underscore` | `__secret_key`, `__account_id` |

**General rule:** Class names should be **nouns** (`Car`, `Student`). Method names should be **verbs** (`drive()`, `update_record()`).

---

## Variable Naming for Instances

Name the variable after **the role the object plays**, not after the data it contains:

```python
# GOOD — variable describes the role
pet = Dog("Snoopy", "Beagle")
lead_dog = Dog("Togo", "Husky")
current_user = User("alice@example.com")

# BAD — variable duplicates the data
snoopy = Dog("Snoopy", "Beagle")   # what if snoopy.name changes?
```

Let the variable name describe the **role**. Let the object's attributes describe the **data**.

---

## Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Forgetting `self` in method parameters | `TypeError: method() takes 0 positional arguments but 1 was given` | Always include `self` as the first parameter |
| Not using `self.` to access attributes | Creates a local variable instead of an instance attribute | Use `self.attribute` inside methods |
| Confusing class and instance attributes | Accidentally shadowing a class attribute through an instance | Change class attributes via `ClassName.attr`, not `instance.attr` |
| Incorrect object creation | `Dog.bark()` instead of `my_dog = Dog(); my_dog.bark()` | Create an instance first, then call methods on it |
| Naming variables after data | `snoopy = Dog("Snoopy")` — becomes misleading if name changes | Name after role: `pet = Dog("Snoopy")` |

---

## Quick Reference

```python
# 1. Define a class
class Dog:
    species = "Canis familiaris"       # class attribute

    def __init__(self, name, age):     # constructor
        self.name = name               # instance attribute
        self.age = age                 # instance attribute

    def bark(self):                    # instance method
        print(f"{self.name} says Woof!")

    def have_birthday(self):           # method that modifies state
        self.age += 1

# 2. Create objects
pet = Dog("Buddy", 3)
stray = Dog("Rex", 7)

# 3. Use methods
pet.bark()                            # Buddy says Woof!
pet.have_birthday()
print(pet.age)                        # 4

# 4. Access class attribute
print(Dog.species)                    # Canis familiaris
print(pet.species)                    # Canis familiaris
```

---

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/classes1).

| File | Description |
|------|-------------|
| [animal_hierarchy.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/classes1/animal_hierarchy.py) | Animal/Dog/Cat class hierarchy - constructors, inheritance preview, method overriding, super() |
| [bank_account.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/classes1/bank_account.py) | Class vs instance attributes, the shadowing trap, encapsulated BankAccount |
| [my_class.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/classes1/my_class.py) | Simple class with default parameters in __init__ |

## My Example Code

| File | Description |
|------|-------------|
| [class_vs_instance_traps.py](examples/class_vs_instance_traps.py) | The traps that get everyone - shadowing class attributes, mutable shared lists, forgetting self, and the silent bugs |
| [how_self_works.py](examples/how_self_works.py) | What self actually is, how Python passes it behind the scenes, tracing it through a class, and methods calling methods |
| [building_a_class.py](examples/building_a_class.py) | The thinking process for writing a class from scratch - from "what am I modeling?" to skeleton to finished code |

## Resources

- [Course GitHub Repository: Classes 1](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/classes1)
- [Python Classes (Official Documentation)](https://docs.python.org/3/tutorial/classes.html)
- [Python Classes and Objects (W3Schools)](https://www.w3schools.com/python/python_classes.asp)
- [Object-Oriented Programming in Python (Real Python)](https://realpython.com/python3-object-oriented-programming/)
- [UML Class Diagrams (Visual Paradigm Guide)](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-class-diagram/)