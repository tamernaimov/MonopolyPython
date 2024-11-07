from DisplayInfo import DisplayInfo
from Jail import Jail
from MakeMonopoly import MakeMonopoly
from Map import Map
from Properties.Hotel import Hotel
from Properties.House import House

class PlayerAction():
    def __init__(self):
        self.map = Map()
        self.space = self.map.space
        self.di = DisplayInfo()
        self.makeMonopoly = MakeMonopoly()
        self.jail = Jail()

    def travellingAction(self, player):
        pos = player.position - 1
        if player.travelling:
            self.space[pos].action(player)
            player.travelling = False

    def returnAction(self, player):
        pos = player.position - 1

        if player.inJail:
            self.jail.action(player)
            return

        result = self.space[pos].action(player)
        self.travellingAction(player)
        self.makeMonopoly.fromSpaceToProperties(self.space, player)
        self.di.displayInfo(player, self.space)

        if isinstance(result, House) or isinstance(result, Hotel): #Could Try with the object being Property(parent)
            self.space[pos] = result