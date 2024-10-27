import random

from Map import Map


class Dice():
    def __init__(self):
        self.map = Map()

    def throwDice(self, player):
        while True:
            a = random.randint(1,1)
            b = random.randint(2,2)
            print(f"Dices Thrown by {player.name} were {a} And {b}")

            if a == b:
                player.position += a+b
                self.map.returnAction(player)
                print()
                if player.position >= 31:
                    player.position -= 31
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}")
                    print(f"Current Position for {player.name} is {player.position}")
                else:
                    print(f"Current Position for {player.name} is {player.position}")

            else:
                #print("No double for you!")
                player.position += a+b
                self.map.returnAction(player)
                print(f"Current Position for {player.name} is {player.position}")
                if player.position >= 31:
                    player.position -= 31
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}")
                break

