# class vs instance attribute traps - the stuff that silently breaks your OOP code
# classes are straightforward until you hit these edge cases


# === TRAP 1: shadowing a class attribute through an instance ===
# assigning through an instance does NOT change the class attribute
# it creates a brand-new instance attribute that hides it
print("=== Shadowing a Class Attribute ===")


class Dog:
    species = "Canis familiaris"  # class attribute - shared by all dogs

    def __init__(self, name):
        self.name = name  # instance attribute - unique per dog


rex = Dog("Rex")
luna = Dog("Luna")

print(rex.species)  # Canis familiaris (from the class)
print(luna.species)  # Canis familiaris (from the class)

rex.species = "Canis lupus"  # this creates an INSTANCE attribute on rex only!

print(f"rex.species:  {rex.species}")  # Canis lupus (rex's own copy)
print(f"luna.species: {luna.species}")  # Canis familiaris (still the class attribute)
print(f"Dog.species:  {Dog.species}")  # Canis familiaris (class attribute unchanged)

# the fix: change class attributes through the CLASS NAME, not an instance
Dog.species = "Canis lupus"
print(f"After fix - luna.species: {luna.species}")  # Canis lupus (now everyone sees it)
print()


# === TRAP 2: mutable class attributes are shared by everyone ===
# if a class attribute is a list or dict, ALL instances point to the SAME object
# appending from one instance affects every instance
print("=== Mutable Class Attribute (the shared list bug) ===")


class BadDog:
    tricks = []  # ONE list shared by ALL dogs

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


fido = BadDog("Fido")
buddy = BadDog("Buddy")
fido.add_trick("roll over")
buddy.add_trick("play dead")

print(f"fido.tricks:  {fido.tricks}")  # ['roll over', 'play dead'] - wait what?
print(f"buddy.tricks: {buddy.tricks}")  # ['roll over', 'play dead'] - same list!
print(f"Same object?  {fido.tricks is buddy.tricks}")  # True

# the fix: put the list in __init__ so each instance gets its own
print("\n--- Fix: list in __init__ ---")


class GoodDog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # each dog gets its OWN list

    def add_trick(self, trick):
        self.tricks.append(trick)


rex = GoodDog("Rex")
luna = GoodDog("Luna")
rex.add_trick("shake")
luna.add_trick("sit")

print(f"rex.tricks:  {rex.tricks}")  # ['shake']
print(f"luna.tricks: {luna.tricks}")  # ['sit'] - independent!
print()


# === TRAP 3: forgetting self. — the silent bug ===
# without self., Python creates a local variable that disappears
# when __init__ ends. no error, just missing data.
print("=== Forgetting self. ===")


class Broken:
    def __init__(self, value):
        value = value  # local variable - gone after __init__ ends


b = Broken(42)
try:
    print(b.value)
except AttributeError as e:
    print(f"Error: {e}")
    print("The attribute was never saved - 'value = value' just assigned to a local")


class Fixed:
    def __init__(self, value):
        self.value = value  # saved to the instance


f = Fixed(42)
print(f"Fixed version: {f.value}")  # 42
print()


# === TRAP 4: forgetting self in a method definition ===
# every instance method needs self as the first parameter
# without it, Python passes the instance but has nowhere to put it
print("=== Missing self in Method ===")


class Greeter:
    def __init__(self, name):
        self.name = name

    # def greet():                  # WRONG - would cause TypeError
    #     print("Hello!")

    def greet(self):  # CORRECT - self receives the instance
        print(f"Hello from {self.name}!")


g = Greeter("Alice")
g.greet()  # Hello from Alice!
print()


# === TRAP 5: calling a method on the class instead of an instance ===
# you need to create an object first, then call methods on it
print("=== Class vs Instance Method Call ===")


class Car:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"This car is {self.color}")


# Car.describe()                    # TypeError - no instance, no self
my_car = Car("red")
my_car.describe()  # This car is red
print()


# === QUICK REFERENCE ===
# 1. Class attribute = defined in class body, shared by ALL instances
# 2. Instance attribute = defined in __init__ with self., unique per object
# 3. Change class attributes via ClassName.attr, not instance.attr (or you shadow it)
# 4. Mutable class attributes (lists, dicts) are shared - almost always a bug
# 5. Always use self.attr = value in __init__ or the data disappears
# 6. Every instance method needs self as its first parameter
# 7. Create an instance first, then call methods on it
