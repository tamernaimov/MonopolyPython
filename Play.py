from Dice import Dice
from Player import Player
from Players import Players
class Play:
    def __init__(self):
        self.players = Players()
        self.users = self.players.setPlayers()
        self.dice = Dice()

    def setPlayers(self):
        pass
    def throwDices(self):
        for i in range(len(self.users)):
            self.dice.throwDice(self.users[i])
            print()

    def checkForContinue(self):
        if len(self.users) == 1:
            print("GAME IS OVER")
            #EXIT
            print(f"WINNER IS {self.users[0].name}")
            exit()

        for i in range(len(self.users)):
            if self.users[i].money <= 0:
                self.users.pop(i)
            else:
                break

    def playGame(self):
        self.setPlayers()  # Set up players
        print("we set up players")
        print()
        #Update Block
        while True:
            self.checkForContinue()
            self.throwDices()

