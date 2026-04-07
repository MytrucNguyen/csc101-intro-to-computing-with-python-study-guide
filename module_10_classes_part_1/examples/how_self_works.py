# how self works - the thing everyone nods along to but doesn't actually get
# self is just Python's way of saying "this specific object right here"


# === WHAT ACTUALLY HAPPENS WHEN YOU CALL A METHOD ===
# when you write my_dog.bark(), Python secretly translates it to Dog.bark(my_dog)
# self is just the variable that catches the instance
print("=== What Python Does Behind the Scenes ===")


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")


buddy = Dog("Buddy")
rex = Dog("Rex")

# these two lines do the EXACT same thing
buddy.bark()  # Buddy says Woof!  (Python passes buddy as self)
Dog.bark(buddy)  # Buddy says Woof!  (you pass buddy manually)

# when you call rex.bark(), self becomes rex
# when you call buddy.bark(), self becomes buddy
# self is just a placeholder for "whichever object called this method"
rex.bark()  # Rex says Woof!
print()


# === TRACING SELF THROUGH A CLASS ===
# follow self from __init__ through every method call
print("=== Tracing self Step by Step ===")


class Student:
    def __init__(self, name, grade):
        # self is the NEW object being created
        # self.name stores "Alice" ON that specific object
        self.name = name
        self.grade = grade
        print(f"  __init__: self is {self}, storing name='{name}'")

    def study(self, hours):
        # self is whichever student called .study()
        bonus = hours * 2
        self.grade += bonus
        print(f"  study: self.name is '{self.name}', grade is now {self.grade}")

    def get_report(self):
        # same self - same student
        return f"{self.name}: grade {self.grade}"


print("Creating alice:")
alice = Student("Alice", 75)

print("\nCreating bob:")
bob = Student("Bob", 60)

print("\nalice.study(5):")
alice.study(5)  # self = alice, grade goes from 75 to 85

print("bob.study(3):")
bob.study(3)  # self = bob, grade goes from 60 to 66

# alice and bob are independent - studying one doesn't affect the other
print(f"\n{alice.get_report()}")  # Alice: grade 85
print(bob.get_report())  # Bob: grade 66
print()


# === SELF CONNECTS THE INSIDE TO THE OUTSIDE ===
# self.name inside the class IS the same thing as my_object.name outside
print("=== Inside vs Outside the Class ===")


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        # self.color inside here...
        print(f"A {self.color} {self.model}")


my_car = Car("red", "Honda")

# ...is the same as my_car.color out here
print(my_car.color)  # red
my_car.describe()  # A red Honda

# changing it from outside changes what self sees inside
my_car.color = "blue"
my_car.describe()  # A blue Honda
print()


# === METHODS CALLING OTHER METHODS WITH SELF ===
# inside a class, you call your own methods with self.method_name()
print("=== Methods Calling Methods ===")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        # calling area() and perimeter() from inside the class
        a = self.area()
        p = self.perimeter()
        print(f"{self.width}x{self.height} rectangle: area={a}, perimeter={p}")


r = Rectangle(5, 3)
r.describe()  # 5x3 rectangle: area=15, perimeter=16
print()


# === THE MISTAKE THAT PROVES YOU DON'T GET SELF YET ===
# if you forget self, the method can't find the object's data
print("=== The Proof ===")


class Broken:
    def __init__(self, x):
        self.x = x

    def double(self):
        # return x * 2          # NameError! 'x' doesn't exist as a local variable
        return self.x * 2  # self.x tells Python: get x from THIS object


b = Broken(5)
print(b.double())  # 10

# without self, Python looks for a local variable called x
# there isn't one, so it crashes
# self.x says "go to this specific object and get its x"
print()


# === QUICK REFERENCE ===
# 1. self = the specific object that called the method
# 2. my_dog.bark() is secretly Dog.bark(my_dog) — Python passes the instance for you
# 3. self.name inside the class = my_dog.name outside the class (same data)
# 4. use self.attribute to read/write the object's data inside any method
# 5. use self.method() to call another method from inside the class
# 6. without self, Python looks for a local variable — not the object's attribute
