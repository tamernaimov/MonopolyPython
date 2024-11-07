from Space import Space

class WorldTour(Space):
    def action(self, player):
        print(f"--------------------------- {player.name}, YOU ARE IN THE WORLD TOUR---------------------------")
        answer = int(input("Choose a position to travel to!"))
        player.position = answer
        player.travelling = True