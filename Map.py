
from Player import Player
from Properties.House import House
from Properties.Land import Land
from Properties.Property import Property

class Map():
    def __init__(self):
        self.space = [Land("Grenada", 5000, 2000, 0, "Spain", "Land"),
                      Land("Seville", 2000, 3000, 0, "Spain", "Land"),
                      Land("Madrid", 3000, 200, 0, "Spain", "Land")]

    def returnAction(self,player):
        if player.position == 3:
            result = self.space[2].action(player)
            if isinstance(result, House):
                self.space[2] = result
                print(self.space[2].typeOfBuilding)
