# floor division (//) and modulus (%)

# regular division always returns a float
print(10 / 3)  # 3.3333333333333335

# floor division drops the decimal
print(10 // 3)  # 3

# modulus returns the remainder
print(10 % 3)  # 1

# practical example: converting minutes to hours and minutes
total_minutes = 135
hours = total_minutes // 60  # 2
minutes = total_minutes % 60  # 15
print(f"{total_minutes} minutes = {hours} hours and {minutes} minutes")
