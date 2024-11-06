from DisplayCountries import DisplayCountries
from Jail import Jail
from MakeMonopoly import MakeMonopoly
from Map import Map
from Properties.Land import Land
from WorldTour import WorldTour


class PlayerAction():
    def __init__(self):
        self.map = Map()
        self.space = self.map.space
        self.dc = DisplayCountries()
        self.makeMonopoly = MakeMonopoly()
        self.jail = Jail()

    def travellingAction(self, player):
        pos = player.position - 1
        if player.travelling:
            self.space[pos].action(player)
            player.travelling = False

    def returnAction(self, player):
        from Properties.House import House
        pos = player.position - 1

        if player.inJail:
            self.jail.action(player)
            return

        result = self.space[pos].action(player)
        self.travellingAction(player)
        self.makeMonopoly.fromSpaceToProperties(self.space, player)
        self.dc.displayCountries(player, self.space)
        if isinstance(result, House) or isinstance(result, Land):
            self.space[pos] = result


