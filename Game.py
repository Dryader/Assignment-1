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

        
def winloss(result1, result2, result3):
    if result1 == "win" and result2 == "win" and result3 == "win":
        print("You have won the game, congratulations!")
    else:
        print("You have lost the game, better luck next time!")