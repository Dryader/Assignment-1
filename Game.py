import Role1
import Role2
def roll():
    import random
    return random.randint(1, 12)

def rules(result, userrole):
    if result <= 3:
        print("You have failed the challenge and have lost an attribute point.")
        if userrole == "warrior":
            Role1.warrior[0] = Role1.warrior[0] - 1
        elif userrole == "wizard":
            Role2.wizard[2] = Role2.wizard[2] - 1
        return "lost"

    elif result <= 7:
        print("You have failed the challenge and didn't lose an attribute point")
        return "lost"
    elif result <= 10:
        print("You have succeeded the challenge and didnt gain an attribute point")
        return "win"
    elif result <= 12:
        print("You have succeeded the challenge and have gained an attribute point")
        if userrole == "warrior":
            Role1.warrior[0] = Role1.warrior[0] -+1
        elif userrole == "wizard":
            Role2.wizard[2] = Role2.wizard[2] + 1
        return "win"


        
def winloss(result1, result2, result3):
    if result1 == "win" and result2 == "win" and result3 == "win":
        print("You have won the game, congratulations!")
    else:
        print("You have lost the game, better luck next time!")