# csv processing - from raw text file to usable data
# CSVs look simple but there are a few things that trip people up

import csv
import os


# === STEP 1: what a CSV actually looks like ===
# it's just a text file where commas separate the columns
# let's create one so you can see exactly what's in it
print("=== What a CSV Looks Like ===")

with open("students.csv", "w") as f:
    f.write("Name,Age,Grade\n")
    f.write("Alice,20,92\n")
    f.write("Bob,19,85\n")
    f.write("Charlie,21,78\n")
    f.write("Diana,20,95\n")

# read it back raw to see the actual content
with open("students.csv", "r") as f:
    raw = f.read()
print("Raw file content:")
print(raw)


# === STEP 2: manual parsing (the hard way) ===
# readlines → strip → split — this is what your instructor teaches first
print("=== Manual Parsing ===")

with open("students.csv", "r") as f:
    rows = f.readlines()

# rows looks like: ['Name,Age,Grade\n', 'Alice,20,92\n', ...]
# each line still has \n at the end

data = []
for row in rows:
    row = row.strip()              # remove \n
    cells = row.split(",")         # split into list
    data.append(cells)

# data is now a 2-D list (list of lists)
print(f"Header: {data[0]}")        # ['Name', 'Age', 'Grade']
print(f"First student: {data[1]}") # ['Alice', '20', '92']
print(f"All data: {data}")
print()


# === STEP 3: skipping the header and using the data ===
# the first row is usually column names, not actual data
print("=== Skipping the Header ===")

header = data[0]
students = data[1:]                # everything after the header

for student in students:
    name = student[0]
    age = int(student[1])          # still strings! must convert
    grade = int(student[2])
    print(f"{name} is {age} years old with a grade of {grade}")
print()


# === STEP 4: the csv module (the right way) ===
# manual parsing breaks if a field contains a comma
# like: "Smith, John",25,88
# split(",") would chop "Smith, John" into two pieces
print("=== Using the csv Module ===")

with open("students.csv", newline='') as f:
    reader = csv.reader(f)
    all_rows = [row for row in reader]    # list comprehension

print(f"Header: {all_rows[0]}")
print(f"Data rows: {all_rows[1:]}")
print()


# === STEP 5: filtering data ===
# find students with a grade above 90
print("=== Filtering: Grades Above 90 ===")

with open("students.csv", newline='') as f:
    reader = csv.reader(f)
    header = next(reader)          # skip the header row

    honor_roll = []
    for row in reader:
        name = row[0]
        grade = int(row[2])
        if grade > 90:
            honor_roll.append(name)

print(f"Honor roll: {honor_roll}")   # ['Alice', 'Diana']
print()


# === STEP 6: handling bad data ===
# real CSV files have missing fields, wrong types, blank rows
print("=== Handling Bad Data ===")

# create a messy CSV
with open("messy.csv", "w") as f:
    f.write("Name,Age,Grade\n")
    f.write("Alice,20,92\n")
    f.write("Bob,,85\n")           # missing age
    f.write("Charlie,twenty,78\n") # age isn't a number
    f.write("\n")                   # blank row
    f.write("Diana,20,95\n")

with open("messy.csv", newline='') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        # skip blank rows
        if not row or all(cell.strip() == '' for cell in row):
            print("  (skipped blank row)")
            continue

        try:
            name = row[0]
            age = int(row[1])      # might fail
            grade = int(row[2])
            print(f"  {name}: age={age}, grade={grade}")
        except (ValueError, IndexError) as e:
            print(f"  Bad row {row}: {e}")
print()


# === STEP 7: writing a CSV ===
# if you need to create a CSV from your data
print("=== Writing a CSV ===")

results = [
    ["Name", "Score", "Pass"],
    ["Alice", "92", "Yes"],
    ["Bob", "58", "No"],
    ["Charlie", "78", "Yes"],
]

with open("results.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for row in results:
        writer.writerow(row)

# verify it worked
with open("results.csv", "r") as f:
    print(f.read())


# cleanup temp files
for f in ["students.csv", "messy.csv", "results.csv"]:
    if os.path.exists(f):
        os.remove(f)
print("(temp files cleaned up)")


# === QUICK REFERENCE ===
# 1. CSV = text file, commas separate columns, \n separates rows
# 2. Manual: readlines() → strip() → split(",") → 2-D list
# 3. csv module: csv.reader() handles commas in quoted fields
# 4. Always use newline='' in open() when using csv module
# 5. First row is usually the header — skip it with next(reader) or data[1:]
# 6. Data from CSV is always strings — convert with int() or float()
# 7. Wrap processing in try/except for bad data (ValueError, IndexError)