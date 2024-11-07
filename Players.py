from Player import Player

class Players():
    def __init__(self):
        self.users = []
    def setPlayers(self):
        player_amount = int(input("Enter the number of players: "))
        for i in range(player_amount):
            name = input(f"Enter name for player {i + 1}: ")
            player = Player(name)
            self.users.append(player)
        return self.users