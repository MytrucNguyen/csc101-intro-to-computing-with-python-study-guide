# sep and end parameters in print()

# sep changes what goes between values (default is a space)
print("apple", "banana", "cherry")  # apple banana cherry
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry
print("apple", "banana", "cherry", sep=" | ")  # apple | banana | cherry
print(2025, 1, 15, sep="-")  # 2025-1-15
print("a", "b", "c", sep="")  # abc (no separator)

print()  # blank line

# end changes what prints at the end (default is a newline)
print("hello", end=" ")
print("world")  # hello world (on the same line)

print("loading", end="...")
print("done!")  # loading...done!
