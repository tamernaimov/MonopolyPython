from Cards.ChanceCard import ChanceCard
from Jail import Jail
from Player import Player
from Properties.Beach import Beach
from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Land import Land
from Properties.Property import Property
from Properties.PropertyFactory import PropertyFactory
from Start import Start
from WorldTour import WorldTour
from MakeMonopoly import MakeMonopoly

class Map():
    def __init__(self):

        self.makeMonopoly = MakeMonopoly()
        self.jail = Jail()
        self.worldTour = WorldTour()
        self.space = [Start(),
                      PropertyFactory("Grenada", 5000, 2000,  "Spain", "Land").createB(),
                      PropertyFactory("Seville", 2000, 3000,  "Spain", "Land").createB(),
                      PropertyFactory("Madrid", 3000, 200,  "Spain", "Land").createB(),
                      Beach("Bali", 3000, 200),
                      PropertyFactory("Hong Kong", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Beijing", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Shanghai", 3000, 200,  "China", "Land").createB(),
                      self.jail,
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
                      self.worldTour,
                      Beach("Nice",2000,200),
                      PropertyFactory("Lyon", 3000, 200,  "France", "Land").createB(),
                      PropertyFactory("Paris", 3000, 200,  "France", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Osaka", 3000, 200, "Spain", "Land").createB(),
                      PropertyFactory("Tokyo", 3000, 200,  "Spain", "Land").createB(),]




    def travellingAction(self,player):
        pos = player.position - 1
        if player.travelling == True:
            self.space[pos].action(player)
            player.travelling = False




    def returnAction(self,player):
        pos = player.position - 1

        if player.inJail == True:
            self.jail.action(player)
            return

        result = self.space[pos].action(player)
        self.travellingAction(player)
        print("\n      ------------------DONE ACTION-----------------        ")
        #self.makeMonopoly.fromSpaceToProperties(self.space)
        if isinstance(result, House) or isinstance(result,Land):
            self.space[pos] = result


