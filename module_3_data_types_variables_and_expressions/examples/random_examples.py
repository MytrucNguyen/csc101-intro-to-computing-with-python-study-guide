# random module examples
import random

# randint: random integer between two values (inclusive)
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# random: random float between 0.0 and 1.0
coin_flip = random.random()
print(f"Random float: {coin_flip}")

# choice: picks a random item from a list
foods = ["tacos", "pizza", "sushi", "ramen", "pho"]
lunch = random.choice(foods)
print(f"You should eat: {lunch}")
