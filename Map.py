from Cards.ChanceCard import ChanceCard
from Player import Player
from Properties.Beach import Beach
from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Land import Land
from Properties.PropertyFactory import PropertyFactory
from Start import Start


class Map():
    def __init__(self):
        self.space = [Start(),
                      PropertyFactory("Grenada", 5000, 2000,  "Spain", "Land").createB(),
                      PropertyFactory("Seville", 2000, 3000,  "Spain", "Land").createB(),
                      PropertyFactory("Madrid", 3000, 200,  "Spain", "Land").createB(),
                      Beach("Bali", 3000, 200),
                      PropertyFactory("Hong Kong", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Beijing", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Shanghai", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Shenzhen!", 3000, 200,  "China", "Land").createB(),#MAKE IT A JAIL THIS IS NOT RIGHT
                      PropertyFactory("Venice!", 3000, 200,  "Italy", "Land").createB(),
                      PropertyFactory("Milan", 3000, 200,  "Italy", "Land").createB(),
                      PropertyFactory("Rome", 3000, 200,  "Italy", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Hamburg!", 3000, 200,  "Germany", "Land").createB(),
                      Beach("Cyprus",3000,200),
                      PropertyFactory("Berlin", 3000, 200,  "Germany", "Land").createB(),
                      PropertyFactory("Liverpool!", 3000, 200,  "England", "Land").createB(),#MAKE THIS A WORLD CHAMPIONSHIP
                      PropertyFactory("London!", 3000, 200,"England", "Land").createB(),
                      Beach("Dubai",2000,200),
                      PropertyFactory("Sydney!", 3000, 200,  "England", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Chicago", 3000, 200,  "USA", "Land").createB(),
                      PropertyFactory("Las Vegas", 3000, 200, "USA", "Land").createB(),
                      PropertyFactory("New York", 3000, 200,  "USA", "Land").createB(),
                      PropertyFactory("Heisenberg CITY!", 3000, 200,  "USA", "Land").createB(), #World Tour
                      Beach("Nice",2000,200),
                      PropertyFactory("Lyon", 3000, 200,  "France", "Land").createB(),
                      PropertyFactory("Paris", 3000, 200,  "France", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Osaka", 3000, 200, "Spain", "Land").createB(),
                      PropertyFactory("Tokyo", 3000, 200,  "Spain", "Land").createB(),]

    def returnAction(self,player):
        pos = player.position - 1
        result = self.space[pos].action(player)
        print("\n      ------------------DONE ACTION-----------------")

        if isinstance(result, House) or isinstance(result,Land):
            print("MOMMA WE MADE IT")
            self.space[pos] = result
            print(self.space[pos].typeOfBuilding)

