from Cards.ChanceCard import ChanceCard
from Player import Player
from Properties.Beach import Beach
from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Land import Land
from Properties.Property import Property
from Start import Start


class Map():
    def __init__(self):
        self.space = [Start(),
                      Property("Grenada", 5000, 2000, 0, "Spain", "Land").define(),
                      Property("Seville", 2000, 3000, 0, "Spain", "Land").define(),
                      Land("Madrid", 3000, 200, 0, "Spain", "Land"),
                      Beach("Bali", 3000, 200),
                      Property("Hong Kong", 3000, 200, 0, "China", "Land").define(),
                      Property("Beijing", 3000, 200, 0, "China", "Land").define(),
                      Property("Shanghai", 3000, 200, 0, "China", "Land").define(),
                      Property("Shenzhen!", 3000, 200, 0, "China", "Land").define(),#MAKE IT A JAIL THIS IS NOT RIGHT
                      Property("Venice!", 3000, 200, 0, "Italy", "Land").define(),
                      Property("Milan", 3000, 200, 0, "Italy", "Land").define(),
                      Property("Rome", 3000, 200, 0, "Italy", "Land").define(),
                      ChanceCard(),
                      Property("Hamburg!", 3000, 200, 0, "Germany", "Land").define(),
                      Beach("Cyprus",3000,200),
                      Property("Berlin", 3000, 200, 0, "Germany", "Land").define(),
                      Property("Liverpool!", 3000, 200, 0, "England", "Land").define(),#MAKE THIS A WORLD CHAMPIONSHIP
                      Property("London!", 3000, 200, 0, "England", "Land").define(),
                      Beach("Dubai",2000,200),
                      Property("Sydney!", 3000, 200, 0, "England", "Land").define(),
                      ChanceCard(),
                      Property("Chicago", 3000, 200, 0, "USA", "Land").define(),
                      Property("Las Vegas", 3000, 200, 0, "USA", "Land").define(),
                      Property("New York", 3000, 200, 0, "USA", "Land").define(),
                      Property("Heisenberg CITY!", 3000, 200, 0, "USA", "Land").define(), #World Tour
                      Beach("Nice",2000,200),
                      Property("Lyon", 3000, 200, 0, "France", "Land").define(),
                      Property("Paris", 3000, 200, 0, "France", "Land").define(),
                      ChanceCard(),
                      Property("Osaka", 3000, 200, 0, "Spain", "Land").define(),
                      Property("Tokyo", 3000, 200, 0, "Spain", "Land").define(),]




    def returnAction(self,player):
        pos = player.position - 1
        result = self.space[pos].action(player)
        print("------------------DONE ACTION-----------------")
        if isinstance(result, House):
            print("MOMMA WE MADE IT")
            self.space[pos] = result
            print(self.space[pos].typeOfBuilding)
