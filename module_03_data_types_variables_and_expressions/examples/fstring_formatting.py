# f-string formatting examples

name = "Ada"
age = 25
price = 7600.1
number = 4
hex_num = 31

# basic f-string
print(f"Name: {name}, Age: {age}")

# :.2f - 2 decimal places (good for money)
print(f"Price: ${price:.2f}")  # $7600.10

# :,d - commas in integers
print(f"Population: {1000000:,d}")  # 1,000,000

# :,.2f - commas + 2 decimal places
print(f"Salary: ${75000.50:,.2f}")  # $75,000.50

# :02d - leading zeros
print(f"Day: {number:02d}")  # 04

# :b - binary
print(f"Binary of {number}: {number:b}")  # 100

# :x - hexadecimal
print(f"Hex of {hex_num}: {hex_num:x}")  # 1f

# :e - scientific notation
print(f"Scientific: {44:e}")  # 4.400000e+01

# you can also do math inside f-strings
hours = 40
rate = 25.50
print(f"Weekly pay: ${hours * rate:,.2f}")  # $1,020.00
