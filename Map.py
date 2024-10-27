
from Player import Player
from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Land import Land
from Properties.Property import Property

class Map():
    def __init__(self):
        self.space = [Land("Grenada", 5000, 2000, 0, "Spain", "Land"),
                      Land("Seville", 2000, 3000, 0, "Spain", "Land"),
                      Land("Madrid", 3000, 200, 0, "Spain", "Land"),
                      Land("OHIO!", 3000, 200, 0, "Spain", "Land"),
                      Land("OHIO!", 3000, 200, 0, "Spain", "Land"),
                      Land("OHIO!", 3000, 200, 0, "Spain", "Land"),
                      Land("OHIO!", 3000, 200, 0, "Spain", "Land")]

    def returnAction(self,player):



        pos = player.position - 1

        result = self.space[pos].action(player)
        print("------------------DONE ACTION-----------------")
        if isinstance(result, House):
            self.space[pos] = result
            print(self.space[pos].typeOfBuilding)
