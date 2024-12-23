from DiceForJail import DiceForJail
from Player import Player
from Space import Space

class Jail(Space):
    def __init__(self):
        self.diceForJail = DiceForJail()

    def action(self, player: Player):

        player.inJail = True
        print("You are in Jail!!!!!")
        print("Choose An option to escape!")
        answer = int(input("1.Pray for a double\n2.Pay 50 bands\n3.Use GetOutOFJail Card: "))
        print()
        if answer == 1:
            out_or_not = self.diceForJail.throwDiceOutOfJail()
            if out_or_not:
                player.inJail = False
                print("You are out of Jail!")
            else:
                print("Sorry, Not Sorry! You are NOT out of the jail!")

        elif answer == 2:
            if player.money >= 50000:
                player.money -= 50000
                print("You are out of Jail")
                player.inJail = False
            else:
                print("You dont have money bro!")

        elif answer == 3:
            if player.hasJailCard:
                print("You are out of Jail!")
                player.inJail = False
            elif not player.hasJailCard:
                print("You dont even have a Jail Card!")
