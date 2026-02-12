# Module 1: Course Intro & Foundations

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Setting Up Your Environment](#setting-up-your-environment)
  - [Install Python](#1-install-python)
  - [Pick an IDE](#2-pick-an-ide)
  - [Google Colab](#3-google-colab-no-install-needed)
- [Key Concepts](#key-concepts)
  - [Why Computer Science Matters](#why-computer-science-matters)
  - [Decomposition](#decomposition)
  - [Algorithmic Thinking](#algorithmic-thinking)
  - [Programming Languages](#programming-languages)
  - [File Systems](#file-systems)
  - [Your First Python Program](#your-first-python-program)
  - [Ways to Run Python](#ways-to-run-python)
- [Example Code From the Class](#example-code-from-the-class)
- [Resources](#resources)

## Overview

This module is all about getting set up and understanding the basics before we start coding. It covers why CS matters, how to think about problems like a programmer, and how to get Python and your IDE ready to go. By the end of it you should have Python installed, know how to navigate your file system, and have your first program running.

## Learning Objectives

- Why computer science matters
- Introduction to VS Code & Google Colab
- Using the file system (files/directories)
- Your first Python program: Hello, World!

## Setting Up Your Environment

### 1. Install Python

1. Head to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest version for your OS
3. Run the installer. Make sure you check "Add Python to PATH" (seriously, don't skip this)
4. Choose "Install Now" for default settings

### 2. Pick an IDE

An IDE (Integrated Development Environment) is basically a text editor with superpowers. It lets you write, run, and debug code all in one place.

**VS Code (Recommended for this course)**
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- After installing, open it up, click the Extensions icon on the sidebar, search "Python", and install the one from Microsoft
- It's free, lightweight, and has a built-in terminal

**PyCharm (Another solid option)**
- Grab the free Community Edition from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)
- It's heavier than VS Code but has more Python-specific features built in

The course recommends VS Code since that's what's installed in the classrooms and labs. Either one works though.

### 3. Google Colab (No Install Needed)

If you want to skip the setup entirely (or can't get Python installed yet), [Google Colab](https://colab.research.google.com/) lets you write and run Python right in your browser. Just sign in with your Google account and you're good to go.

It's great for labs, experimenting, and sharing code. But for actual projects and regular practice, you'll want a local IDE eventually.

## Key Concepts

### Why Computer Science Matters

Python is used in about 80% of AI applications so it's a pretty important language to learn. CS shows up everywhere: healthcare, business, education, entertainment, transportation, etc. The point of this course isn't just to learn how to write code but to develop the thinking skills that come with it.

### Decomposition

This is just breaking big problems into smaller pieces. Instead of trying to solve everything at once, you figure out the main goal, split it into sub-tasks, and keep breaking those down until each piece is small enough to handle on its own. It's a fundamental skill that comes up constantly in programming.

### Algorithmic Thinking

An algorithm is a step-by-step process to solve a problem. Think of it like directions to get somewhere or instructions to build furniture. A good algorithm needs three things:

| Property | What It Means |
|----------|---------------|
| Definiteness | Every step is clear, no guessing |
| Finiteness | It has to end at some point |
| Effectiveness | Each step is actually doable with what you have |

It's not just about coding. It's about taking what you want the computer to do and describing exactly how it should do it.

### Programming Languages

| Type | Examples | What It Means |
|------|----------|---------------|
| High-level | Python, Java | Human-readable, easier to write |
| Low-level | Machine code, assembly | Closer to the hardware |
| Compiled | C++, Java | Translates the whole program before running |
| Interpreted | Python, JavaScript | Reads and executes code line by line |

An **IDE** (Integrated Development Environment) combines a text editor with tools to run and debug your code. VS Code is recommended for this course. PyCharm and IDLE are also options.

### File Systems

As programmers we need to know how files and folders are organized on a computer. Phones and tablets hide this from you but when you're writing code, you need to understand it.

| Term | What It Means |
|------|---------------|
| File | An individual document, program, or piece of data |
| Folder (Directory) | A container that holds files and other folders |
| Path | The full address of where a file lives |
| Current Directory | Where you are right now (`.`) |
| Parent Directory | One level up (`..`) |
| Root Directory | The very top level (`C:\` on Windows, `/` on Mac/Linux) |
| Home Directory | Your personal user folder (`~` on Mac/Linux) |

#### Absolute vs. Relative Paths

An absolute path is the full address from the root:

| OS | Example |
|----|---------|
| Windows | `C:\Users\YourName\Documents\hello.py` |
| Mac/Linux | `/Users/YourName/Documents/hello.py` |

A relative path is based on where you currently are:

| Path | What It Means |
|------|---------------|
| `hello.py` | Same folder |
| `../Desktop/file.txt` | Go up one level, then into Desktop |

#### Common File Extensions

| Extension | What It Is |
|-----------|------------|
| `.py` | Python source code |
| `.txt` | Plain text |
| `.csv` | Comma-separated data |
| `.json` | JSON data format |
| `.md` | Markdown documentation |
| `.html` | Web page |

#### Basic Terminal Commands

You'll use the terminal (or command prompt on Windows) to navigate your files and run Python scripts.

| What You Want to Do | Windows (`cmd`) | Mac/Linux (`terminal`) |
|---------------------|----------------|----------------------|
| List files | `dir` | `ls` |
| Change directory | `cd folder_name` | `cd folder_name` |
| Go up one level | `cd ..` | `cd ..` |
| Create a folder | `mkdir new_folder` | `mkdir new_folder` |
| Print current location | N/A | `pwd` |

Special symbols: `.` (current directory), `..` (parent directory), `~` (home directory on Mac/Linux)

### Your First Python Program

```python
print("Hello, World!")
```

`print()` displays output to the screen. Python files use the `.py` extension.

### Ways to Run Python

| Method | How |
|--------|-----|
| VS Code | Click the Run button (play icon) or press F5 |
| Google Colab | Type code in a cell, press Shift+Enter |
| Command line | Navigate to the file in your terminal, run `python hello.py` |
| Interactive mode | Type `python` in your terminal to enter commands one at a time. Good for quick tests |

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/gettingstarted).

| File | Description |
|------|-------------|
| [hello.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/gettingstarted/hello.py) | A "Hello, World" program |
| [example.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/gettingstarted/example.py) | Walkthrough of the example program from the slides |
| [indent.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/gettingstarted/indent.py) | Indentation in Python (for students with prior programming experience) |

## Resources

- [Course GitHub Repository: Getting Started](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/gettingstarted)
- [Python Downloads](https://www.python.org/downloads/)
- [VS Code Download](https://code.visualstudio.com/)
- [Google Colab](https://colab.research.google.com/)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)
- [Think Python 2e (Downey)](https://greenteapress.com/wp/think-python-2e/)