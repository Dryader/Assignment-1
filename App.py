print("Welcome to the quest for epic loot!")
print("You have 3 challenges in order to get the loot.")
print("You also have 2 possible roles to choose from, a warrior or a wizard.")
userrole = input("Enter your role, all lowercase:")


print("You come across a group of goblins on your travels. They look like they are up to no good. What do you do?")
input("Enter 1 to roll")

def roll():
    import random
    return random.randint(1, 12)

def rules():
    if roll() <= 3:
        print("You have failed the challenge and have lost an attribute point.")

    elif roll() <= 7:
        print("You have failed the challenge and didn't lose an attribute point")

    elif roll() <= 10:
        print("You have succeeded the challenge and didnt gain an attribute point")

    elif roll() <= 12:
        print("You have succeeded the challenge and have gained an attribute point")