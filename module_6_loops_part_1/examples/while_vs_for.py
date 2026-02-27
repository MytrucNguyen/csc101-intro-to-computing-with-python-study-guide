# while vs for - same tasks, different loops, and when each one shines

# === TASK 1: print numbers 1 to 5 ===
# both loops can do this, but for is cleaner

print("=== Counting to 5 ===")

# while version (you manage everything yourself)
print("while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

print()

# for version (Python handles the counting)
print("for loop:")
for count in range(1, 6):
    print(count)

# same output, but the for loop is 2 lines instead of 4
# no need to initialize or update a variable

print()

# === TASK 2: iterate through a list ===
# for is the clear winner here

print("=== Printing a grocery list ===")

groceries = ["eggs", "milk", "bread", "butter"]

# for version (natural and readable)
print("for loop:")
for item in groceries:
    print(f"- {item}")

print()

# while version (works but more effort for no reason)
print("while loop:")
index = 0
while index < len(groceries):
    print(f"- {groceries[index]}")
    index += 1

print()

# === TASK 3: input validation ===
# only while works here because you don't know how many tries it'll take

print("=== Guess the number ===")

secret = 7
guess = 0

# can't use for because you have no idea how many guesses it'll take
while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    if guess != secret:
        print("Try again!")

print("You got it!")

# === QUICK REFERENCE ===
# for  -> you know how many times, or you have a sequence to loop through
# while -> you're waiting for something to happen and don't know when