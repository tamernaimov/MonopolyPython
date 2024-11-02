from Space import Space


class WorldTour(Space):
    def action(self, player):
        print("---------------------------YOU ARE IN THE WORLD TOUR BABY BOY---------------------------")
        answer = int(input("Choose a position to travel to!"))
        player.position = answer
        player.travelling = True