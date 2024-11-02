from Player import Player

class Players():
    def __init__(self):
        self.users = []
    def setPlayers(self):
        playerNumber = int(input("Enter the number of players: "))
        for i in range(playerNumber):
            name = input(f"Enter name for player {i + 1}: ")
            player = Player(name)
            self.users.append(player)
