import Role1
import Role2
def roll(): #function to roll a 12 sided dice
    import random
    return random.randint(1, 12) #returns a random number between 1 and 12

def rules(result, userrole):
    if result <= 3:
        print("You have failed the challenge and have lost an attribute point.")
        if userrole == "warrior":
            Role1.warrior[0] = Role1.warrior[0] - 1 #subtracts 1 from the strength value in the warrior list
        elif userrole == "wizard":
            Role2.wizard[2] = Role2.wizard[2] - 1 #subtracts 1 from the intelligence value in the wizard list
        return "lost"

    elif result <= 7:
        print("You have failed the challenge and didn't lose an attribute point")
        return "lost" #returns a string to be used in the winloss function
    elif result <= 10:
        print("You have succeeded the challenge and didnt gain an attribute point")
        return "win" #returns a string to be used in the winloss function
    elif result <= 12:
        print("You have succeeded the challenge and have gained an attribute point")
        if userrole == "warrior":
            Role1.warrior[0] = Role1.warrior[0] + 1 #adds 1 to the strength value in the warrior list
        elif userrole == "wizard":
            Role2.wizard[2] = Role2.wizard[2] + 1 #adds 1 to the intelligence value in the wizard list
        return "win" #returns a string to be used in the winloss function


        
def winloss(result1, result2, result3): #function to check if the user has won or lost all 3 challenges taking into account 3 "win" strings
    if result1 == "win" and result2 == "win" and result3 == "win":
        print("You have won the game, congratulations!")
    else:
        print("You have lost the game, better luck next time!")