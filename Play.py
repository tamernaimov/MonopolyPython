from Dice import Dice
from Players import Players
class Play:
    def __init__(self):
        self.players = Players()
        self.users = self.players.setPlayers()
        self.dice = Dice()

    def throwDices(self):
        for i in range(len(self.users)):
            self.dice.throwDice(self.users[i])
            print()

    def checkForContinue(self):
        if len(self.users) == 1:
            print(f"GAME IS OVER\nWINNER IS {self.users[0].name} \n Thanks For Playing!")
            exit()

        for i in range(len(self.users)):
            if self.users[i].money <= 0:
                print(f"{self.users[i].name} HAS GONE BANKRUPT")
                self.users.pop(i)
            else:
                break

    def playGame(self):
        print("Players are Set!\n")
        #Update Block
        while True:
            self.checkForContinue()
            self.throwDices()