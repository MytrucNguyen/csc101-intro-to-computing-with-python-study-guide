# sets vs dicts - they both use {} but they're completely different

# THE GOTCHA: {} creates an empty DICTIONARY, not a set
mystery = {}
print(f"type of {{}}: {type(mystery)}")  # <class 'dict'>

# to make an empty set, you MUST use set()
empty_set = set()
print(f"type of set(): {type(empty_set)}")  # <class 'set'>

print()

# once they have items, the syntax is different
my_set = {1, 2, 3}  # just values
my_dict = {"a": 1, "b": 2, "c": 3}  # key: value pairs

print(f"set:  {my_set}")
print(f"dict: {my_dict}")

print()

# SETS: unordered, unique items, no keys, no indexing
colors = {"red", "blue", "green", "red"}  # duplicate "red" is removed
print(f"set with duplicates removed: {colors}")
# print(colors[0])   # TypeError - sets don't support indexing

# DICTS: key-value pairs, access by key
prices = {"apple": 1.50, "banana": 0.75}
print(f"apple costs: ${prices['apple']}")  # access by key, not index

print()

# when to use which:
# SET  = "I just need a collection of unique things"
#        checking membership, removing duplicates, set math (union, intersection)
# DICT = "I need to look things up by a label"
#        phone book, student records, config settings, word counts

# practical example: removing duplicates from a list
names_with_dupes = ["Ada", "Grace", "Ada", "Margaret", "Grace"]
unique_names = list(set(names_with_dupes))
print(f"duplicates removed: {unique_names}")
