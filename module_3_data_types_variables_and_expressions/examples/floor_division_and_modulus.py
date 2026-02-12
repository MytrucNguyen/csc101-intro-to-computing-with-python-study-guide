# floor division (//) and modulus (%)

# regular division always returns a float
print(10 / 3)  # 3.3333333333333335

# floor division drops the decimal
print(10 // 3)  # 3

# modulus returns the remainder
print(10 % 3)  # 1

# practical example: extracting digits from a phone number
phone = 6025551234

area_code = phone // 10000000  # 602
prefix = phone // 10000 % 1000  # 555
line_number = phone % 10000  # 1234

print(f"({area_code}) {prefix}-{line_number}")  # (602) 555-1234

# practical example: converting minutes to hours and minutes
total_minutes = 135
hours = total_minutes // 60  # 2
minutes = total_minutes % 60  # 15
print(f"{total_minutes} minutes = {hours} hours and {minutes} minutes")
