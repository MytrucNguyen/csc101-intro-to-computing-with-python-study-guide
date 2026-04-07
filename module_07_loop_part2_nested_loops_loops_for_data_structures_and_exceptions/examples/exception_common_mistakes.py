# exception common mistakes - what goes wrong and how to fix it


# === MISTAKE 1: bare except catches EVERYTHING ===
# this hides bugs you didn't know about
print("=== Bare except (bad habit) ===")
my_list = [10, 20, 30]
try:
    # you think this will catch a ValueError from bad input
    # but what if you also have a typo or logic error?
    result = my_list[5]  # IndexError, not ValueError
except:
    print("Something went wrong")
    # you have no idea WHAT went wrong
    # was it bad input? a missing index? a typo? who knows
print()

# the fix: catch specific types
print("=== Specific except (much better) ===")
try:
    result = my_list[5]
except IndexError:
    print("Index out of range - list only has 3 items")
    # now you know exactly what happened and can fix it
except ValueError:
    print("Bad value")
    # this would catch a different kind of error
print()


# === MISTAKE 2: too much code in the try block ===
# if 5 lines are in try and one crashes, you don't know which one
print("=== Too much in try (hard to debug) ===")
try:
    name = "Alice"
    age = int("twenty")  # this is the line that crashes
    height = 65
    weight = 150
    bmi = (weight * 703) / (height * height)
    print(f"{name}: BMI is {bmi:.1f}")
except ValueError:
    print("Something in there was a bad value... but what?")
    # was it age? height? weight? you can't tell from here
print()

# the fix: only wrap the dangerous line
print("=== Minimal try block (easy to debug) ===")
name = "Alice"
try:
    age = int("twenty")  # only the risky line is in try
except ValueError:
    print(f"Could not convert age to integer")
    age = 0  # set a default or handle it
print()


# === MISTAKE 3: not knowing when to raise vs catch ===
# catch = someone else's code might fail (user input, files, network)
# raise = YOUR code detected something wrong and wants to signal it

# catching - you're protecting against external failure
print("=== Catching (protecting against bad input) ===")
user_input = "abc"
try:
    number = int(user_input)  # this might fail, not your fault
except ValueError:
    print(f"'{user_input}' is not a number")
print()

# raising - you're enforcing your own rules
print("=== Raising (enforcing your rules) ===")


def calculate_tip(bill, tip_percent):
    if bill < 0:
        raise ValueError("Bill can't be negative")
    if tip_percent < 0 or tip_percent > 100:
        raise ValueError("Tip percent must be 0-100")
    return bill * (tip_percent / 100)


# valid input
try:
    tip = calculate_tip(50, 20)
    print(f"Tip: ${tip:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# invalid input - your function catches it before doing bad math
try:
    tip = calculate_tip(-10, 20)
    print(f"Tip: ${tip:.2f}")
except ValueError as e:
    print(f"Error: {e}")

try:
    tip = calculate_tip(50, 150)
    print(f"Tip: ${tip:.2f}")
except ValueError as e:
    print(f"Error: {e}")
print()


# === MISTAKE 4: forgetting that try skips the rest on failure ===
# if line 2 of 5 crashes, lines 3-5 in try never run
print("=== Try skips remaining lines after failure ===")
try:
    print("Step 1: starting...")  # runs
    result = 10 / 0  # crashes here
    print("Step 2: this never runs")  # skipped
    print("Step 3: this never runs")  # skipped
except ZeroDivisionError:
    print("Caught division by zero")
print("Program continues after try/except")
# if you need all steps to run independently, use separate try blocks
# or restructure your code
print()


# === MISTAKE 5: confusing else and finally ===
# else = only runs if NO exception happened
# finally = ALWAYS runs no matter what
print("=== else vs finally ===")

# test with good input
print("Good input (5):")
try:
    num = int("5")
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"  except: {e}")
else:
    print(f"  else: result is {result}")  # only this runs
finally:
    print(f"  finally: always runs")  # always runs
print()

# test with bad input
print("Bad input (0):")
try:
    num = int("0")
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"  except: {e}")  # only this runs
else:
    print(f"  else: result is {result}")
finally:
    print(f"  finally: always runs")  # always runs
print()

# test with invalid input
print("Invalid input ('abc'):")
try:
    num = int("abc")
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"  except: {e}")  # only this runs
else:
    print(f"  else: result is {result}")
finally:
    print(f"  finally: always runs")  # always runs
print()


# === MISTAKE 6: using exceptions for normal control flow ===
# exceptions are for EXCEPTIONAL situations, not everyday logic
print("=== Don't use exceptions as if-statements ===")

# WRONG - using try/except to check if a key exists
my_dict = {"name": "Alice", "age": 25}
print("Bad way (using exceptions for normal checks):")
try:
    phone = my_dict["phone"]
except KeyError:
    phone = "N/A"
print(f"  Phone: {phone}")

# BETTER - just check first with 'in' or .get()
print("Better way (check first):")
phone = my_dict.get("phone", "N/A")
print(f"  Phone: {phone}")
# use try/except for things that MIGHT fail unpredictably
# use if/else for things you can check beforehand
print()


# === QUICK REFERENCE ===
# 1. Always catch specific exception types, never bare except:
# 2. Keep try blocks small - only the line that might fail
# 3. Catch = protect against external failure. Raise = enforce your own rules
# 4. Code after a failing line in try is skipped - plan for that
# 5. else = runs on success. finally = runs always (cleanup)
# 6. Don't use exceptions as if-statements - check first when you can
