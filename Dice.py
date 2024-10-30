import random

from Map import Map


class Dice():
    def __init__(self):
        self.map = Map()

    def throwDice(self, player):
        while True:
            a = random.randint(1,6)
            b = random.randint(1,6)
            print(f"Dices Thrown by {player.name} were {a} And {b}")

            if a == b:
                player.position += a+b

                print()
                if player.position >= 31:
                    player.position -= 31
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}")
                    print(f"Current Position for {player.name} is {player.position}")
                    self.map.returnAction(player)
                else:
                    print(f"Current Position for {player.name} is {player.position}")
                    self.map.returnAction(player)

            else:
                player.position += a+b


                if player.position >= 31:
                    player.position -= 31
                    print(f"Current Position for {player.name} is {player.position}")
                    self.map.returnAction(player)
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}")
                else:
                    print(f"Current Position for {player.name} is {player.position}")
                    self.map.returnAction(player)
                break

