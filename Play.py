from Dice import Dice
from Player import Player
from Map import Map
class Play:
    def __init__(self):
        self.dice = Dice()
        self.users = []

    def setPlayers(self):
        playerNumber = int(input("Enter the number of players: "))
        for i in range(playerNumber):
            name = input(f"Enter name for player {i + 1}: ")
            player = Player(name)
            self.users.append(player)

    def throwDices(self):
        for i in range(len(self.users)):
            self.dice.throwDice(self.users[i])
            print()

    def checkForContinue(self):
        if len(self.users) == 1:
            print("GAME IS OVER")
            #EXIT
            exit()
            print(f"WINNER IS {self.users[0].name}")

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


