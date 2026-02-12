# Module 2: Introduction to Computers

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
  - [How Computing Changed Our World](#how-computing-changed-our-world)
  - [Computer History](#computer-history)
  - [Computer Hardware](#computer-hardware)
  - [Software Development Lifecycle (SDLC)](#software-development-lifecycle-sdlc)
  - [Number Systems](#number-systems)
  - [Data Representation](#data-representation)
  - [Debugging](#debugging)
- [Example Code From the Class](#example-code-from-the-class)
- [Resources](#resources)

## Overview

This module gives you the background on how computers actually work before we start writing real code. It covers the history of computing, hardware components, how software gets built (SDLC), and how data is represented at the lowest level with binary, octal, hex, ASCII, and Unicode. It's a lot of theory but it gives you the framework for understanding why things work the way they do.

## Learning Objectives

- Identify and describe the primary components of a computer (CPU, RAM, storage, motherboard, etc.)
- Discuss the societal and cultural effects of major computer science breakthroughs
- Understand Binary and ASCII Data Representation
- Explain the purpose and significance of Unicode in global text representation

## Key Concepts

### How Computing Changed Our World

Computing has transformed pretty much everything. Here are the big ones:

| Area | Impact |
|------|--------|
| Internet | Connected billions of people, real-time communication, global collaboration |
| Mobile Computing | Smartphones put computers in everyone's pocket, apps for everything |
| AI | Virtual assistants, recommendations, self-driving cars, medical diagnosis |
| Social Media | Changed how we communicate, spread information faster, but also misinformation |
| E-commerce | Shop from anywhere 24/7, small businesses can reach global markets, digital payments |

These are all interconnected. Your phone accesses the internet, uses AI, runs social media, and handles e-commerce. But it also raises questions about privacy, security, and digital well-being.

### Computer History

A quick timeline of how we got here:

| Era | Key Developments |
|-----|-----------------|
| Ancient Times | Abacus, Antikythera Mechanism, Napier's Bones |
| 1600s-1800s | Pascal's Pascaline (1642), Leibniz Calculator (1673), Jacquard Loom (1804, first programmable machine using punched cards) |
| 1820s-1840s | Babbage's Difference Engine (1822), Analytical Engine (1837, first general-purpose computer design), Ada Lovelace (1843, first programmer) |
| 1st Gen (1940s) | ENIAC (30 tons, 18,000 vacuum tubes), EDVAC (first stored-program computer) |
| 2nd Gen (1950s-60s) | Transistors replaced vacuum tubes, FORTRAN (1957), COBOL (1959) |
| 3rd Gen (1960s-70s) | Integrated circuits, Moore's Law (1965, transistor density doubles every 2 years) |
| Personal Computing (1970s-90s) | Intel 4004 (1971, first commercial microprocessor), Apple II (1977), IBM PC (1981), Windows (1985) |
| Internet Era (1990s+) | ARPANET (1969), World Wide Web (1989), Python (1991), Java (1995), JavaScript (1995) |

Fun fact: things like generative AI and deep learning are based on ideas from over 50 years ago.

### Computer Hardware

The physical components that make up a computer:

| Component | What It Does |
|-----------|-------------|
| CPU (Central Processing Unit) | The brain. Executes instructions billions of times per second. Has an ALU (math/logic), Control Unit (manages execution), and Cache (fast storage) |
| RAM (Random Access Memory) | Fast, temporary memory. Holds programs and data the CPU is actively using. Volatile, so it's gone when power is off |
| Storage (HDD/SSD) | Permanent memory. Slower than RAM but keeps data when power is off. SSDs are replacing HDDs since they have no moving parts |
| Motherboard | Connects everything together. CPU, RAM, storage, and I/O devices all plug into it |
| GPU (Graphics Processing Unit) | Dedicated processor for graphics. Used for video editing, gaming, and now AI/ML |
| Power Supply (SMPS) | Provides stable power to all the internal components |
| Input Devices | Keyboard, mouse, microphone, camera, touchscreen, sensors |
| Output Devices | Monitor, speakers, printer |

**How it all works together:** Your program gets loaded into RAM. The CPU grabs instructions from RAM one at a time, executes them, and stores the results. It does this billions of times per second. When you save something, it goes to storage so it persists after power off.

**Memory hierarchy (fastest to slowest):** Registers > Cache > RAM > SSD/HDD

#### Hardware vs. Software

| Type | What It Is | Examples |
|------|-----------|----------|
| Hardware | Physical components you can touch | CPU, RAM, keyboard, monitor |
| System Software | Controls and manages hardware | Windows, macOS, Linux |
| Application Software | Programs for end users | Word, browsers, games |

### Software Development Lifecycle (SDLC)

The SDLC is a structured process for building software. Think of it like building a house: you wouldn't start construction without blueprints. The 4 core phases:

| Phase | What Happens |
|-------|-------------|
| Planning | Define the problem, gather requirements, figure out scope, timeline, and resources |
| Design | Create the blueprint: system architecture, UI design, data flow, algorithm design |
| Implementation | Write the actual code, follow coding standards, use version control, document everything |
| Testing | Test individual parts (unit testing), test parts together (integration testing), let users try it (UAT), fix bugs |

**Remember:** Planning > Design > Implementation > Testing

There are also additional phases in real-world projects: Requirements Analysis, Deployment, and Maintenance & Support (this phase often lasts the longest, some software has been in production for over 60 years).

Different teams use different approaches:

| Model | How It Works |
|-------|-------------|
| Waterfall | Linear, step-by-step, each phase completed before the next |
| Agile | Iterative, short sprints (2-4 weeks), adaptable to change |
| Spiral | Risk-driven, combines iterative development with risk analysis |
| DevOps | Continuous integration and delivery, automation, dev + ops collaboration |

### Number Systems

Computers only understand 1s and 0s. We use other number systems to make binary easier to read and work with.

| System | Base | Digits | Why It Exists |
|--------|------|--------|--------------|
| Decimal | 10 | 0-9 | What humans use (probably because we have 10 fingers) |
| Binary | 2 | 0, 1 | What computers use. Transistors are either on (1) or off (0) |
| Octal | 8 | 0-7 | Shorter way to write binary (each octal digit = 3 binary bits) |
| Hexadecimal | 16 | 0-9, A-F | Even shorter (each hex digit = 4 binary bits). Used for color codes, memory addresses |

#### How to Convert

**Binary to Decimal:** Each position is a power of 2. Read right to left.

```
1101 in binary:
(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)
= 8 + 4 + 0 + 1
= 13
```

**Hex to Decimal:** Each position is a power of 16. Letters A-F = 10-15.

```
2F in hex:
(2 × 16¹) + (15 × 16⁰)
= 32 + 15
= 47
```

**Python conversion functions:**

```python
bin(10)   # '0b1010'  (decimal to binary)
oct(10)   # '0o12'    (decimal to octal)
hex(10)   # '0xa'     (decimal to hex)
```

The `0b`, `0o`, `0x` prefixes tell you which base it is. You can remove them with slicing: `bin(10)[2:]` gives you just `'1010'`.

### Data Representation

Everything in a computer is binary. Letters, images, sounds, all of it gets converted to 0s and 1s.

#### Bits and Bytes

| Unit | Size |
|------|------|
| Bit | Smallest unit. Either 0 or 1 |
| Byte | 8 bits. Can represent 256 values (0-255) |
| Kilobyte (KB) | 1,024 bytes |
| Megabyte (MB) | ~1 million bytes |
| Gigabyte (GB) | ~1 billion bytes |
| Terabyte (TB) | ~1 trillion bytes |

#### Character Encoding

| Encoding | What It Supports |
|----------|-----------------|
| ASCII | English only. 7 bits, 128 characters (0-127). 'A' = 65, 'a' = 97 |
| Extended ASCII | 8 bits, 256 characters. Adds accented characters but still not enough for all languages |
| Unicode (UTF-8) | 140,000+ characters. All languages, emojis, symbols. Variable length: 1-4 bytes per character |

Unicode was created because ASCII only handles English. UTF-8 is the most common Unicode encoding. It uses 1 byte for ASCII characters and up to 4 bytes for things like emojis.

### Debugging

Finding and fixing errors in your code. There are three types:

| Error Type | What It Is | Example |
|------------|-----------|---------|
| Syntax Error | Code structure is wrong, program won't run at all | Missing a colon, unclosed parenthesis |
| Runtime Error | Code runs but crashes during execution (also called exceptions) | Dividing by zero |
| Semantic Error | Code runs without crashing but gives the wrong result | Logic is wrong, program does what you told it to do, not what you meant |

**Process:** Identify the problem > Locate the source > Fix the error > Test the solution

## Example Code From the Class

Example code for this module is in the [course repository](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/computing).

| File | Description |
|------|-------------|
| [binary.py](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/blob/main/modules/computing/binary.py) | A Python program to convert between decimal and binary |

## Resources

- [Course GitHub Repository: Computing](https://github.com/CGCC-CS/csc101-intro-to-computing-with-python/tree/main/modules/computing)
- [ASCII Code Reference](https://www.ascii-code.com/)
- [Getting Started with Google Colab](https://www.marqo.ai/blog/getting-started-with-google-colab-a-beginners-guide)
- [Think Like a Computer Scientist](https://www.greenteapress.com/thinkpython/thinkCSpy/html/)