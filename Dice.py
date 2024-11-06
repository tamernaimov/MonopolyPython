import random

from PlayerAction import PlayerAction


class Dice():
    def __init__(self):
        self.pa = PlayerAction()

    def throwDice(self, player):
        while True:
            if player.inJail == True:
                self.pa.returnAction(player)
                return

            a = random.randint(1,6)
            b = random.randint(1,6)
            print(f"Dices Thrown by {player.name} were {a} And {b}")
            if a == b:
                player.position += a+b

                print("YOU JUST THREW A DOUBLE(Lucky)")
                if player.position >= 31:
                    player.position -= 31
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}")
                    print(f"Current Position for {player.name} is {player.position}\n")
                    self.pa.returnAction(player)
                else:
                    print(f"Current Position for {player.name} is {player.position}\n")
                    self.pa.returnAction(player)

            else:
                player.position += a+b
                if player.position >= 31:
                    player.position -= 31
                    print(f"Current Position for {player.name} is {player.position}\n")
                    self.pa.returnAction(player)
                    player.money += 500000
                    print(f"{player.name}'s money is currently {player.money}\n")
                else:
                    print(f"Current Position for {player.name} is {player.position}\n")
                    self.pa.returnAction(player)

                break

    def throwDiceOutOfJail(self,player):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(f"{player.name} Threw {a} and {b}")
        if a==b:
            return True
        else:
            return False


