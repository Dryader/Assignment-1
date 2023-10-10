import Game #imports game logic
firstchallenge = "lost"
secondchallenge = "lost"
thirdchallenge = "lost"
#declares booleans if the user has won or lost the challenge


print("Welcome to the quest for epic loot!")
print("You have 3 challenges in order to get the loot.")
print("You also have 2 possible roles to choose from, a warrior or a wizard.")
userrole = input("Enter your role, all lowercase:") #asks the user for their role


print("You come across a group of goblins on your travels. They look like they are up to no good.")
input("Enter 1 to roll")
Game.roll() #calls the roll function from the Game.py file
if Game.rules(Game.roll(), userrole) == "win": #calls the rules function from the Game.py file
    firstchallenge = "win"
    print("You beat the goblins and continue on your journey.")
else:
    print("You lost the fight and continue on your journey")
#test

print("You see a treasure chest in the distance. You go to open it and it is locked.")
input("Enter 1 to roll")
Game.roll()
if Game.rules(Game.roll(), userrole) == "win":
    secondchallenge = "win"
    print("You opened the chest and found some loot and continue on your journey.")
else:
    print("You opened the chest and found nothing in and continue on your journey")

print("You see a giant dragon in the distance. You go to fight it")
input("Enter 1 to roll")
Game.roll()
if Game.rules(Game.roll(), userrole) == "win":
    thirdchallenge = "win"
    print("You beat the dragon!.")
else:
    print("You lost to the dragon!")

Game.winloss(firstchallenge, secondchallenge, thirdchallenge) #calls the winloss function from the Game.py file and passes the 3 strings as parameters