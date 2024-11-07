from Space import Space

class Start(Space):
    def action(self,player):
        player.money += 500000
        print("You made good money Boy :)")